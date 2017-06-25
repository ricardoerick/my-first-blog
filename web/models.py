#encoding:utf-8
from __future__ import unicode_literals
from django import forms
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
#class Cliente(models.Model):
 #   Nombre = models.CharField(max_length=25)
  #  ApellidoPaterno = models.CharField(verbose_name='Apellido Paterno', max_length=15)
   # ApellidoMaterno = models.CharField(verbose_name='Apellido Materno', max_length=15)
    #Direccion = models.CharField(verbose_name='Dirección', max_length=50, blank=True, null=True)
    #Municipio = models.CharField(max_length=35)
 #   NumeroTelefono = models.CharField(verbose_name='Número Telefónico', max_length = 14, default = '000-00-0-00-00')
  #  DiaPago = models.IntegerField(verbose_name='Dia de Pago')
   # Estatus = models.BooleanField('1', default=True)


 #   def __str__(self):
  #      return '%s %s %s' % (self.Nombre, self.ApellidoPaterno, self.ApellidoMaterno)

class User(AbstractUser):
   tipos = (
    (u'1', u'Administrador'),
    (u'2', u'Tecnico'),
    (u'3', u'Cobranza'),
    )

   tipo_Empleado = models.CharField("Tipo de Empleado", max_length=2, choices=tipos)

   class Meta:
        db_table = 'auth_user'

class usuarioWiver(User):
    Nombre = models.CharField(max_length=25)
    ApellidoPaterno = models.CharField(verbose_name='Apellido Paterno', max_length=15)
    ApellidoMaterno = models.CharField(verbose_name='Apellido Materno', max_length=15)
    NumeroTelefono = models.CharField(verbose_name='Número Telefónico', max_length = 14, default = '000-00-0-00-00')
    Direccion = models.CharField(verbose_name='Dirección', max_length=50, blank=True, null=True)
    Municipio = models.CharField(max_length=35) 
    Estatus = models.BooleanField('1', default=True)

    def __str__(self):
        return '%s %s' % (self.Nombre, self.ApellidoPaterno)

class Unidad(models.Model):
    Numero = models.CharField(max_length=25)
    Placa = models.CharField(verbose_name='Placa', max_length=10)
    Marca = models.CharField(verbose_name='Marca', max_length=10)
    Modelo = models.CharField(verbose_name='Modelo', max_length=10, blank=True, null=True)
    Color = models.CharField(max_length=10)
    Nombre = models.ForeignKey(usuarioWiver)
    Estatus = models.BooleanField('1', default=True)

    def __str__(self):
        return '%s %s' % (self.Placa, self.Numero)

class Combustible(models.Model):
    Cantidad = models.FloatField(verbose_name='Cantidad')
    Descripcion = models.CharField(verbose_name='Descripcion', max_length=30)
    Placa =models.ForeignKey(Unidad)
    Nombre = models.ForeignKey(usuarioWiver)
    Estatus = models.BooleanField('1', default=True)

class Taller(models.Model):
     FechaInicio = models.DateField(verbose_name='Fecha Inicio', blank=True, null=True, default = 'DD/MM/AAAA')
     FechaFin = models.DateField(verbose_name='Fecha Fin', blank=True, null=True, default = 'DD/MM/AAAA')
     Descripcion = models.CharField(verbose_name='Descripcion', max_length=50)
     Costo = models.FloatField(verbose_name='Costo')
     Placa =models.ForeignKey(Unidad)
     Estatus = models.BooleanField('1', default=True)
   
class Bitacora(models.Model):
    Fecha = models.DateField(verbose_name='Fecha', blank=True, null=True, default = 'DD/MM/AAAA')
    Actividades = models.CharField(verbose_name='Descripcion', max_length=100)
    Descripcion = models.CharField(verbose_name='Descripcion', max_length=150)
    Beneficios= models.CharField(verbose_name='Descripcion', max_length=100)
    Nombre = models.ForeignKey(usuarioWiver)
    Estatus = models.BooleanField('1', default=True)

class Cliente2(models.Model):
    FechaInscripcion = models.DateField(verbose_name='Fecha de Inscripcion', blank=True, null=True, default = 'DD/MM/AAAA')
    NombreCliente = models.CharField(max_length=25)
    ApellidoPaterno = models.CharField(verbose_name='Apellido Paterno', max_length=15)
    ApellidoMaterno = models.CharField(verbose_name='Apellido Materno', max_length=15)
    Direccion = models.CharField(verbose_name='Dirección', max_length=50, blank=True, null=True)
    Municipio = models.CharField(max_length=35)
    NumeroTelefono = models.CharField(verbose_name='Número Telefónico', max_length = 14, default = '000-00-0-00-00')
    DiaPago = models.IntegerField(verbose_name='Dia de Pago')
    Estatus = models.BooleanField('1', default=True)

    def __str__(self):
        return '%s %s' % (self.NombreCliente, self.ApellidoPaterno )

class Mantenimiento(models.Model):
    Fecha = models.DateField(verbose_name='Fecha ', blank=True, null=True, default = 'DD/MM/AAAA')
    Descripcion = models.CharField(verbose_name='Descripcion', max_length=150)
    Costo = models.FloatField(verbose_name='Costo')
    Nombre = models.ForeignKey(usuarioWiver)
    NombreCliente = models.ForeignKey(Cliente2)
    Estatus = models.BooleanField('1', default=True)

    
