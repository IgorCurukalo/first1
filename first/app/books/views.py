from django_filters.views import FilterView
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse_lazy
from app.books.models import Books, Author
from app.books.forms import BookForm
from app.books.filters import BooksFilter


class BookList(FilterView):

    model = Books
    filterset_class = BooksFilter
    context_object_name = 'books'
    template_name = 'books/books_list.html'
    paginate_by = settings.OBJECTS_ON_PAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.queryset
        context['title'] = 'Городская библиотека'
        return context


class BooksDetail(DetailView):
    model = Books
    pk_url_kwarg = 'pk'


class CreateBooksView(CreateView):
    model = Books
    form_class = BookForm
    template_name = 'books/books_add_new.html'
    success_url = reverse_lazy('main')
