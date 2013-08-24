from django.db import models
from django.contrib.auth.models import User

class Persona(models.Model):

	nombre 	= models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	telefono = models.IntegerField()
	email = models.CharField(max_length=100, unique=True)
	fecha_nacimiento = models.DateField()
	
class Lider(models.Model):

	persona = models.OneToOneField(Persona)

class Miembro(models.Model):

	persona = models.OneToOneField(Persona)
	grupo = models.ForeignKey(Grupo)

class Colider(models.Model):
	
	persona = models.OneToOneField(Persona)
	grupo = models.ForeignKey(Grupo)

class Grupo(models.Model):

	direccion = models.CharField(max_length=150)
	dia = models.CharField(max_length=10)
	hora = models.TimeField()
	lider = models.ForeignKey(Lider)