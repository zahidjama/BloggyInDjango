from django.shortcuts import render, redirect
from .models import customUser, posts
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import AuthForm, postUploadForm
# Create your views here.


@login_required(login_url="login")
def home(request):
    obj=posts.objects.all()
    return render(request, "home.html", {'posts':obj})

@login_required(login_url="login")
def Read(request):
    slug=request.GET.get("id")
    obj=posts.objects.get(slug=slug)

    return render(request, 'read.html', {'post':obj})

@login_required(login_url="login")
def logoutUser(request):
    logout(request)
    return redirect("index")


@login_required(login_url="login")
def createPost(request):
    form=postUploadForm(request.POST, request.FILES)
    if form.is_valid():
        title=form.cleaned_data['title']
        post=form.cleaned_data['post']
        image=form.cleaned_data['postImage']
        obj=posts(title=title, post=post, postImage=image)
        obj.user=request.user
        obj.save()
    return render(request, "createPost.html", {'form':form})



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
