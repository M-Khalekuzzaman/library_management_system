from django.db import models

# Create your models here.

class BookStoreModel(models.Model):
    CATEGORY = (
        ('Harry-Poter','Harry-Poter'),
        ('Drama','Drama'),
        ('Sci-Fi','Sci-Fi'),
        ('Horror','Horror'),
    )
    isbn_number = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    genre = models.CharField(max_length=30,choices=CATEGORY)
    availability = models.IntegerField()
    first_pub = models.DateTimeField(auto_now_add=True)
    last_pub =  models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"ISBN : {self.isbn_number} - BOOK_NAME : {self.title}"
    
class BookBorrowModel(models.Model):
    CATEGORY = (
        ('Harry-Poter','Harry-Poter'),
        ('Drama','Drama'),
        ('Sci-Fi','Sci-Fi'),
        ('Horror','Horror'),
    )
    isbn_number = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    genre = models.CharField(max_length=30,choices=CATEGORY)
    availability = models.IntegerField()
    first_pub = models.DateTimeField(auto_now_add=True)
    last_pub =  models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"ISBN : {self.isbn_number} - BOOK_NAME : {self.title}"
