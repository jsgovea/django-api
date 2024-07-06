from django import forms

from .models import Planet


class PlanetForm(forms.ModelForm):
    class Meta:
        model = Planet
        fields = "__all__"
