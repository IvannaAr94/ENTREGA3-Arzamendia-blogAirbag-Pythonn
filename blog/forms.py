from django import forms
from .models import Post, Integrante, Album

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'contenido', 'autor']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
        }

class IntegranteForm(forms.ModelForm):
    class Meta:
        model = Integrante
        fields = ['nombre', 'instrumento', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'instrumento': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['titulo', 'anio', 'descripcion']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class BuscarPostForm(forms.Form):
    busqueda = forms.CharField(label='Buscar publicación', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: recital, álbum, Airbag'}))
