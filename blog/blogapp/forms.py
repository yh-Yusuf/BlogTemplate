from django.db import models
from django import forms
from .models import *

# Create your models here.


class post_form(forms.ModelForm):
    class Meta:
        model = post
        fields = "__all__"

