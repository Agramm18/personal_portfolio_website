from django.shortcuts import render

def contact_form_view(request):
    print("Hello World")  # nur zum Debug
    return render(request, "contactform.html")
