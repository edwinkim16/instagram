from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.fields import related

# Create your models here.

class Profile(models.Model):
    bio = models.CharField(max_length =200)
    profile_pic = CloudinaryField('image')
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    followers = models.ManyToManyField('Profile',related_name="profile_followers",blank=True,default=0)
    following = models.ManyToManyField('Profile',related_name="profile_following",blank=True,default=0)
    
    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()
    @classmethod
    def search_profile(cls,search_term):
        profiles = cls.objects.filter(user__icontains=search_term)
        return profiles    

class Image(models.Model):
    image = CloudinaryField('image')
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE,related_name="user_name")
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    image_name = models.CharField(max_length =30)
    caption = models.CharField(max_length =50)
    post_date = models.DateTimeField(auto_now_add=True)
    
     
    def __str__(self):
        return self.image_name        

class Comment(models.Model):
    image = models.ForeignKey('Image',on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment        

class Like(models.Model):
    post = models.ForeignKey('Image',on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        unique_together = ("post", "user")

    def __str__(self):
        return 'Like: ' + self.user.username

class Followers(models.Model):
    user = models.CharField(max_length=15)
    follower = models.CharField(max_length=15)
    following = models.CharField(max_length=15)                 