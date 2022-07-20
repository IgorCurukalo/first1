from django.urls import path
from .views import LibrarysList, LibrarysDetail


urlpatterns = [
    path('', LibrarysList.as_view(), name='librarys'),
    path('<int:pk>', LibrarysDetail.as_view(), name='detail_librarys'),
]