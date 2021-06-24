from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.conf import settings
import pymongo

# Create your views here.

def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    else:
        return render(request,'login.html')
def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if len(first_name)<1:
            messages.info(request, "Enter first name")
        if len(last_name)<1:
            messages.info(request, "Enter last name")
        if len(username)<1:
            messages.info(request, "Enter username")
        if len(password1)<1 or len(password2)<1:
            messages.info(request, "Enter Password")
        if (len(password1)>1 and len(password2)>1) and password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("user created")
                return redirect('login')
        else:
            messages.info(request,"Password don't match")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')