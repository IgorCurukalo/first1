from django import forms
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from app.librarys.models import Librarys, LibrarysStorage, Librarian


class LibrarysForm(forms.Form):

    librarys_name = forms.CharField(
        min_length=4,
        widget=forms.TextInput(attrs={"class": "filter"}),
        label='Название библиотеки'
    )


class LibrarysAddNewForm(forms.ModelForm):

    librarian_query = Librarian.objects.all()

    librarian_array = [
        (librarian.id, f'{librarian.last_name} {librarian.first_name} {librarian.father_name}') for librarian in librarian_query
    ]

    librarian = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        choices=librarian_array,
        required=False,
        label='Библиотекари'
    )

    class Meta:
        model = Librarys
        fields = ['librarys_name', 'description', 'librarian', 'id_librarys_storage', 'library_img']
        widgets = {
            'librarys_name': forms.TextInput(attrs={'class': "filter"}),
            'description': forms.Textarea(attrs={'class': "filter_discription"}),
        }
