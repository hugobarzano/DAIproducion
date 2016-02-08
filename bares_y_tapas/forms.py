from django import forms
from bares_y_tapas.models import *

class BarForm(forms.ModelForm):
    nombre = forms.CharField(max_length=128, help_text="Introduce el nombre del bar")
    direccion = forms.CharField(max_length=256, help_text="Introduce la direccion del bar(Spain,Granada,Calle Recogidas,numero)")
    visitas = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Bar
        fields = ('nombre','direccion')
        #completar aqui con clean del formulario y completar la clase para las tapas


class TapaForm(forms.ModelForm):
    nombre_tapa = forms.CharField(max_length=128, help_text="Introduce el nombre de la tapa")
    megusta = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Tapa
        exclude = ('bar',)
