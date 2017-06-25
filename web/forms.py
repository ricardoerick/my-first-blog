from django import forms
from django.forms import extras
#from rest_framework import serializers
from django.shortcuts import render
from .models import *
from django.contrib.admin.widgets import AdminDateWidget
    
#inicia Pasajero

class fCliente(forms.ModelForm):
	class Meta:
		model=Cliente2
		fields=('FechaInscripcion','NombreCliente','ApellidoPaterno','ApellidoMaterno','Direccion','Municipio','NumeroTelefono','DiaPago')

class fUsuario(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=usuarioWiver
        fields = ('username','email','password','first_name','last_name','Nombre','ApellidoPaterno','ApellidoMaterno','NumeroTelefono','Direccion','Municipio','tipo_Empleado')

class fBitacora(forms.ModelForm):
	class Meta:
		model=Bitacora
		fields=('Fecha','Actividades','Descripcion','Beneficios','Nombre')

class fMantenimiento(forms.ModelForm):
	class Meta:
		model=Mantenimiento
		fields=('Fecha','Descripcion','Costo','Nombre','NombreCliente')

class fUnidad(forms.ModelForm):
	class Meta:
		model=Unidad
		fields=('Numero','Placa','Marca','Modelo','Color','Nombre')

class fTaller(forms.ModelForm):
	class Meta:
		model=Taller
		fields=('FechaInicio','FechaFin','Descripcion','Costo','Placa')

class fCombustible(forms.ModelForm):
	class Meta:
		model=Combustible
		fields=('Cantidad','Descripcion','Placa','Nombre')
