from django.shortcuts import render

from .models import Kube


def index(request):
    kubes = Kube.objects.all()

    return render(request, 'app/index.html', {
        'kubes': kubes
    })
