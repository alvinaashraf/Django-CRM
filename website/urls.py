
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('logout/',views.logout_user,name="logout"),
    path('register/',views.register_user,name="register"),
    path('add_record/',views.add_record,name="add_record"),

    path('record_detail/<int:pk>',views.record_detail,name="record_detail"),
        path('update_record/<int:pk>',views.update_record,name="update_record"),

    path('record_delete/<int:pk>',views.record_delete,name='record_delete')

   
]
