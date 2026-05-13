from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def homepage(request):
    movies = ['Sunset limited' , 'Star Wars' , 'Lord of the rings']
    user = 'Florentina'
    return render(request , 
                  'mainapp/home.html' , 
                  {
                    "filme" : movies ,
                    "user" : user ,
                    "current_date" : datetime.now() ,
                   },
                )

def contact(request):
    return render(request , "mainapp/contacts.html")

def exercitiu(request):
    return render(request , "mainapp/exercitiu.html" , 
                  {
                      "nume" : "Florentina" ,
                      "animale_de_companie" : 4 ,
                  },
                )
