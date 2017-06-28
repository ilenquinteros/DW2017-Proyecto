from django import forms
from models import Categoria

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