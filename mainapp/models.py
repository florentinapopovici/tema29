from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    release_date = models.DateTimeField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "movie"

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    full_name = models.CharField(max_length=150)

    class Meta:
        db_table = "user"


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    pages = models.PositiveIntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "book"