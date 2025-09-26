from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about_me(request):
    return render(request, 'about-me.html')

def projects(request):
    return render(request, 'projects.html')

def contact_form(request):
    return render(request, 'contactform.html')

def social_media(request):
    return render(request, 'social-media.html')