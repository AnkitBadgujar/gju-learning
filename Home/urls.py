from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
    path('photoshoot',views.photoshoot,name='photoshoot'),
    path('wedding',views.wedding,name='wedding'),
    path('pre_wedding',views.pre_wedding,name='pre_wedding')
]
