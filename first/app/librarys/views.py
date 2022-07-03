from django.shortcuts import render
from .models import Librarys

def get_librarys_list(request):
    library = Librarys.objects.filter(pk=1)
    context = {
        'libs': library,
    }

    return render(request, 'librarys/list_librarys.html', context)