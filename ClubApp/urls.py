from django.urls import path
from ClubApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('programs/', views.programs, name='programs'),
    path('community/', views.community, name='community'),
    path('resources/', views.resources, name='resources'),
]