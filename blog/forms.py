from django import forms
from .models import Autor, Articulo, Comentario

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'email', 'bio']

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'autor']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['articulo', 'autor_nombre', 'contenido']
