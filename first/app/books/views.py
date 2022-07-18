from django_filters.views import FilterView
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from app.books.models import Books, Author
from app.books.forms import BookForm
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


# def get_book(request):
#
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#
#         if form.is_valid():
#             book_name = form.cleaned_data['book_name']
#             authors = form.cleaned_data['authors']
#
#     form = BookForm()
#
#     filter = BooksFilter(request.GET, queryset=Books.objects.all())
#
#     context = {
#         'filter': filter,
#         'form': form,
#     }
#
#     return render(request, 'books/books_list.html', context=context)


class BooksDetail(DetailView):

    model = Books
    # template_name = 'books_detail.html'
    pk_url_kwarg = 'pk'
