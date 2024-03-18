from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from . import models
from django import forms
from django.forms import EmailInput
from ckeditor.widgets import CKEditorWidget
class AuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget=EmailInput({"type": "email"})

class postUploadForm(forms.ModelForm):
    post = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model=models.posts
        fields=['title', 'post', 'postImage']
    