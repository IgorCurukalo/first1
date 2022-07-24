from django.urls import path
from .views import BookList, BooksDetail, add_books, CreateBooksView


urlpatterns = [
    path('', BookList.as_view(), name='main'),
    path('<int:pk>', BooksDetail.as_view(), name='detail_books'),
    path('add_books', add_books, name='add_books'),
    path('books_add_new/', CreateBooksView.as_view(), name='books_add_new')
]