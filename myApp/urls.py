from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("login", views.loginFunc, name="login"),
    path("signin", views.signinFunc, name="signin"),
]