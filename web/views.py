from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import *
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect

from django.contrib.auth.forms import   UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.db.models import Q
from models import Cliente2
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from io import BytesIO
from reportlab.pdfgen import canvas

# Create your views here.
#def home(request):
#	return render_to_response('base.html',context_instance = RequestContext(request))

def index(request):
	return render_to_response('base.html',context_instance =RequestContext(request))

def administracion(request):
	return render_to_response('base4.html',context_instance =RequestContext(request))

def prueba(request):
  return render_to_response('pruebaUsuario.html',context_instance =RequestContext(request))



def iniciar_sesion(request):
  if not request.user.is_anonymous():
    return HttpResponseRedirect('/administracion/')
  if request.method == 'POST':
    formulario = AuthenticationForm(request.POST)
    if formulario.is_valid:
      username = request.POST['username']
      clave = request.POST['password']
      acceso = authenticate(username = username, password = clave)
      if acceso is not None:
        if acceso.is_active:
          login(request, acceso)
          return HttpResponseRedirect('/administracion/')
        else:
          return HttpResponseRedirect('/administracion/')
  else:
    formulario=AuthenticationForm()
  return render_to_response('login.html',{'formulario':formulario},context_instance=RequestContext(request))

def cerrar_sesion(request):
  logout(request)
  return HttpResponseRedirect('/index/')



@login_required(login_url = '/usuario/login/')
def agregarCliente(request):
        if request.method == 'POST':
            ClienteForm = fCliente(request.POST)
            if ClienteForm.is_valid():
                post = ClienteForm.save(commit=False)
                post.author=request.user  
                post.save()
                post= fCliente()
                return HttpResponseRedirect("/cliente/1")
        else:
            ClienteForm= fCliente()
        return render(request, 'formularioCliente.html', {'formCliente': ClienteForm})  
@login_required(login_url = '/usuario/login/')
def cliente(request,activo):
    cliente=Cliente2.objects.filter(Estatus=activo)
    return render(request, 'listaDeclientes.html',{'cliente':cliente})
@login_required(login_url = '/usuario/login/')
def editar_cliente(request, id_cliente):
       cliente=Cliente2.objects.get(pk=id_cliente)
       if request.method == "POST":
        formulario = fCliente(request.POST,instance=cliente)
        if formulario.is_valid():
            
            formulario.save()
            return HttpResponseRedirect("/cliente/1")
       else:
        formulario = fCliente(instance=cliente)

       return render_to_response("editarCliente.html",{"formulario":formulario}, context_instance=RequestContext(request))
@login_required(login_url = '/usuario/login/')
def eliminar_cliente(request, id_cliente):
  cliente= Cliente2.objects.get(pk=id_cliente)
  cliente.Estatus = 0
  cliente.save()
  return HttpResponseRedirect("/cliente/1")

@login_required(login_url = '/usuario/login/')
def reactivarCliente(request, id_cliente):
  cliente= Cliente2.objects.get(pk=id_cliente)
  cliente.Estatus = 1
  cliente.save()
  return HttpResponseRedirect("/cliente/0")

@login_required(login_url = '/usuario/login/')
def agregar_bitacora (request):
        if request.method == 'POST':
            bitacoraForm = fBitacora(request.POST)
            if bitacoraForm.is_valid():
                post = bitacoraForm.save(commit=False)
                post.author=request.user    
                post.save()
                post= fBitacora()

                return HttpResponseRedirect("/bitacora/1")
        else:
            bitacoraForm= fBitacora()
        return render(request, 'formularioBitacora.html', {'bitacoraForm': bitacoraForm}) 

@login_required(login_url = '/usuario/login/')
def bitacora(request,activo):
    bitacora=Bitacora.objects.filter(Estatus=activo)
    return render(request, 'listaDeBitacoras.html',{'bitacora':bitacora})

