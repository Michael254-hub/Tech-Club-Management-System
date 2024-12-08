from django.urls import path
from ClubApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('programs/', views.programs, name='programs'),
    path('resources/', views.resources, name='resources'),
    path('events/', views.events, name='events'),
    path('blog/', views.blog, name='blog'),
    path('community/', views.community, name='community'),
    path('contact/', views.contacts, name='contacts'),
    path('logout', views.logout, name='logout'),
]