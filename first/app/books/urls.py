from django.urls import path
from .views import BookList, BooksDetail


urlpatterns = [
    path('', BookList.as_view(), name='main'),
    path('<int:pk>', BooksDetail.as_view()),
]