import django_filters
from django import forms
from app.books.models import Books, Author

class BooksFilter(django_filters.FilterSet):

    author_query = Author.objects.all()
    book_name = django_filters.CharFilter(widget=forms.TextInput(attrs={"class": "text"}))
    author = django_filters.ModelChoiceFilter(queryset=Author.objects.all(), widget=forms.Select(attrs={'class': "text"}))

    class Meta:
        model = Books
        fields = ['book_name', 'author']