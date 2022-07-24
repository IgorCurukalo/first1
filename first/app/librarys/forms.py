from django import forms
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from app.librarys.models import Librarys


class LibrarysForm(forms.Form):

    librarys_name = forms.CharField(min_length=4)

