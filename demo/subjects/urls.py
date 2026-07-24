from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.subadd),
    path('update/',views.subupdate),
]
