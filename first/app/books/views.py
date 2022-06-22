from django.shortcuts import render
from django.http import HttpResponse
from .models import Books

def get_books_list(request):
    book = Books.objects.get(pk=1)
    return HttpResponse(f'<h1>{book.book_name}</h1>')

