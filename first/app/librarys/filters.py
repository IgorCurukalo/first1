import django_filters
from django import forms
from app.librarys.models import Librarys

class LibrarysFilter(django_filters.FilterSet):

    librarys_name = django_filters.CharFilter(widget=forms.TextInput(attrs={"class": "librarys_text"}))
    librarys_address = django_filters.CharFilter(widget=forms.TextInput(attrs={"class": "librarys_text"}))

    class Meta:
        model = Librarys
        fields = ['librarys_name', 'librarys_address']
        exclude = ['library_img']