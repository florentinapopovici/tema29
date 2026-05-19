from django.urls import path 
from mainapp import views

urlpatterns = [
    path('', views.homepage , name='homepage'),
    path("contact" , views.contact , name='contact'),
    path("exercitiu" , views.exercitiu , name='exercitiu'),
    path("add" , views.add_movie , name='add'),
    path("movie/<int:pk>" , views.details , name='details'),
    path("book/<int:pk>" , views.book_detail , name = 'book'),
    path("add-books", views.book, name="add_books")
]