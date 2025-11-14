from django import forms
from SGI_app.models import Empleado
#Importar libreria para validar datos
from wsgiref.validate import validator
from django.core import validators

class EmpleadoRegistroForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre")
    rut = forms.CharField(max_length=12, label="RUT")
    email = forms.EmailField(label="Correo Electrónico")
    cargo = forms.CharField(max_length=50, label="Cargo")
    estado = forms.ChoiceField(
        choices=[('', 'Seleccione'), ('1', 'Activo'), ('0', 'Inactivo'),],
        label="Estado",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    nombre.widget.attrs['class'] = 'form-control'
    rut.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    cargo.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'

    nombre.widget.attrs['placeholder'] = 'Juan Perez'
    rut.widget.attrs['placeholder'] = '11111111-1'
    email.widget.attrs['placeholder'] = 'correo@ejemplo.com'
    cargo.widget.attrs['placeholder'] = 'Cargo del empleado'

    nombre.label= "Nombre"
    rut.label= "Rut"
    email.label= "Email"
    cargo.label= "Cargo"
    estado.label= "Estado"

class EmpleadoRegistroForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

    nombre = forms.CharField(max_length=100, label="Nombre")
    rut = forms.CharField(max_length=12, label="RUT")
    email = forms.EmailField(label="Correo Electrónico")
    cargo = forms.CharField(max_length=50, label="Cargo")
    estado = forms.ChoiceField(
        choices=[('', 'Seleccione'), ('1', 'Activo'), ('0', 'Inactivo')],
        label="Estado",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    nombre.widget.attrs['class'] = 'form-control'
    rut.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    cargo.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'

    nombre.widget.attrs['placeholder'] = 'Juan Perez'
    rut.widget.attrs['placeholder'] = '11111111-1'
    email.widget.attrs['placeholder'] = 'correo@ejemplo.com'
    cargo.widget.attrs['placeholder'] = 'Cargo del empleado'

    nombre.label= "Nombre"
    rut.label= "Rut"
    email.label= "Email"
    cargo.label= "Cargo"
    estado.label= "Estado"