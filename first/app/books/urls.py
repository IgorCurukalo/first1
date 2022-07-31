from django.urls import path
from .views import BookList, BooksDetail, CreateBooksView


urlpatterns = [
    path('', BookList.as_view(), name='main'),
    path('<int:pk>', BooksDetail.as_view(), name='detail_books'),
    path('books_add_new/', CreateBooksView.as_view(), name='books_add_new')
]