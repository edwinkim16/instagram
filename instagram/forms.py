from django import forms
from .models import Profile,Image,Comment,Like
from django.contrib.auth.models import User

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['followers','following','user']

class PostImage(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['owner','post_date','profile']