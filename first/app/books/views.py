from django_filters.views import FilterView
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from django.urls import reverse_lazy
from app.books.models import Books, Author
from app.books.forms import BookForm, BooksAddNewForm
from app.books.filters import BooksFilter



class BookList(FilterView):

    model = Books
    filterset_class = BooksFilter
    context_object_name = 'books'
    template_name = 'books/books_list.html'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['books'] = self.queryset
        context['title'] = 'Городская библиотека'
        return context


def add_books(request):

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            book_name = form.cleaned_data['book_name']
            # authors = form.cleaned_data['authors']
            Books.objects.create(book_name=book_name)
            # form.save()

    form = BookForm()

    context = {
        'form': form,
    }

    return render(request, 'books/add_books.html', context=context)


class BooksDetail(DetailView):

    model = Books
    # template_name = 'books_detail.html'
    pk_url_kwarg = 'pk'


class CreateBooksView(CreateView):
    model = Books
    form_class = BooksAddNewForm
    template_name = 'books/books_add_new.html'
    success_url = reverse_lazy('main')
