from django.shortcuts import render
from .models import * 
import random

# Create your views here.
def index(request):
	return render(request, 'home.html')

def Agendar(request):
	return render(request, 'Agendar.html')

def contacto(request):
	return render(request, 'contacto.html')

def registros(request):
	return render(request, 'registros.html')	

def listo(request):
	diccionario0={}
	return render(request, "listo.html", diccionario0)	

def inicio(request):
	return render(request, 'inicio.html')

def agrega_datos(request):
	for x in range(10):
		user = Usuario(rut=12345670+x, nombre='User '+str(x), telefono=2343445, email='user'+str(x)+'@gmail.com', es_admin=False)
		user.save()
		item = Item(nombre_item='item'+str(x), cantidad_disponible=random.randint(1, 100))
		item.save()
	return listo(request)

def recuperar(request):
	diccionario={}
	items=request.POST.getlist('inputCheck')
	diccionario["item1"]=items
	return render(request, "mostrar_resultado.html", diccionario)

def inventario(request):
	diccionario = {};
	diccionario['item'] = Usuario.objects.all()
	print(diccionario)
	print('heello world')
	return render(request, 'inventario.html')

def recuperar_inv(request):
	diccionario2={}
	return render(request, "mostrar_inventario.html", diccionario2)

def agrega_usuario(request):
	rut = request.POST('rut')
	nombre = request.POST('nombre')
	telefono = request.POST('telefono')
	email = request.POST('email')
	es_admin = request.POST('es_admin')
	usuario = Usuario(rut=rut, nombre=nombre, telefono=telefono, email=email, es_admin=es_admin)
	usuario.save()
	return listo(request)

def agrega_item(request):
	nombre_item = request.POST('nombre_item')
	cantidad_disponible = request.POST('cantidad_disponible')
	item = Item(nombre_item=nombre_item, cantidad_disponible=cantidad_disponible)
	item.save()
	return listo(request)

def agrega_evento(request):
	fecha = request.POST('fecha')
	lugar = request.POST('lugar')
	Usuario_rut = request.POST('Usuario_rut')
	evento = Evento(fecha=fecha, lugar=lugar, Usuario_rut=Usuario_rut)
	evento.save()
	return listo(request)