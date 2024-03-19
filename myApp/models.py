from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import customUserManager
from autoslug import AutoSlugField
from tinymce.models import HTMLField
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

    



class posts(models.Model):
    title=models.CharField(max_length=100)
    post=HTMLField()
    postImage=models.ImageField(upload_to="media/posts/", default="static/posts/post.jpg")
    user=models.ForeignKey(customUser, on_delete=models.CASCADE, related_name="uploader")
    upload_time=models.DateTimeField(auto_now_add=True)
    likes=models.ManyToManyField(customUser, related_name="likes")
    slug=AutoSlugField(populate_from='title', default='')
    def __str__(self) -> str:
        return self.title
    

class comments(models.Model):
    id=models.AutoField(primary_key=True)
    # commentId=models.AutoField(default=0, related_name="Id")
    user=models.ForeignKey(customUser, on_delete=models.CASCADE)
    post=models.ForeignKey(posts, on_delete=models.CASCADE)
    comment=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    def __str__(self) -> str:
        return f"{self.user.full_name} , {self.post.title}"


