from django import forms
from .models import Asiento

class SelectAsientoForm(forms.Form):
    ruta = forms.ChoiceField(choices=[], required=True, label='Ruta')
    asiento = forms.ChoiceField(choices=[], required=True, label='Asiento')
    
    def __init__(self, *args, **kwargs):
        ruta_choices = kwargs.pop('ruta_choices', [])
        asiento_choices = kwargs.pop('asiento_choices', [])
        super().__init__(*args, **kwargs)
        self.fields['ruta'].choices = ruta_choices
        self.fields['asiento'].choices = asiento_choices