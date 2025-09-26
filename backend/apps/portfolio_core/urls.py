from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("about/", views.about_me, name='about'),
    path("projects/", views.projects, name='projects'),
    path("contactform/", views.contact_form, name="contact"),
    path("socialmedia/", views.social_media, name="social")
]
