from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Menu

def index(request):
    return render(request,"index.html") 

def login(request):
    return render(request,"login.html")

def menu(request):
    menu1=Menu()
    menu1.name = 'Paneer Tikka'

    return render(request,"menu.html",{'menu1' :menu1})

def about(request):
    return render(request,"about.html")

def signup(request):
    if request.method == 'POST':
        FullName = request.POST['FullName']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Exists')
        elif User.objects.filter(email=email).exists():
            message.info(request,'Email Already Exists')
        else:    
            user=User.objects.create_user(FullName=FullName,email=email,username=username,password=password)
            user.save();
            messages.info(request,'User Created')
            return redirect('/')
    else:
        return render(request,"signup.html")