@login_required(login_url = '/usuario/login/')
def editar_bitacora(request, id_bitacora):
       bitacora=Bitacora.objects.get(pk=id_bitacora)
       if request.method == "POST":
        formulario = fBitacora(request.POST,instance=bitacora)
        if formulario.is_valid():
            
            formulario.save()
            return HttpResponseRedirect("/bitacora/1")
       else:
        formulario = fBitacora(instance=bitacora)

       return render_to_response("editarBitacora.html",{"formulario":formulario}, context_instance=RequestContext(request))

@login_required(login_url = '/usuario/login/')
def eliminar_bitacora(request, id_bitacora):
  bitacora= Bitacora.objects.get(pk=id_bitacora)
  bitacora.Estatus = 0
  bitacora.save()
  return HttpResponseRedirect("/bitacora/1")

@login_required(login_url = '/usuario/login/')
def reactivarBitacora(request, id_bitacora):
  bitacora= Bitacora.objects.get(pk=id_bitacora)
  bitacora.Estatus = 1
  bitacora.save()
  return HttpResponseRedirect("/bitacora/0")

@login_required(login_url = '/usuario/login/')
def agregar_mantenimiento (request):
        if request.method == 'POST':
            mantenimientoForm = fMantenimiento(request.POST)
            if mantenimientoForm.is_valid():
                post = mantenimientoForm.save(commit=False)
                post.author=request.user    
                post.save()
                post= fMantenimiento()

                return HttpResponseRedirect("/mantenimiento/1")
        else:
            mantenimientoForm= fMantenimiento()
        return render(request, 'formularioMantenimiento.html', {'mantenimientoForm': mantenimientoForm}) 

@login_required(login_url = '/usuario/login/')
def mantenimiento(request,activo):
    mantenimiento=Mantenimiento.objects.filter(Estatus=activo)
    return render(request, 'listaDeMantenimientos.html',{'mantenimiento':mantenimiento})

@login_required(login_url = '/usuario/login/')
def editar_mantenimiento(request, id_mantenimiento):
       mantenimiento=Mantenimiento.objects.get(pk=id_mantenimiento)
       if request.method == "POST":
        formulario = fMantenimiento(request.POST,instance=mantenimiento)
        if formulario.is_valid():
            
            formulario.save()
            return HttpResponseRedirect("/mantenimiento/1")
       else:
        formulario = fMantenimiento(instance=mantenimiento)

       return render_to_response("editarMantenimiento.html",{"formulario":formulario}, context_instance=RequestContext(request))

@login_required(login_url = '/usuario/login/')
def eliminar_mantenimiento(request, id_mantenimiento):
  mantenimiento= Mantenimiento.objects.get(pk=id_mantenimiento)
  mantenimiento.Estatus = 0
  mantenimiento.save()
  return HttpResponseRedirect("/mantenimiento/1")

@login_required(login_url = '/usuario/login/')
def reactivarMantenimiento(request, id_mantenimiento):
  mantenimiento= Mantenimiento.objects.get(pk=id_mantenimiento)
  mantenimiento.Estatus = 1
  mantenimiento.save()
  return HttpResponseRedirect("/mantenimiento/0")

@login_required(login_url = '/usuario/login/')
def agregar_unidad (request):
        if request.method == 'POST':
            unidadForm = fUnidad(request.POST)
            if unidadForm.is_valid():
                post = unidadForm.save(commit=False)
                post.author=request.user    
                post.save()
                post= fUnidad()

                return HttpResponseRedirect("/unidad/1")
        else:
            unidadForm= fUnidad()
        return render(request, 'formularioUnidad.html', {'unidadForm': unidadForm}) 

@login_required(login_url = '/usuario/login/')
def unidad(request,activo):
    unidad=Unidad.objects.filter(Estatus=activo)
    return render(request, 'listaDeUnidades.html',{'unidad':unidad})

@login_required(login_url = '/usuario/login/')
def editar_unidad(request, id_unidad):
       unidad=Unidad.objects.get(pk=id_unidad)
       if request.method == "POST":
        formulario = fUnidad(request.POST,instance=unidad)
        if formulario.is_valid():
            
            formulario.save()
            return HttpResponseRedirect("/unidad/1")
       else:
        formulario = fUnidad(instance=unidad)

       return render_to_response("editarUnidad.html",{"formulario":formulario}, context_instance=RequestContext(request))

