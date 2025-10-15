from django.shortcuts import render
from apps.contactform.views import contact_form_view

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about_me(request):
    return render(request, 'about-me.html')

def projects(request):
    return render(request, 'projects.html')

def social_media(request):
    return render(request, 'social-media.html')

def legal_information(request):
    return render(request, 'legal-rights.html')

def imprint(request):
    return render(request, "imprint.html")

def website_info(request):
    return render(request, "about-this-website.html")