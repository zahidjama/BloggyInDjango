from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def loginFunc(request):
    return render(request, "login.html")

def signinFunc(request):
    return render(request, "signin.html")