@login_required(login_url = '/usuario/login/')
def eliminar_unidad(request, id_unidad):
  unidad= Unidad.objects.get(pk=id_unidad)
  unidad.Estatus = 0
  unidad.save()
  return HttpResponseRedirect("/unidad/1")

@login_required(login_url = '/usuario/login/')
def reactivarUnidad(request, id_unidad):
  unidad= Unidad.objects.get(pk=id_unidad)
  unidad.Estatus = 1
  unidad.save()
  return HttpResponseRedirect("/unidad/0")

@login_required(login_url = '/usuario/login/')
def agregar_taller (request):
        if request.method == 'POST':
            tallerForm = fTaller(request.POST)
            if tallerForm.is_valid():
                post = tallerForm.save(commit=False)
                post.author=request.user    
                post.save()
                post= fTaller()

                return HttpResponseRedirect("/taller/1")
        else:
            tallerForm= fTaller()
        return render(request, 'formularioTaller.html', {'tallerForm': tallerForm}) 

@login_required(login_url = '/usuario/login/')
def taller(request,activo):
    taller=Taller.objects.filter(Estatus=activo)
    return render(request, 'listaDeTalleres.html',{'taller':taller})

@login_required(login_url = '/usuario/login/')
def editar_taller(request, id_taller):
       taller=Taller.objects.get(pk=id_taller)
       if request.method == "POST":
        formulario = fTaller(request.POST,instance=taller)
        if formulario.is_valid():
            
            formulario.save()
            return HttpResponseRedirect("/taller/1")
       else:
        formulario = fTaller(instance=taller)

       return render_to_response("editarTaller.html",{"formulario":formulario}, context_instance=RequestContext(request))

@login_required(login_url = '/usuario/login/')
def eliminar_taller(request, id_taller):
  taller= Taller.objects.get(pk=id_taller)
  taller.Estatus = 0
  taller.save()
  return HttpResponseRedirect("/taller/1")

@login_required(login_url = '/usuario/login/')
def reactivarTaller(request, id_taller):
  taller= Taller.objects.get(pk=id_taller)
  taller.Estatus = 1
  taller.save()
  return HttpResponseRedirect("/taller/0")

@login_required(login_url = '/usuario/login/')
def agregar_combustible (request):
        if request.method == 'POST':
            combustibleForm = fCombustible(request.POST)
            if combustibleForm.is_valid():
                post = combustibleForm.save(commit=False)
                post.author=request.user    
                post.save()
                post= fCombustible()

                return HttpResponseRedirect("/combustible/1")
        else:
            combustibleForm= fCombustible()
        return render(request, 'formularioCombustible.html', {'combustibleForm': combustibleForm}) 

@login_required(login_url = '/usuario/login/')
def combustible(request,activo):
    combustible=Combustible.objects.filter(Estatus=activo)
    return render(request, 'listaDeCombustibles.html',{'combustible':combustible})

@login_required(login_url = '/usuario/login/')
def editar_combustible(request, id_combustible):
       combustible=Combustible.objects.get(pk=id_combustible)
       if request.method == "POST":
        formulario = fCombustible(request.POST,instance=combustible)
        if formulario.is_valid():
            
            formulario.save()
            return HttpResponseRedirect("/combustible/1")
       else:
        formulario = fCombustible(instance=combustible)

       return render_to_response("editarCombustible.html",{"formulario":formulario}, context_instance=RequestContext(request))

@login_required(login_url = '/usuario/login/')
def eliminar_combustible(request, id_combustible):
  combustible= Combustible.objects.get(pk=id_combustible)
  combustible.Estatus = 0
  combustible.save()
  return HttpResponseRedirect("/combustible/1")

