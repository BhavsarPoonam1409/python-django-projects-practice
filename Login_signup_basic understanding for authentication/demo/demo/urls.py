
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('services/', views.services),
    path('students/', include('student.urls') ),
    path('fuculties/', include('faculties.urls') ),
    path('products/', include('myprod.urls') ),
    path('users/', include('users.urls')),

]
