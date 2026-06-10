from django.urls import path
from . import views



urlpatterns = [
    path('', views.index,name="index"),
    path('about/', views.about,name="about"),
    path('contact/', views.contact,name="contact"),
    path('elements/', views.elements,name="elements"),
    path('state/', views.state,name="state"),
    path('post/', views.post,name="post"),
    path('services/', views.services,name="services"),
    path('single-post/', views.singlePost,name="singlePost"),
]
