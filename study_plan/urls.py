from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_study/<int:type>/<str:topic_selected>", views.create_study, name="create_study"),
    path("content", views.content, name="content"),

    #Api routes
    path("get_content_items/<str:type>/<str:name>/<str:content_name>/<str:is_review>", views.get_content_items, name="get_content_items"),
    path("get_subareas/<str:science>", views.get_subareas, name="get_subareas"),
    path("get_subtopics/<str:subarea>", views.get_subtopics, name="get_subtopics"),
    path("uadoajsersalladaqeqe/<str:username_input>", views.verifi_username, name="verifi_username"),
    path("asdajdawqeqweomemail/<str:email_input>", views.verifi_email, name="verifi_email"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)