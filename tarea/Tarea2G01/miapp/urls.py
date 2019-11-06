from django.urls import path
from .views import * 

urlpatterns = [
	path('', index, name ='index'),
	path('Agendar/', Agendar, name='Agendar'),
	path('contacto/', contacto, name='contacto'),	
	path('inventario/', inventario, name='inventario'),
	path('registros/', registros, name='registros'),
	path('inicio/', inicio, name='inicio'),
	path("mostrar_resultado", recuperar, name='mostrar_resultado'),
	path("mostrar_inventario", recuperar_inv, name='mostrar_inventario'),
	path("listo", listo, name='listo'),
	path("agrega_datos", agrega_datos, name='agrega_datos'),

]