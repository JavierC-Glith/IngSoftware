from django import forms
from .models import Publicacion

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'autor']

    def clean(self):
        cleaned_data = super().clean()
        titulo = cleaned_data.get('titulo')
        contenido = cleaned_data.get('contenido')
        autor = cleaned_data.get('autor')

        if not titulo:
            self.add_error('titulo', 'Este campo no puede estar vacío.')

        if not contenido:
            self.add_error('contenido', 'Este campo no puede estar vacío.')

        if not autor:
            self.add_error('contenido', 'Este campo no puede estar vacío')
