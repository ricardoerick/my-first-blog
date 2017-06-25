from django.contrib import admin
from models import *

class usuarioWiberAdmin(admin.ModelAdmin):
	list_display = ('Nombre','ApellidoPaterno')
	search_fields = ('Nombre','ApellidoPaterno')

class Cliente2Admin(admin.ModelAdmin):
	list_display = ('NombreCliente','ApellidoPaterno')
	search_fields = ('NombreCliente', 'ApellidoPaterno')

class UnidadAdmin(admin.ModelAdmin):
	list_display = ('Placa','Numero')
	search_fields = ('Placa','Numero')

admin.site.register(usuarioWiver, usuarioWiberAdmin)
admin.site.register(Cliente2, Cliente2Admin)
admin.site.register(Unidad, UnidadAdmin)

