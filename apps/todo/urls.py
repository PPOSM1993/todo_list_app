from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
    path('login/', views.Login, name='login'),
    path('todo_page/', views.ToDo, name='todo_page'),
    path('update_todo/<int:srno>', views.UpdateTodo, name='update_todo'),
    path('delete_todo/<int:srno>', views.DeleteTodo, name='delete_todo'),
    path('logout/', views.Logout, name='logout'),
]
