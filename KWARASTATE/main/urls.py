from django.urls import path
from . import views



urlpatterns = [
    path('', views.index,name="index"),
    path('about/', views.about,name="about"),
    path('contact/', views.contact,name="contact"),
    path('government/', views.government,name="government"),
    path('project/', views.project,name="project"),
     path('investment/', views.investment,name="investment"),
      path('tourism/', views.project,name="tourism"),
    path('ministries/', views.ministries,name="ministries"),
    path('services/', views.services,name="services"),
    path('news/', views.news,name="news"),
]