@login_required(login_url = '/usuario/login/')
def reactivarCombustible(request, id_combustible):
  combustible= Combustible.objects.get(pk=id_combustible)
  combustible.Estatus = 1
  combustible.save()
  return HttpResponseRedirect("/combustible/0")

@login_required(login_url = '/usuario/login/')
def addUsuario(request):
    if request.method=="POST":
      usuario_form=fUsuario(request.POST)
      if usuario_form.is_valid():
        formulario = usuario_form.save()
        formulario.set_password(usuario_form.cleaned_data['password'])
        formulario.save()
        return redirect("/usuario/1")
     
    else:
      usuario_form=fUsuario()
      return render(request,'formularioUsuario.html',{'usuario_form':usuario_form})

@login_required(login_url = '/usuario/login/')
def usuario(request,activo):
    usuario=usuarioWiver.objects.filter(Estatus=activo)
    return render(request, 'listaDeUsuarios.html',{'usuario':usuario})

@login_required(login_url = '/usuario/login/')
def editar_usuario(request, id_usuario):
       usuario=usuarioWiver.objects.get(pk=id_usuario)
       if request.method == "POST":
        formulario = fUsuario(request.POST,instance=usuario)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/usuario/1")
       else:
        formulario = fUsuario(instance=usuario)

       return render_to_response("editarUsuario.html",{"formulario":formulario}, context_instance=RequestContext(request))

@login_required(login_url = '/usuario/login/')
def eliminar_usuario(request, id_usuario):
  usuario= usuarioWiver.objects.get(pk=id_usuario)
  usuario.Estatus = 0
  usuario.save()
  return HttpResponseRedirect("/usuario/1")

@login_required(login_url = '/usuario/login/')
def reactivarUsuario(request, id_usuario):
  usuario= usuarioWiver.objects.get(pk=id_usuario)
  usuario.Estatus = 1
  usuario.save()
  return HttpResponseRedirect("/usuario/0")

def generar_pdfClientes(request):
    print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "clientes.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=8,

                            )
    cliente = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de clientes activos", styles['Heading1'])
    cliente.append(header)
    headings = ('Dia de Pago', 'Fecha de Inscripcion', 'Nombre', '', '','Direccion', 'Municipio','Telefono')
    allcliente = [(p.DiaPago, p.FechaInscripcion, p.NombreCliente, p.ApellidoPaterno, p.ApellidoMaterno , p.Direccion, p.Municipio, p.NumeroTelefono) for p in Cliente2.objects.all().filter(Estatus=1).order_by('DiaPago')]
    print allcliente

    t = Table([headings] + allcliente)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (0, 0), 0, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (7, 100), 1, colors.darkblue),
            ('BACKGROUND', (0, 0), (7, 0), colors.dodgerblue)
        ]
    ))
    cliente.append(t)
    doc.build(cliente)
    response.write(buff.getvalue())
    buff.close()
    return response

def generar_pdfUsuarios(request):
    print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "Usuarios.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=8,

                            )
    usuario = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de usuarios activos", styles['Heading1'])
    usuario.append(header)
    headings = ('Tipo de empleado', 'Nombre', 'Telefono', 'Direccion', '')
    allusuario = [(p.tipo_Empleado, p.Nombre, p.NumeroTelefono, p.Direccion, p.Municipio) for p in usuarioWiver.objects.all().filter(Estatus=1).order_by('tipo_Empleado')]
    print allusuario

    t = Table([headings] + allusuario)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (0, 0), 0, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (7, 100), 1, colors.darkblue),
            ('BACKGROUND', (0, 0), (7, 0), colors.dodgerblue)
        ]
    ))
    usuario.append(t)
    doc.build(usuario)
    response.write(buff.getvalue())
    buff.close()
    return response

