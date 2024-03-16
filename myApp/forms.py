from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from .models import customUser
from django.forms import EmailInput
class AuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget=EmailInput({"type": "email"})