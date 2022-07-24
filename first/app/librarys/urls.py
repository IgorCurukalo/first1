from django.urls import path
from .views import LibrarysList, LibrarysDetail, CreateLibrarysView


urlpatterns = [
    path('', LibrarysList.as_view(), name='librarys'),
    path('<int:pk>', LibrarysDetail.as_view(), name='detail_librarys'),
    path('librarys_add_new/', CreateLibrarysView.as_view(), name='librarys_add_new'),
]