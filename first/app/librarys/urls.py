from django.urls import path
from .views import LibrarysList, LibrarysDetail


urlpatterns = [
    path('', LibrarysList.as_view()),
    path('<int:pk>', LibrarysDetail.as_view()),
]