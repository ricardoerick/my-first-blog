from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',

	url(r'^$' , 'django.contrib.auth.views.login',
		{'template_name':'base.html'}, name='login'),
	url(r'^index/$','web.views.index',name='index'),

	url(r'^agregar/cliente', 'web.views.agregarCliente', name='formularioCliente.html'),
	
	url(r'^cliente/(?P<activo>\d+)$', 'web.views.cliente', name='listaDeclientes.html'),

	url(r'^Editar/cliente/(?P<id_cliente>\d+)$', 'web.views.editar_cliente', name='editar_cliente'),

	url(r'^Borrar/cliente/(?P<id_cliente>\d+)$', 'web.views.eliminar_cliente', name='eliminar_cliente'),

	url(r'^Activar/cliente/(?P<id_cliente>\d+)$', 'web.views.reactivarCliente', name='activarCliente'), 

	url(r'^Registrar/Usuarios/$', 'web.views.addUsuario', name='addUsuario'),

	url(r'^usuario/(?P<activo>\d+)$', 'web.views.usuario', name='listaDeUsuarios.html'),

	url(r'^Editar/usuario/(?P<id_usuario>\d+)$', 'web.views.editar_usuario', name='editar_usuario'),

	url(r'^Borrar/usuario/(?P<id_usuario>\d+)$', 'web.views.eliminar_usuario', name='eliminar_usuario'),

	url(r'^Activar/usuario/(?P<id_usuario>\d+)$', 'web.views.reactivarUsuario', name='activarUsuario'), 

	url(r'^Registrar/Bitacora/$', 'web.views.agregar_bitacora', name='agregar_bitacora'),

	url(r'^bitacora/(?P<activo>\d+)$', 'web.views.bitacora', name='listaDeBitacoras.html'),

	url(r'^Editar/bitacora/(?P<id_bitacora>\d+)$', 'web.views.editar_bitacora', name='editar_bitacora'),

	url(r'^Borrar/bitacora/(?P<id_bitacora>\d+)$', 'web.views.eliminar_bitacora', name='eliminar_bitacora'),

	url(r'^Activar/bitacora/(?P<id_bitacora>\d+)$', 'web.views.reactivarBitacora', name='activarBitacora'),  

	url(r'^Registrar/Mantenimiento/$', 'web.views.agregar_mantenimiento', name='agregar_mantenimiento'),

	url(r'^mantenimiento/(?P<activo>\d+)$', 'web.views.mantenimiento', name='listaDeMantenimientos.html'),

	url(r'^Editar/mantenimiento/(?P<id_mantenimiento>\d+)$', 'web.views.editar_mantenimiento', name='editar_mantenimiento'),

	url(r'^Borrar/mantenimiento/(?P<id_mantenimiento>\d+)$', 'web.views.eliminar_mantenimiento', name='eliminar_mantenimiento'),

	url(r'^Activar/mantenimiento/(?P<id_mantenimiento>\d+)$', 'web.views.reactivarMantenimiento', name='activarMantenimiento'), 

	url(r'^Registrar/Unidad/$', 'web.views.agregar_unidad', name='agregar_unidad'),

	url(r'^unidad/(?P<activo>\d+)$', 'web.views.unidad', name='listaDeUnidades.html'),

	url(r'^Editar/unidad/(?P<id_unidad>\d+)$', 'web.views.editar_unidad', name='editar_unidad'),

	url(r'^Borrar/unidad/(?P<id_unidad>\d+)$', 'web.views.eliminar_unidad', name='eliminar_unidad'),

	 url(r'^Activar/unidad/(?P<id_unidad>\d+)$', 'web.views.reactivarUnidad', name='activarUnidad'), 

	url(r'^Registrar/Taller/$', 'web.views.agregar_taller', name='agregar_taller'),

	url(r'^taller/(?P<activo>\d+)$', 'web.views.taller', name='listaDeTalleres.html'),

	url(r'^Editar/taller/(?P<id_taller>\d+)$', 'web.views.editar_taller', name='editar_taller'),

	url(r'^Borrar/taller/(?P<id_taller>\d+)$', 'web.views.eliminar_taller', name='eliminar_taller'),

	url(r'^Activar/taller/(?P<id_taller>\d+)$', 'web.views.reactivarTaller', name='activarTaller'), 

	url(r'^Registrar/Combustible/$', 'web.views.agregar_combustible', name='agregar_combustible'),

	url(r'^combustible/(?P<activo>\d+)$', 'web.views.combustible', name='listaDeCombustibles.html'),

	url(r'^Editar/combustible/(?P<id_combustible>\d+)$', 'web.views.editar_combustible', name='editar_combustible'),

	url(r'^Borrar/combustible/(?P<id_combustible>\d+)$', 'web.views.eliminar_combustible', name='eliminar_combustible'),

	url(r'^Activar/combustible/(?P<id_combustible>\d+)$', 'web.views.reactivarCombustible', name='activarCombustible'),

	url(r'^usuario/login/$', 'web.views.iniciar_sesion', name='iniciar_sesion'),

	url(r'^usuario/salir/$', 'web.views.cerrar_sesion', name='cerrar_sesion'),

	url(r'^PruebaUsuario', 'web.views.prueba', name='pruebaUsuarios.html'),

	url(r'^generar_pdf/cliente/$', 'web.views.generar_pdfClientes', name='pdfClientes'),

	url(r'^generar_pdf/usuario/$', 'web.views.generar_pdfUsuarios', name='pdfUsuarios'),

	url(r'^generar_pdf/mantenimiento/$', 'web.views.generar_pdfMantenimientos', name='pdfMantenimientos'),

	url(r'^generar_pdf/unidad/$', 'web.views.generar_pdfUnidades', name='pdfUnidades'),

	url(r'^generar_pdf/taller/$', 'web.views.generar_pdfTalleres', name='pdfTalleres'),

	url(r'^generar_pdf/combustible/$', 'web.views.generar_pdfCombustibles', name='pdfCombustibles'),

	url(r'^generar_pdf/bitacora/$', 'web.views.generar_pdfBitacoras', name='pdfBitacoras'),


	


)
