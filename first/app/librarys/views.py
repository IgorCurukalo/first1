from django_filters.views import FilterView
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse_lazy
from app.librarys.models import Librarys, Librarian
from app.librarys.forms import LibrarysForm
from app.librarys.filters import LibrarysFilter


class LibrarysList(FilterView):

    model = Librarys
    filterset_class = LibrarysFilter
    context_object_name = 'librarys'
    template_name = 'librarys/librarys_list.html'
    paginate_by = settings.OBJECTS_ON_PAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['librarys'] = self.queryset
        return context


class LibrarysDetail(DetailView):

    model = Librarys
    pk_url_kwarg = 'pk'


class CreateLibrarysView(CreateView):
    model = Librarys
    form_class = LibrarysForm
    template_name = 'librarys/librarys_add_new.html'
    success_url = reverse_lazy('librarys')