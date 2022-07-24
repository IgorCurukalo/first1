from django_filters.views import FilterView
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from app.librarys.models import Librarys, Librarian
from app.librarys.forms import LibrarysForm
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

def add_librarys(request):

    if request.method == 'POST':
        form = LibrarysForm(request.POST)

        if form.is_valid():
            librarys_name = form.cleaned_data['librarys_name']

    form = LibrarysForm()

    context = {
        'form': form,
    }

    return render(request, 'librarys/add_librarys.html', context=context)

class LibrarysDetail(DetailView):

    model = Librarys
    pk_url_kwarg = 'pk'