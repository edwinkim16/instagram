from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Image,Profile,Like,Followers,Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm,PostImage,CommentForm,UpdateImage
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to Instagram')

def home(request):
    images = Image.objects.all().order_by('-post_date')
    users = User.objects.all()  
    current = request.user
    likes = Like.objects.all().count()
    
    return render(request, 'index.html',{"images":images,'users':users,'current':current,"likes":likes})   

@login_required(login_url='/accounts/login/')
def profile(request,id):
    current_user = request.user
    user = User.objects.get(id=id)
    if current_user.id == user.id:
        images = Image.objects.filter(owner_id=id)
        current_user = request.user
        user = User.objects.get(id=id)
        try:
            profile = Profile.objects.get(user_id=id)
        except ObjectDoesNotExist:
            return redirect(update_profile,current_user.id)
    else: 
        try:
            profile = Profile.objects.get(user_id=id)
        except ObjectDoesNotExist:
            
            return redirect(no_profile,id)      
            
    return render(request,'profile/profile.html',{'user':user,'profile':profile,'images':images,'current_user':current_user})   

@login_required(login_url='/accounts/login/')
def update_profile(request,id):
    
    current_user = request.user
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_id=id
            profile.save()
            return redirect(home)
    else:
        form = UpdateProfileForm()
    return render(request,'profile/update_profile.html',{'user':user,'form':form})      

def no_profile(request,id):
    
    user = User.objects.get(id=id)
    return render(request,'profile/no_profile.html',{"user":user})    