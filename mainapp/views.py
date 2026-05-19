from django.shortcuts import render , redirect
from django.http import HttpResponse
from datetime import datetime
from mainapp.models import Movie
from mainapp.models import Book

def homepage(request):
    books = Book.objects.all()
    books_filtered = Book.objects.filter(pages__gt=100)
    
    movies = Movie.objects.all()
    user = 'Florentina'
    return render(request , 
                  'mainapp/home.html' , 
                  {
                    "books" : books ,
                    "books_filtered" : books_filtered ,
                    "filme" : movies ,
                    "user" : user ,
                    "current_date" : datetime.now() ,
                  }
                )

def details(request , pk):
    movie = Movie.objects.get(id=pk)
    return render(request , "mainapp/detail.html" , {"movie" : movie})

def contact(request):
    return render(request , "mainapp/contacts.html")

def exercitiu(request):
    return render(request , "mainapp/exercitiu.html" , 
                  {
                      "nume" : "Florentina" ,
                      "animale_de_companie" : 4 ,
                  },
                )

def add_movie(request):
    Movie.objects.create(
        title = "Sunset limited" ,
        description = "description " ,
        release_date = datetime(2007 , 12 , 1)
    )
    Movie.objects.create(
        title = "Star Wars" ,
        description = "description " ,
        release_date = datetime(1985 , 12 , 1)
    )
    Movie.objects.create(
        title = "Scooby Doo (The movie)" ,
        description = "description " ,
        release_date = datetime(2005 , 12 , 1)
    )

    return redirect("homepage")

def book(request):
    Book.objects.create(
        title = "Ion" ,
        author = "Liviu Rebreanu" ,
        pages = 500 ,
    )
    Book.objects.create(
        title = "Moara cu noroc" ,
        author = "Ioan Slavici" ,
        pages = 320 ,
    )
    Book.objects.create(
        title = "Enigma Otiliei" ,
        author = "George Călinescu" ,
        pages = 500 ,
    )

    return redirect("homepage")

def book_detail(request , pk):
    book = Book.objects.get(id=pk)
    return render(request , "mainapp/book.html" , {"book" : book})