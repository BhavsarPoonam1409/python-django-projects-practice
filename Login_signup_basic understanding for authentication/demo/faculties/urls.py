from django.urls import path
from . import views

urlpatterns = [
    path('', views.fachome),
    path('add/', views.facdata), 
    path('update/<int:id>', views.updatefac),
    path('delete/<int:id>', views.deletefac),
   
]
