from array import array
from datetime import datetime, date
import datetime
from unicodedata import name
from urllib import response
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django import forms
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db import IntegrityError
from django.views.decorators.clickjacking import xframe_options_exempt

from .models import *
from .utils import Calendar

message_l = ""
message_r = ""

class UserForm(ModelForm):
    user_image = forms.ImageField()
    class Meta:
        model = User
        fields = ['user_image']

class PdfForm(ModelForm):
    pdf = forms.FileField(label='', widget=forms.FileInput(attrs={'id': 'pdf_input', 'onchange': 'add_pdf_itens()', 'multiple': 'true'}))
    class Meta:
        model = Studys
        fields = ['pdf']

class AudioForm(ModelForm):
    teaching_audio = forms.FileField(label='', widget=forms.FileInput(attrs={'id': 'input_audio', 'accept': 'audio/*', 'required': 'true'}))
    class Meta:
        model = Studys
        fields = ['teaching_audio']

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return date.today()

@xframe_options_exempt
def index(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("content"))
    else:
        form_image = UserForm()
        return render(request, "study_plan/index.html",{
            "form_image" : form_image,
            "message_l": message_l,
            "message_r": message_r
        })

@xframe_options_exempt
def content(request):

    if request.user.is_authenticated:
        d = get_date(request.GET.get('day', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(request.user, withyear=True)
        today = date.today()
        sciences = Sciences.objects.all()
        all_studys = Studys.objects.all()
        review_today = Studys.objects.all()
        for study in review_today:
            if study.rev1_date != today and study.rev2_date != today and study.rev3_date != today and study.rev4_date != today:
                review_today.exclude(id=study.id)

        form_pdf = PdfForm()
        form_audio = AudioForm()

        return render(request, "study_plan/content.html",{
            "user" : request.user,
            "all_studys" : all_studys,
            "review_today" : review_today,
            "sciences" : sciences,
            "calendar" : html_cal,
            "form_pdf" : form_pdf,
            "form_audio" : form_audio
        })
    else:
        return HttpResponseRedirect(reverse("index"))

def login_view(request):
    if request.method == "POST":
        global message_l
        global message_r
        message_r = ""
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            message_l = ""
            return HttpResponseRedirect(reverse("index"))
        else:
            message_l = "Invalid username and/or password."
            return HttpResponseRedirect(reverse("index"))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        global message_r
        global message_l
        message_l = ""
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if username == '' or email == '' or password == '' or confirmation == '':
            message_r = "Fill in all fields."
            return HttpResponseRedirect(reverse("index"))

        elif User.objects.filter(username=username).exists():
            message_r = "This username already exist."
            return HttpResponseRedirect(reverse("index"))

        elif password != confirmation:
            message_r = "Passwords must match."
            return HttpResponseRedirect(reverse("index"))
        
        elif User.objects.filter(email__exact=email).exists():
            message_r = "This email already been registered"
            return HttpResponseRedirect(reverse("index"))

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            new_user = User.objects.get(username=username)
            form_image = UserForm(request.POST, request.FILES, instance=new_user)
            if form_image.is_valid():
                form_image.save()
        except IntegrityError:
            message_r = "Username already taken."
            return HttpResponseRedirect(reverse("index", kwargs={"reload_register":1}))

        login(request, user)
        return HttpResponseRedirect(reverse("index"))

def create_study(request, type, topic_selected):
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            form_pdf = PdfForm(request.POST, request.FILES)
            form_audio = AudioForm(request.POST, request.FILES)
            if request.POST["textarea_study"]:
                textarea_study = request.POST["textarea_study"]
            if request.POST["post_type"]:
                if request.POST["post_type"] == "public":
                    post_type = True
                else:
                    post_type = False
            if request.POST["credit_study"]:
                if request.POST["credit_study"] == "by_me":
                    credit_name = request.user.username
                else:
                    credit_name = request.POST["credit_name"]
            if request.POST["summary_study"]:
                summary_study = request.POST["summary_study"]
            if request.POST["textarea_study"]:
                textarea_study = request.POST["textarea_study"]
            if request.POST["title"]:
                title = request.POST["title"]
            if request.POST["name_study_topics"]:
                name_study_topics = request.POST.getlist('name_study_topics')

            try:
                study = Studys.objects.create(title=title, public=post_type, user_create=request.user, credit=credit_name, summary=summary_study, content=textarea_study)
                study.save()
                new_study = Studys.objects.get(title=title)
                for item in name_study_topics:
                    name = item.replace("_", " ")
                    if SubArea.objects.filter(name=name).exists():
                        area = SubArea.objects.get(name=name)
                        new_study.area.add(area)
                    elif SubTopic.objects.filter(name=name).exists():
                        if SubTopic.objects.filter(name=name)[0]:
                            topics = SubTopic.objects.filter(name=name).all()
                            for topic in topics:
                                new_study.topic.add(topic)
                    else:
                        return HttpResponse(f"{name_study_topics}")
                new_study.save()
                if form_audio.is_valid():
                        for f in request.FILES.getlist('teaching_audio'):
                            audio_doc = Docs.objects.create(type='mp3', file=f)
                            audio_doc.save()
                            for area in new_study.area.all():
                                audio_doc.area.add(area)
                            for topic in new_study.topic.all():
                                audio_doc.topic.add(topic)
                            audio_doc.save()
                            new_study.teaching_audio.add(audio_doc)
                            if audio_doc != None:
                                doc_created_audio = 1
                if form_pdf.is_valid():
                        for f in request.FILES.getlist('pdf'):
                            pdf_doc = Docs.objects.create(type='pdf', file=f)
                            pdf_doc.save()
                            for area in new_study.area.all():
                                pdf_doc.area.add(area)
                            for topic in new_study.topic.all():
                                pdf_doc.topic.add(topic)
                            pdf_doc.save()
                            new_study.pdf.add(pdf_doc)
                            if pdf_doc != None:
                                doc_created_pdf = 1
                if doc_created_audio and doc_created_pdf:
                    return HttpResponseRedirect(reverse("index"))

            except IntegrityError:
                message_r = "Error on create study."
                return HttpResponseRedirect(reverse("index"))

        else:
            sciences = Sciences.objects.all()
            subtopics = SubTopic.objects.values_list("name", flat=True)
            subtopics = list(subtopics)
            subareas = SubArea.objects.values_list("name", flat=True)
            subareas = list(subareas)
            topics_opt = subareas + subtopics
            topics_opt.sort()
            all_topics = list(dict.fromkeys(topics_opt))

            form_pdf = PdfForm()
            form_audio = AudioForm()

            return render(request, "study_plan/create_study.html", {
                "topics" : all_topics,
                "topic_selected" : topic_selected,
                "topic_type" : type,
                "form_pdf": form_pdf,
                "form_audio": form_audio,
                "sciences" : sciences,
            })
    else:
        return HttpResponseRedirect(reverse('index'))

#________________________________________API REQUESTS______________________________________
@login_required
def get_content_items(request, type, name, content_name, is_review):
    name.replace("_", " ")

    #___ a = area _____t = topic____
    if type == "a":
        if content_name.lower() == "studys":
            area_obj = SubArea.objects.get(name=name.capitalize())
            content_items = Studys.objects.filter(area=area_obj, public=True).all()
        elif content_name.lower() == "courses":
            area_obj = SubArea.objects.get(name=name.capitalize())
            content_items = Courses.objects.filter(areas=area_obj).all()

    elif type == "t":
        if content_name.lower() == "studys":
            topic_obj = SubTopic.objects.get(name=name.title())
            content_items = Studys.objects.filter(topic=topic_obj, public=True).all()
        elif content_name.lower() == "courses":
            topic_obj = SubTopic.objects.get(name=name.title())
            content_items = Courses.objects.filter(topics=topic_obj).all()
    elif type == "all":
        if content_name.lower() == "studys":
            if is_review == "1":
                content_items = Studys.objects.filter(user_create=request.user).all()
            else:
                content_items = Studys.objects.filter(public=True).all()
        elif content_name.lower() == "courses":
            content_items = Courses.objects.all()
    try:
        return JsonResponse([content_item.serialize() for content_item in content_items], safe=False)
    except:
        return JsonResponse([], safe=False)

@login_required
def get_study_items(request, type, name):

    if type == 'subtopic':
        topic = SubTopic.objects.get(name=name.capitalize())
        study_items = Studys.objects.filter(topic=topic).all()
    if type == 'subarea':
        area = SubArea.objects.get(name=name.capitalize())
        study_items = Studys.objects.filter(area=area).all()

    return JsonResponse([study_item.serialize() for study_item in study_items], safe=False)


@login_required
def get_subareas(request, science):
    science_name = science.replace("_"," ")
    obj_science = Sciences.objects.get(name=science_name)
    subareas = SubArea.objects.filter(science=obj_science).all().order_by("name")
    return JsonResponse([subarea.serialize() for subarea in subareas], safe=False)

@login_required
def get_subtopics(request, subarea):
    subarea_name = subarea.replace("_"," ")
    obj_subarea = SubArea.objects.get(name=subarea_name)
    subtopics = SubTopic.objects.filter(sub_area=obj_subarea).all().order_by("name")
    return JsonResponse([subtopic.serialize() for subtopic in subtopics], safe=False)

def verifi_username(request, username_input):
    try:
        exist_username = User.objects.get(username=username_input)

        if exist_username != None:
            return JsonResponse({"exist":1}, safe=False)
    except:
        return JsonResponse({"exist":0}, safe=False)

def verifi_email(request, email_input):
    try:
        exist_email = User.objects.get(email__exact=email_input)

        if exist_email != None:
            return JsonResponse({"exist":1}, safe=False)
    except:
        return JsonResponse({"exist":0}, safe=False)

