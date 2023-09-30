from django import forms 
from . models import BookStoreModel,BookBorrowModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BookStoreForm(forms.ModelForm):
    class Meta:
        model = BookStoreModel
        fields = '__all__'
        labels = {
            'isbn_number' : 'ISBN',
            'title' : 'Book_Name',
            'author' : 'Author_name',
            'genre' : 'Genre',
            'availability' : 'Available',
            'first_pub' : 'First_Publis',
            'last_pub' : 'Last_Publis'
        }
        
        help_texts = {
            'isbn_number' : 'Enter book  ISBN number',
            'title' : 'Enter describe a book title',
            'author' : 'Enter author name',
            'genre' : 'Select a genre name',
            'availability' : 'Select a available books',
            'first_pub' : 'Enter first publication',
            'last_pub' : 'Enter last publication'
            
        }
        
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {
            'username' : "User_name",
            'first_name' : "First_name",
            'last_name' : "Last_name",
            'email': "Email",
            'password' : "Password",
            'confirm_password' : "Confirm_Password"
        }
        help_texts = {
            'user_name' : "Enter your valid user name",
            'first_name' : "Enter your first name",
            'last_name' : "Enter your last name",
            'email' : "Enter your valid email address",
            'password' : 'Password must be contain at least 8 character'
        }
             
class BookBorrowForm(forms.ModelForm):
    class Meta:
        model = BookBorrowModel
        fields = '__all__'
        labels = {
            'isbn_number' : 'ISBN',
            'title' : 'Book_Name',
            'author' : 'Author_name',
            'genre' : 'Genre',
            'availability' : 'Available',
            'first_pub' : 'First_Publis',
            'last_pub' : 'Last_Publis'
        }
        
        help_texts = {
            'isbn_number' : 'Enter book  ISBN number',
            'title' : 'Enter describe a book title',
            'author' : 'Enter author name',
            'genre' : 'Select a genre name',
            'availability' : 'Available must be less then 3',
            'first_pub' : 'Enter first publication',
            'last_pub' : 'Enter last publication'
            
        }
