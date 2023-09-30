from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = "homepage"),
    path('show_book/',views.showBook, name = "showbook"),
    path('store_book/',views.storeBook, name = "storebook"),
    path('registration/',views.registrationForm , name = "registrationform"),
    path('login/',views.logIn, name = 'loginpage'),
    path('logout/',views.userLogout, name = "logoutpage"),
    path('borrow_book/<int:isbn_number>',views.borrowBook, name = "borrowbook"),
    path('profile/',views.profile,name = "profile"),

]
