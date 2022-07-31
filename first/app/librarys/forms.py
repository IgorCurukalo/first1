from django import forms
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from app.librarys.models import Librarys, LibrarysStorage, Librarian
from app.librarys.validators import validation_librarys_address, validation_librarys_name


class LibrarysForm(forms.ModelForm):

    librarys_name = forms.CharField(
        required=True,
        min_length=4,
        label='Название библиотеки',
        validators=[validation_librarys_name]
    )

    librarys_address = forms.CharField(
        required=True,
        min_length=10,
        label='Адрес библиотеки',
        validators=[validation_librarys_address]
    )

    librarian_query = Librarian.objects.all()

    librarian_array = [
        (librarian.id, f'{librarian.last_name} {librarian.first_name} {librarian.father_name}') for librarian in librarian_query
    ]

    librarian = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        choices=librarian_array,
        required=True,
        label='Библиотекари'
    )

    class Meta:
        model = Librarys
        fields = ['librarys_name', 'librarys_address', 'description', 'librarian', 'id_librarys_storage', 'library_img']
        widgets = {
            'librarys_name': forms.TextInput(attrs={'class': "librarys_text"}),
            'librarys_address': forms.TextInput(attrs={'class': "librarys_text"}),
            'description': forms.Textarea(attrs={'class': "librarys_textarea"}),
        }
