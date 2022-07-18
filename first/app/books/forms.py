from django import forms
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from app.books.models import Books, Author


class BookForm(forms.Form):

    author_query = Author.objects.all()

    author_array = [
        (author.id, f'{author.first_name, author.last_name}') for author in author_query
        ]

    book_name = forms.CharField(min_length=4)
    authors = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple(),
            choices=author_array,
            required=False
        )
