from django.urls import path
from .views import *

urlpatterns = [
    # path('hello/<str:name>/', home)
    # path('hello/', HomeView.as_view())
    path('books/', books_list, name='books-list'),
    path('book/<int:pk>/', book_detail, name='book-detail'),
    path('book/create/', book_create, name='book-create'),
]