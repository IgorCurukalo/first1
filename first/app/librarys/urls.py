from django.urls import path
from .views import LibrarysList, LibrarysDetail, add_librarys


urlpatterns = [
    path('', LibrarysList.as_view(), name='librarys'),
    path('<int:pk>', LibrarysDetail.as_view(), name='detail_librarys'),
    path('add_librarys', add_librarys, name='add_librarys'),
]