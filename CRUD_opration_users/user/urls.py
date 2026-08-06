from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="user_list"),
    # path('alluser/',views.alluser),
    path('singleuser/<int:id>',views.singleuser, name="singleuser"),
    path('adduser/',views.adduser),
    path('deleteuser/<int:id>',views.deleteuser),
    path('updateuser/<int:id>',views.updateuser),
]