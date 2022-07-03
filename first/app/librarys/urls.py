from django.urls import path
from .views import get_librarys_list


urlpatterns = [
    path('', get_librarys_list),
]