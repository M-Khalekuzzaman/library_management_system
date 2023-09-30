from django.shortcuts import render,redirect
from first_app.forms import BookStoreForm,BookBorrowForm
from first_app.models import BookStoreModel,BookBorrowModel
from . forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from rest_framework import viewsets
from . import models,serializers
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

def home(request):
    return render(request,"./first_app/home.html")


def storeBook(request):
    if request.method == 'POST':
        book = BookStoreForm(request.POST)
        if book.is_valid():
            book.save(commit=True)
            
    else:
        book = BookStoreForm()
    return render(request,"./first_app/store_book.html",{'form': book})


def showBook(request):
    book = BookStoreModel.objects.all()
    return render(request,"./first_app/show_book.html",{'data':book})
    
def registrationForm(request):
    if request.method == 'POST':
      form = RegisterForm(request.POST)
      if form.is_valid():
        form.save()
        messages.success(request,'<h4>Successfully created !</h4>')
    else:
        form = RegisterForm()
    return render(request,"./first_app/registration.html",{'form':form})
  
  
  
def logIn(request):
  if request.method == 'POST':
    form = AuthenticationForm(request=request,data = request.POST)
    if form.is_valid():
      name = form.cleaned_data['username']
      userpass = form.cleaned_data['password']
      user = authenticate(username = name,password = userpass)
      if user is not None:
        login(request,user)
        return redirect('showbook')
  else:
    form = AuthenticationForm()
    return render(request,'./first_app/login.html',{'form':form})

def userLogout(request):
  logout(request)
  return redirect('homepage')


def borrowBook(request,isbn_number):
    book = BookStoreModel.objects.get(pk = isbn_number)
    form = BookBorrowForm(instance = book)
    if request.method == 'POST':
        form = BookBorrowForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile')
    else:
        form = BookBorrowForm()    
    return render(request,"./first_app/borrow_book.html",{'form':form})


def profile(request):
    book = BookBorrowModel.objects.all()
    return render(request,"./first_app/profile.html",{'data':book})
