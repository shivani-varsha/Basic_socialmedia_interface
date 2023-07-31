from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from imo.models import Post, Profile
# Create your views here.
def coder(request):
    return render(request,'frontend 1.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            user_object = User.objects.get(username=request.user.username)
            user_profile=Profile.objects.get(user=user_object)
            posts = Post.objects.all()

            return render(request,'indexo.html',{'user_profile':user_profile})

        else:
            messages.info(request,"not registered")
            return redirect('newo:login')

    else:
        return render(request,'login site.html')   
def sign(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass1']
        cpassword = request.POST['pass2']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken:choose other one')
                return redirect('newo:sign')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                user_login = auth.authenticate(username=username,password=password)
                auth.login(request,user_login)
                user_model = User.objects.get(username=username)
                new_profile =Profile.objects.create(user=user_model,id_user =user_model.id)
                new_profile.save()
                messages.info(request,"Account created")
                return redirect('newo:settings')
        else:
            messages.info(request,"please correct you pswd")
            return redirect('newo:sign')
    else:
        return render(request,'sign in.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def settings(request):
    user_profile=Profile.objects.get(user=request.user)
    if request.method == "POST" :
        if request.FILES.get('image') ==None:
            image = user_profile.profimg
            bio =request.POST['bio']
            location = request.POST['location']

            user_profile.profimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        if request.FILES.get('image') !=None:
            pimage = request.FILES.get('image')
            bio =request.POST['bio']
            location = request.POST['location']

            user_profile.profimg = pimage
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        return redirect("newo:settings")
    return render(request,'sett.html',{'user_profile': user_profile})

