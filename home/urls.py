from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.firstpage, name="first"),
    path('home', views.index, name="home"),
    path('home/', views.index, name="home"),
    path('about', views.about, name="about"),
    path('resume', views.resume, name="resume"),
    path('resume-main', views.resume_main, name="resume-main"),
    path('resume-main1', views.resume_main1, name="resume-main1"),
    path('jobs', views.jobs, name="jobs"),
    path('contact', views.contact, name="contact"),
    path('submitform/', views.submitform, name="submitform"),
    path('logoutUser/', views.logoutUser, name="logoutUser"),
    path('resources', views.resources, name="resources"),
    path('resources/questions', views.questions, name="questions"),
    path('resources/mockinterview', views.mock, name="mockinterview"),
    path('resources/handbooks', views.handbooks, name="handbooks"),
    path('react', views.react, name="react"),
    path('country/', views.country, name="country"),
    path('category/', views.category, name="category"),
]