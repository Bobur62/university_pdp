from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

from .models import Book
from .forms import BookForm


# *********************************************************************

# def home(request):  #name
#     name = request.GET.get('name', 'World')
#     # return HttpResponse(f"Hello {name}")
#     return render(request, 'library/home.html', {'name': name})


# class HomeView(View):
#     def get(self, request):
#         name = request.GET.get('name', 'World')
#         return render(request, 'library/home.html', {'name': name})
# 
#     def post(self, request):
#         pass

# *********************************************************************

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)

    return render(request, 'library/book.html', {'book': book})


def books_list(request):
    search = request.GET.get("search")

    if search is None:
        books = Book.objects.all()
    else:
        books = Book.objects.filter(title__contains=search)

    # books = Book.objects.all()
    return render(
        request, 'library/books.html', {'books': books, 'search': search}
    )


def book_create(request):
    if request.method == 'GET':
        form = BookForm
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            book = Book.objects.create(
                title=data['title'],
                author=data['author'],
                count=data['count'],
            )
            return redirect('books-list')
    return render(request, 'library/book_create.html', {'form': form})
