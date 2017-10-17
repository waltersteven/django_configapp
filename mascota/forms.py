from django import forms
from mascota.models import Mascota

class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota  #para indicarle de que modelo vamos a crear este formulario
        fields = [
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna',
        ]
        labels = {  #asignamos las etiquetas que van a tener a la hora de mostrar el formulario
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'edad_aproximada': 'Edad aproximada',
            'fecha_rescate': 'Fecha de rescate',
            'persona': 'Adoptante',
            'vacuna': 'Vacunas',
        }
        widgets = {  #son etiquetas html
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.TextInput(attrs={'class':'form-control'}),
            'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate': forms.TextInput(attrs={'class':'form-control'}),
            'persona': forms.Select(attrs={'class':'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
        }