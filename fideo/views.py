from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request=request, template_name="index.html")

def about_us_view(request):
    return render(request=request , template_name="aboutUs.html")

def fideo_view(request):
    return render(request=request , template_name="fideo.html")

def impressum_view(request):
    return render(request=request , template_name="impressum.html")

def login_view(request):
    return render(request=request , template_name="login.html")
