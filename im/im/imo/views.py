from django.shortcuts import render,redirect
from .models import Post,Profile
from django.contrib.auth.models import User, auth

# Create your views here.
def main(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile=Profile.objects.get(user=user_object)
    posts = Post.objects.all()
    return render(request,'indexo.html',{'posts':posts,"user_profile":user_profile})

def upload(request):
    if request.method == 'POST':
        user= request.user.username
        image=request.FILES.get('image_upload')
        caption=request.POST['caption']
        new_post=Post.objects.create(user=user,caption=caption,image=image)
        new_post.save()
        return redirect("main")
    return render(request,'upload.html')