from django import forms

from .models import Kube


class KubeCreateForm(forms.ModelForm):
    class Meta:
        model = Kube
        fields = ['width', 'height', 'color']
