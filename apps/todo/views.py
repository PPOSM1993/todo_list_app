from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from apps.todo import models

from .models import Todo
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def SignUp(request):
    if request.method =="POST":
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('email')
        pwd = request.POST.get('pwd')

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

    return render(request, 'login.html')

@login_required(login_url='/login')
def ToDo(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        obj=models.Todo(title=title,user=request.user)
        obj.save()
        user=request.user        
        res=models.Todo.objects.filter(user=user).order_by('-date')
        return redirect('/todo_page',{'res':res})
        
    
    res=models.Todo.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo_page.html',{'res':res,})

@login_required(login_url='/login')
def UpdateTodo(request, srno):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = models.Todo.objects.get(srno=srno)
        obj.title = title
        obj.save()
        return redirect('/todo_page')

    obj = models.Todo.objects.get(srno=srno)
    return render(request, 'update_todo.html', {'obj': obj})


def DeleteTodo(request, srno):
    print(srno)
    obj=models.Todo.objects.get(srno=srno)
    obj.delete()
    return redirect('/todo_page')


def Logout(request):
    logout(request)
    return redirect('/login')