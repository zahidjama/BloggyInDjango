from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("login", views.loginFunc, name="login"),
    path("signin", views.signinFunc, name="signin"),
    path("home", views.home, name="home"),
    path("logout", views.logoutUser, name="logout"),
    path("createPost", views.createPost, name="createPost"),
    path("read/<slug:id>", views.Read, name="read"),
    path("like", views.addLike, name="like")
]