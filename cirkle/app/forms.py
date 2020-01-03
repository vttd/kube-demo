from django import forms

from .models import Cirkle


class CirkleCreateForm(forms.ModelForm):
    class Meta:
        model = Cirkle
        fields = ['radius', 'color']
