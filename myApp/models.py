from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import customUserManager
# Create your models here.

class customUser(AbstractBaseUser):
    full_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100, unique=True)
    phone=models.IntegerField()
    address=models.CharField(max_length=500, default="No Address")
    bio=models.CharField(max_length=500, default="No Bio")
    profileImage=models.ImageField(upload_to="media/profiles/", default="static/images/profile.jpg")
    coverImage=models.ImageField(upload_to="media/cover/", default="static/images/cover.jpg")
    total_likes=models.IntegerField(default=0)
    
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    object=customUserManager()
    REQUIRED_FIELDS=['full_name', 'phone']

    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, perms):
        return True

    



