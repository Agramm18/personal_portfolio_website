from django.urls import path
from . import views
from apps.contactform.views import contact_form_view

urlpatterns = [
    path("home/", views.home, name="home"),
    path("about/", views.about_me, name='about'),
    path("projects/", views.projects, name='projects'),
    path("contactform/", contact_form_view, name="contactform"), 
    path("socialmedia/", views.social_media, name="socialmedia"),
    path("legal/", views.legal_information, name="legal"),
    path("imprint/", views.imprint, name="imprint"),
    path("about_this_website/", views.website_info, name="website_info")
]
