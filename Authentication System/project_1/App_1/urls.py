from django.contrib import admin
from django.urls import path
from App_1 import views


urlpatterns = [
    path("",views.index,name="home"),
    path("index",views.index,name="home"),
    path("signup",views.index,name="home"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact")
]
