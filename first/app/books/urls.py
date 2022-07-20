from django.urls import path
from .views import BookList, BooksDetail, add_books


urlpatterns = [
    path('', BookList.as_view(), name='main'),
    path('<int:pk>', BooksDetail.as_view(), name='detail_books'),
    path('add_books', add_books, name='add_books'),
]