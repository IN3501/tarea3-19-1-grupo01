from django.db import models

# Create your models here.
class Item(models.Model):
	nombre_item=models.CharField(max_length=250, primary_key=True)
	cantidad_disponible=models.IntegerField()

class Usuario(models.Model):
	rut=models.IntegerField(primary_key=True)
	nombre=models.CharField(max_length=250)
	telefono=models.IntegerField()
	email=models.CharField(max_length=250)
	es_admin=models.BooleanField(default=False)

class Evento(models.Model):
	fecha=models.DateField()
	lugar=models.CharField(max_length=250,primary_key=True)
	Usuario_rut=models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Items_agendados(models.Model):
	Usuario_rut=models.ForeignKey(Usuario, on_delete=models.CASCADE)
	Evento_lugar=models.ForeignKey(Evento, on_delete=models.CASCADE)
	nombre_item=models.ForeignKey(Item, on_delete=models.CASCADE)