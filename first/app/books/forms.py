from django import forms
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from app.books.models import Books, Author


class BookForm(forms.Form):

    author_query = Author.objects.all()

    author_array = [
        (author.id, f'{author.last_name} {author.first_name} {author.father_name}') for author in author_query
        ]

    book_name = forms.CharField(
        min_length=4,
        widget=forms.TextInput(attrs={"class": "filter"}),
        label='Название книги'
    )

    authors = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple(),
            choices=author_array,
            required=False,
            label='Авторы'
        )

