from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Librarys, Librarian

class LibrarysList(ListView):

    model = Librarys
    context_object_name = 'librarys'

class LibrarysDetail(DetailView):

    model = Librarys
    pk_url_kwarg = 'pk'