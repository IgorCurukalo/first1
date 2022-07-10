from django.urls import path
from .views import BooksList, BooksDetail\
    # , get_book


urlpatterns = [
    path('', BooksList.as_view()),
    path('<int:pk>', BooksDetail.as_view()),
]


# 4/7/2022
#
# from .views import get_books_list,get_book
# urlpatterns = [
#     path('', get_books_list),
#     path('<int:id_book>', get_book),
# ]