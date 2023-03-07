from datetime import datetime
from email.policy import default
from genericpath import exists
from pyexpat import model
from random import choices
from unicodedata import name
from urllib import request
from urllib.parse import urljoin
from venv import create
from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
from datetime import datetime
from datetime import timedelta
from django.utils import timezone
from multiselectfield import MultiSelectField

#____________________FILES and DOCS____________________
def get_upload_path(instance, filename):
    return 'docs/{0}/{1}'.format(instance.type, filename)


class Docs(models.Model):
    doc_types = [('pdf','pdf'),('mp3','mp3')]

    file = models.FileField(upload_to=get_upload_path, blank=False, default='')
    type = models.CharField(choices=doc_types, max_length=10, default='pdf')
    area = models.ManyToManyField('SubArea', blank=True, related_name="files_by_area")
    topic = models.ManyToManyField('SubTopic', blank=True, related_name="files_by_topic")

    def __str__(self):
        return f"{self.file.url}"

    def serialize(self):
        return {
            "file" : self.file.url,
            "type" : self.type,
            "area" : [area.name for area in self.area.all()],
            "topic" : [topic.name for topic in self.topic.all()],
        }


#____________________USER and PROFILES________________________
class User(AbstractUser):
    user_image = models.ImageField(upload_to="users/profile_pic", default='users/profile_pic/default.png')

    def __str__(self):
        return f"{self.username}"
    
    def serialize(self):
        return {
            "id" : self.id,
            "username" : self.username,
            "user_image" : self.user_image.url,
        }

class Instructors(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="instructor_user")
    courses = models.ManyToManyField('Courses', blank=True, related_name="instructor_courses")

    def __str__(self):
        return f"{self.user}"
    
    def serialize(self):
        return {
            "user" : self.user.username,
            "courses" : [course.name for course in self.courses.all()],
        }

