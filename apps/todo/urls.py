from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
    path('login/', views.Login, name='login'),
    path('todo_page', views.ToDo, name='todo_page')
]
