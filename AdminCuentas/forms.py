from django import forms
from models import Categoria, Editor
from Noticias.models import Noticia
from sorl.thumbnail import ImageField

class CategoriaForm(forms.ModelForm):
	class Meta:
		model = Categoria

		fields = [
			'nombre_categoria',
		]

		labels = {
			'nombre_categoria': 'Nombre',
		}

		widgets = {
			'nombre_categoria': forms.TextInput(attrs={'class':'form-control'}),
		}

class NoticiaForm(forms.ModelForm):
	class Meta:
		model = Noticia

		fields = [
			'titulo_noticia',
			'descripcion',
			'contenido',
			'categoria',
			'autor',

		]

		labels = {
			'titulo_noticia': 'Titulo',
			'descripcion': 'Descripcion',
			'contenido':'Contenido',
			'categoria':'Categoria',
			'autor':'Autor',
		}

		widgets = {
			'titulo_noticia': forms.TextInput(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'contenido': forms.TextInput(attrs={'class':'form-control'}),
			'categoria': forms.Select(attrs={'class':'form-control'}),
			'autor': forms.Select(attrs={'class':'form-control'}),
		}

class EditorForm(forms.ModelForm):
	class Meta:
		model = Editor

		fields = [
			'nombre',
			'username',
			'contrasena',
			'email',

		]

		labels = {
			'nombre': 'Nombre',
			'username': 'Usuario',
			'contrasena': 'Contrasena',
			'email': 'Email',
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'username': forms.TextInput(attrs={'class':'form-control'}),
			'contrasena': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
		}