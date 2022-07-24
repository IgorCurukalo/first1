from django_filters.views import FilterView
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from django.urls import reverse_lazy
from app.librarys.models import Librarys, Librarian
from app.librarys.forms import LibrarysForm, LibrarysAddNewForm
from app.librarys.filters import LibrarysFilter

class LibrarysList(FilterView):

    model = Librarys
    filterset_class = LibrarysFilter
    context_object_name = 'librarys'
    template_name = 'librarys/librarys_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['librarys'] = self.queryset
        return context


class LibrarysDetail(DetailView):

    model = Librarys
    pk_url_kwarg = 'pk'


class CreateLibrarysView(CreateView):
    model = Librarys
    form_class = LibrarysAddNewForm
    template_name = 'librarys/librarys_add_new.html'
    success_url = reverse_lazy('librarys')