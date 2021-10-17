from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    bio = models.CharField(max_length =200)
    profile_pic = CloudinaryField('image')
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    followers = models.ManyToManyField('Profile',related_name="profile_followers",blank=True,default=0)
    following = models.ManyToManyField('Profile',related_name="profile_following",blank=True,default=0)
    def __str__(self):
        return self.user