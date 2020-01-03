from django.shortcuts import render, redirect

from .models import Kube
from .forms import KubeCreateForm


def index(request):
    kubes = Kube.objects.all()

    return render(request, 'app/index.html', {
        'kubes': kubes
    })


def create(request):
    form = KubeCreateForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('index')

    return render(request, 'app/create.html', {
        'form': form
    })
