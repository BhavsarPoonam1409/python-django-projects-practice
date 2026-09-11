from django.urls import path
from . import views

urlpatterns = [
    path('', views.stuhome),
    path('edit/', views.stuedit),
]
