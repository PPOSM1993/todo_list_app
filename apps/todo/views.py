from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout



# Create your views here.


def SignUp(request):
    if request.method =="POST":
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('email')
        pwd = request.POST.get('pwd')
        print(fnm, emailid, pwd)

        my_user = User.objects.create_user(fnm, emailid, pwd)

        my_user.save()

        return redirect('/login')


    return render(request, 'sign_up.html')


def Login(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')



        user = authenticate(request, username=fnm, password=pwd)

        if user is not None:
            login(request, user)
            return redirect('/todo_page')
        else:
            return redirect('/login')

        print(pwd, fnm)
    return render(request, 'login.html')


def ToDo(request):
    return render(request, 'todo_page.html')