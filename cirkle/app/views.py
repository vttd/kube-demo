from django.shortcuts import render, redirect

from .models import Cirkle
from .forms import CirkleCreateForm


def index(request):
    cirkles = Cirkle.objects.all()

    return render(request, 'app/index.html', {
        'cirkles': cirkles
    })


def create(request):
    form = CirkleCreateForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('index')

    return render(request, 'app/create.html', {
        'form': form
    })