def generar_pdfMantenimientos(request):
    print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "Mantenimientos.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=8,

                            )
    mantenimiento = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de mantenimientos activos", styles['Heading1'])
    mantenimiento.append(header)
    headings = ('Fecha', 'Descripcion', 'Costo', 'Nombre del cliente', 'Nombre de quien realizo')
    allmantenimiento = [(p.Fecha, p.Descripcion, p.Costo, p.NombreCliente, p.Nombre) for p in Mantenimiento.objects.all().filter(Estatus=1).order_by('Fecha')]
    print allmantenimiento

    t = Table([headings] + allmantenimiento)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (0, 0), 0, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (7, 100), 1, colors.darkblue),
            ('BACKGROUND', (0, 0), (7, 0), colors.dodgerblue)
        ]
    ))
    mantenimiento.append(t)
    doc.build(mantenimiento)
    response.write(buff.getvalue())
    buff.close()
    return response

def generar_pdfUnidades(request):
    print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "Unidades.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=8,

                            )
    unidad = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de unidades activas", styles['Heading1'])
    unidad.append(header)
    headings = ('Numero', 'Placa', 'Marca', 'Modelo', 'Color', 'Conductor asignado')
    allunidad = [(p.Numero, p.Placa, p.Marca, p.Modelo, p.Color, p.Nombre) for p in Unidad.objects.all().filter(Estatus=1).order_by('Numero')]
    print allunidad

    t = Table([headings] + allunidad)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (0, 0), 0, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (7, 100), 1, colors.darkblue),
            ('BACKGROUND', (0, 0), (7, 0), colors.dodgerblue)
        ]
    ))
    unidad.append(t)
    doc.build(unidad)
    response.write(buff.getvalue())
    buff.close()
    return response

def generar_pdfTalleres(request):
    print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "Talleres.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=8,

                            )
    taller = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de talleres activas", styles['Heading1'])
    taller.append(header)
    headings = ('Fecha de ingreso', 'Fecha de salida', 'Descripcion', 'Costo', 'Placa')
    alltaller = [(p.FechaInicio, p.FechaFin, p.Descripcion, p.Costo, p.Placa,) for p in Taller.objects.all().filter(Estatus=1).order_by('FechaInicio')]
    print alltaller

    t = Table([headings] + alltaller)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (0, 0), 0, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (7, 100), 1, colors.darkblue),
            ('BACKGROUND', (0, 0), (7, 0), colors.dodgerblue)
        ]
    ))
    taller.append(t)
    doc.build(taller)
    response.write(buff.getvalue())
    buff.close()
    return response

def generar_pdfCombustibles(request):
    print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "Combustibles.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=8,

                            )
    combustible = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de consumo de combustible", styles['Heading1'])
    combustible.append(header)
    headings = ('Conductor que adquiere', 'Unidad que consume','Cantidad (Lt)', 'Descripcion',)
    allcombustible = [(p.Nombre, p.Placa, p.Cantidad, p.Descripcion) for p in Combustible.objects.all().filter(Estatus=1).order_by('Nombre')]
    print allcombustible

    t = Table([headings] + allcombustible)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (0, 0), 0, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (7, 100), 1, colors.darkblue),
            ('BACKGROUND', (0, 0), (7, 0), colors.dodgerblue)
        ]
    ))
    combustible.append(t)
    doc.build(combustible)
    response.write(buff.getvalue())
    buff.close()
    return response

def generar_pdfBitacoras(request):
    print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "Bitacoras.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=8,

                            )
    bitacora = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de bitacoras", styles['Heading1'])
    bitacora.append(header)
    headings = ('Nombre de redactor', 'Fecha','Actividades', 'Descripcion', 'Beneficios')
    allbitacora = [(p.Nombre, p.Fecha, p.Actividades, p.Descripcion, p.Beneficios) for p in Bitacora.objects.all().filter(Estatus=1).order_by('Fecha')]
    print allbitacora

    t = Table([headings] + allbitacora)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (0, 0), 0, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (7, 100), 1, colors.darkblue),
            ('BACKGROUND', (0, 0), (7, 0), colors.dodgerblue)
        ]
    ))
    bitacora.append(t)
    doc.build(bitacora)
    response.write(buff.getvalue())
    buff.close()
    return response