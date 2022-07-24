import django_filters
from django import forms
from app.librarys.models import Librarys

class LibrarysFilter(django_filters.FilterSet):

    librarys_name = django_filters.CharFilter(widget=forms.TextInput(attrs={"class": "filter"}))

    class Meta:
        model = Librarys
        fields = ['librarys_name']
        exclude = ['library_img']