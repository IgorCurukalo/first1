from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Books, Author


class BooksList(ListView):

    model = Books
    # template_name = 'books_list.html'
    # queryset = Books.objects.all()
    context_object_name = 'books'

    # print('hello')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['books'] = self.queryset
    #     return context

class BooksDetail(DetailView):

    model = Books
    # template_name = 'books_detail.html'
    pk_url_kwarg = 'pk'


# def get_book(request, id_book):
#
#     books = Books.objects.get(pk=id_book)
#
#     return books



# 4/7/2022
    # def get_book(request, id_book):
    #     books = Books.objects.get(pk=id_book)
    #
    #     return books
    #
    #     def get_books_list(request):
    #         book = Books.objects.all()
    #
    #         context = {
    #             'books': book,
    #             'sale': True,
    #         }
    #
    #         return render(request, 'books/index.html', context)
    #
    #     def get_book(request, id_book):
    #         books = Books.objects.get(pk=id_book)
    #
    #         return books




    # book = Books.objects.all().first()
    # book = Books.objects.get(id_publishing_house__publishing_house_name='Утро')
    # return HttpResponse(f'<h1>{book.book_name}</h1>')
    # {book.id_publishing_house.publishing_house_name}
    # print(book.book_name)

    # author_query = Author.objects.filter(pk=1).prefetch_related('books')
    # for a in author_query:
    #     author = a
    # context = {
    #     "author": author,
    # }
    # books = author.books.first()
    # return HttpResponse(f'<h1>{books.book_name}</h1>')

    # pub_house_query = PublishingHouse.objects.prefetch_related('publishinghouse_books').all()
    # for pub_house in pub_house_query:
    #     for book in pub_house.publishinghouse_books.all():
    #         print(book.book_name)
    # # books_in_pubhouse = pub_house.publishinghouse_books
    # return HttpResponse(f'<h1>1</h1>')


