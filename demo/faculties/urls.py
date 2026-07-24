from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.fachome),
    path('add/',views.facadd),
]