from django.urls import path
from . import views

urlpatterns = [
    path('', views.allusers, name="users_list"),
    path('add/', views.adduser),
    path('delete/<int:id>', views.deleteUser),
    path('update/<int:id>', views.updateUser),
    path('singleuser/<int:id>', views.singleUser, name="singleuser"),


]
