
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('add/',views.addbook),
    path('delete/<int:id>',views.deletebook),
    path('update/<int:id>',views.updatebook),
 ]