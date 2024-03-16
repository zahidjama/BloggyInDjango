from django.shortcuts import render, redirect
from .models import customUser
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import AuthForm
# Create your views here.


@login_required(login_url="login")
def home(request):
    return render(request, "home.html")

@login_required(login_url="login")
def logoutUser(request):
    logout(request)
    return redirect("index")


def index(request):
    if request.user.is_authenticated:
        return redirect("home")
    return render(request, "index.html")


def loginFunc(request):
    if request.user.is_authenticated:
        return redirect("home")
    form=AuthForm()
    if request.method=='POST':
        email=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
    return render(request, "login.html", {'form':form})

def signinFunc(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        user=customUser(full_name=name, email=email, phone=phone)
        user.set_password(password)
        user.save()
        login(request, user)
        return redirect("home")

    return render(request, "signin.html")
