from django.urls import path 
from mainapp import views

urlpatterns = [
    path('', views.homepage , name='homepage'),
    path("contact" , views.contact , name='contact'),
    path("exercitiu" , views.exercitiu , name='exercitiu'),
]