class Students(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_user")
    courses = models.ManyToManyField('Courses', blank=True, related_name="student_courses")


#__________________EDUCATION and STUDYS_____________________
class Sciences(models.Model):
    name = models.CharField(max_length=100)
    icon = models.FileField(upload_to="icons/sciences/", blank=False)

    def __str__(self):
        return f"{self.name}"

    def namejs(self):
        name = self.name
        name = name.replace(" ","_")
        return f"{name}"
    
    def serialize(self):
        return {
            "name" : self.name,
        }

class SubArea(models.Model):
    name = models.CharField(max_length=100)
    science = models.ManyToManyField(Sciences, blank=False, related_name="science_type")

    def __str__(self):
        return f"{self.name}"
    
    def namejs(self):
        name = self.name
        name = name.replace(" ","_")
        return f"{name}"

    def serialize(self):
        return {
            "name" : self.name,
            "science" : [science.serialize() for science in self.science.all()]
        }

class SubTopic(models.Model):
    name = models.CharField(max_length=100)
    sub_area = models.ManyToManyField(SubArea, blank=False, related_name="science_area")

    def __str__(self):
        return f"{self.name}"
    
    def namejs(self):
        name = self.name
        name = name.replace(" ","_")
        return f"{name}"
    
    def serialize(self):
        return {
            "name" : self.name,
            "sub_area" : [sub_area.serialize() for sub_area in self.sub_area.all()]
            }

class Studys(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True)
    public = models.BooleanField(blank=False, default=False)
    user_create = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    credit = models.CharField(max_length=200, blank=False, default=None)
    area = models.ManyToManyField(SubArea, blank=True, related_name="studys_area")
    topic = models.ManyToManyField(SubTopic, blank=True, related_name="studys_topic")
    content = models.TextField(blank=False)
    summary = models.CharField(max_length=1500, blank=False)
    pdf = models.ManyToManyField(Docs, blank=True, default='', max_length=1000, related_name="pdf_docs")
    teaching_audio = models.ManyToManyField(Docs, blank=True, default='', max_length=1000, related_name="audio_docs")
    create_date = models.DateField(auto_now=True, editable=False)
    rev1_date = models.DateField(default=datetime.now() + timedelta(days=1))
    rev2_date = models.DateField(default=datetime.now() + timedelta(days=7))
    rev3_date = models.DateField(default=datetime.now() + timedelta(days=30))
    rev4_date = models.DateField(default=datetime.now() + timedelta(days=60))

    def serialize(self):
        return {
            "title" : self.title,
            "public" : self.public,
            "credit" : self.credit,
            "area" : [area.name for area in self.area.all()],
            "topic" : [topic.name for topic in self.topic.all()],
            "content" : self.content,
            "summary" : self.summary,
            "pdf" : [pdf.serialize() for pdf in self.pdf.all()],
            "teaching_audio" : [teaching_audio.serialize() for teaching_audio in self.teaching_audio.all()],
            "create_date" : self.create_date,
            "rev1_date" : self.rev1_date,
            "rev2_date" : self.rev2_date,
            "rev3_date" : self.rev3_date,
            "rev4_date" : self.rev4_date,
        }
 
class Event(models.Model):
    EVENT_TYPES = [('Study','Study'),('Review','Review')]

    user_create = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    type = models.CharField(choices=EVENT_TYPES, max_length=6, default='Study')
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

#__________________COURSES__________________________________
def get_upload_path_courses(instance, filename):
    return 'courses/{0}/{1}/{2}'.format(instance.course_model, instance.title, filename)

class Courses(models.Model):
    choices_course_model = [('face-to-face', 'face-to-face'), ('distance', 'distance')]
    choices_duration = [('1 months - 2 months', '1 months - 2 months'), ('2 months - 4 months', '2 months - 4 months'), ('4 months - 8 months', '4 months - 8 months')]

    title = models.CharField(max_length=200, blank=False)
    cover_image = models.FileField(upload_to=get_upload_path_courses, blank=False, default='')
    topics = models.ManyToManyField(SubTopic, blank=False, related_name="courses_topic")
    areas = models.ManyToManyField(SubArea, blank=False, related_name="courses_area")
    rooms = models.ManyToManyField('Rooms', blank=True, related_name="course_rooms")
    lessons = models.ManyToManyField('Lessons', blank=True, related_name="course_lessons")
    hard_skills = models.ManyToManyField('HardSkills', blank=True, related_name="courses_hard_skills")
    course_model = models.CharField(choices=choices_course_model, max_length=50, blank=False, default='distance')
    duration = models.CharField(choices=choices_duration, max_length=50, blank=False, default='1 months - 2 months')
    certificate = models.ForeignKey('Certificates', on_delete=models.CASCADE, blank=True, null=True)
    instructors = models.ManyToManyField(Instructors, blank=True, related_name="courses_instructors")
    credits = models.ManyToManyField('Institutions', blank=True, related_name="courses_institutions")

    def __str__(self):
        return f"{self.title}"

    def serialize(self):
        return {
            "id" : self.id,
            "title" : self.title,
            "cover_image" : self.cover_image.url,
            "topics" : [topic.name for topic in self.topics.all()],
            "areas" : [area.name for area in self.areas.all()],
            "rooms" : [room.serialize() for room in self.rooms.all()],
            "lessons" : [lesson.title for lesson in self.lessons.all()],
            "hard_skills" : [skill.serialize() for skill in self.hard_skills.all()],
            "course_model" : self.course_model,
            "duration" : self.duration,
            "certificate" : self.certificate,
            "instructors" : [instructor.serialize() for instructor in self.instructors.all()],
            "credits" : [credit.serialize() for credit in self.credits.all()],

        }

def get_upload_path_lessons(instance, filename):
    return 'courses/{0}/{1}/lessons/{2}/{3}'.format(instance.course.course_model, instance.course.title, instance.title, filename)

class Rooms(models.Model):
    choices_days = [('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')]
    choices_duration = [('1 hour', '1 hour'), ('1:30 hour', '1:30 hour'), ('2 hours', '2 hours'), ('2:30 hours', '2:30 hours'), ('3 hours', '3 hours')]

    course = models.ForeignKey(Courses, on_delete=models.CASCADE, blank=False, related_name="rooms_course")
    max_students = models.IntegerField(blank=False)
    students = models.ManyToManyField(User, blank=True, related_name="rooms_students")
    course_days = MultiSelectField(choices=choices_days, max_choices=7, max_length=15, blank=False)
    course_schedule = models.TimeField(blank=False)
    duration = models.CharField(choices=choices_duration, blank=False, max_length=10)

    def __str__(self):
        return f"Room {self.id}"

    def serialize(self):
        return {
            "name" : f"Room + {self.id}",
            "max_students" : self.max_students,
            "students" : [student.username for student in self.students.all()],
            "course_days" : self.course_days,
            "course_schedule" : self.course_schedule,
            "duration" : self.duration
        }

class Lessons(models.Model):
    course = models.ForeignKey(Courses, blank=False, on_delete=models.CASCADE, related_name="lessons_course")
    title = models.CharField(max_length=100, blank=False)
    video = models.CharField(max_length=500, blank=False)
    audio = models.FileField(upload_to=get_upload_path_lessons, blank=False, max_length=500)
    notes = models.TextField(max_length=200000, blank=False)
    slides = models.FileField(upload_to=get_upload_path_lessons, max_length=500, blank=False)
    source_code = models.FileField(upload_to=get_upload_path_lessons, max_length=500, blank=True)
    subtitles = models.FileField(upload_to=get_upload_path_lessons, max_length=500, blank=False)
    transcript = models.TextField(max_length=150000, blank=False)
    hard_skills = models.ManyToManyField('HardSkills', blank=True, related_name='lessons_hard_skills')
    projects = models.ManyToManyField('Projects', blank=True, related_name='lesson_project', default="")

    def __str__(self):
        return f"{self.title}"
    
    def serialize(self):
        lessons = {"title" : self.title,
                "video" : self.video,
                "audio" : self.audio.url,
                "notes" : self.notes,
                "slides" : self.slides.url,
                "subtitles" : self.subtitles.url,
                "transcript" : self.transcript,
                "hard_skills" : [skill.serialize() for skill in self.hard_skills.all()],
                "projects" : [project.serialize() for project in self.projects.all()]
                }
        if self.source_code:
            lessons["source_code"] = self.source_code.url
            return lessons
        else:
            return lessons

def get_upload_path_projects(instance, filename):
    return 'courses/{0}/{1}/Projects/{2}/{3}'.format(instance.lessons.course.course_model, instance.lessons.course.title, instance.title, filename)

class Projects(models.Model):
    lessons = models.ForeignKey(Lessons, on_delete=models.CASCADE, blank=False, related_name='lesson_project')
    title = models.CharField(max_length=100, blank=False)
    cover_image = models.FileField(upload_to=get_upload_path_projects, max_length=500)
    delivery_date = models.DateTimeField(blank=True, null=True, default=datetime.now)
    start_file = models.FileField(upload_to=get_upload_path_projects, max_length=500, blank=True)
    getting_started = models.TextField(max_length=100000, blank=True, default="")
    description = models.TextField(max_length=100000, blank=True, default="")
    hints = models.TextField(max_length=100000, blank=True, default="")
    specifications = models.TextField(max_length=100000, blank=True, default="")
    how_to_send = models.TextField(max_length=100000, blank=True, default="")

    def __str__(self):
        return f"{self.title}"
    
    def serialize(self):
        projects = {
            "title" : self.title,
            "cover_image" : self.cover_image.url,
            "delivery_date" : self.delivery_date,
            "getting_started" : self.getting_started,
            "description" : self.description,
            "hints" : self.hints,
            "specifications" : self.specifications,
            "how_to_send" : self.how_to_send,
        }
        if self.start_file:
            projects["start_file"] = self.start_file.url
            return projects
        else:
            return projects

def get_upload_path_hardskills(instance, filename):
    return 'hard_skills/{0}/{1}'.format(instance.name, filename)

class HardSkills(models.Model):
    name = models.CharField(max_length=200, blank=False)
    icon = models.FileField(upload_to=get_upload_path_hardskills)

    def __str__(self):
        return f"{self.name}"

    def serialize(self):
        return {
            "name" : self.name,
            "icon" : self.icon.url,
        }

def get_upload_path_softkills(instance, filename):
    return 'soft_skills/{0}/{1}'.format(instance.name, filename)

class SoftSkills(models.Model):
    name = models.CharField(max_length=200, blank=False)
    icon = models.FileField(upload_to=get_upload_path_softkills)

def get_upload_path_certifications(instance, filename):
    return 'institutions/{0}/{1}/{2}/{3}'.format(instance.institutions.name, instance.course, 'certificate', filename)

class Certificates(models.Model):
    choices_nivel = [('basic', 'basic'), ('Intermediary', 'Intermediary'), ('Advanced', 'Advanced')]

    name = models.CharField(max_length=200, blank=False)
    institutions = models.ManyToManyField('Institutions', blank=False, related_name="certificate_institution")
    course = models.ForeignKey(Courses, default='', blank=False, on_delete=models.CASCADE, related_name="certificate_course")
    icon = models.FileField(upload_to=get_upload_path_certifications)
    nivel = models.CharField(choices=choices_nivel, max_length=50, blank=False)

def get_upload_path_institutions(instance, filename):
    return 'institutions/{0}/{1}/{2}'.format(instance.name, 'logo', filename)

class Institutions(models.Model):
    name = models.CharField(max_length=200, blank=False)
    logo = models.FileField(upload_to=get_upload_path_institutions, blank=False)
    courses = models.ManyToManyField(Courses, blank=True, related_name="institution_courses")

    def __str__(self):
        return f"{self.name}"
    
    def serialize(self):
        return {
            "name" : self.name,
            "logo" : self.logo.url,
            "courses" : [course.name for course in self.courses.all()],
        }
