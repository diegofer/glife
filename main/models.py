from django.db import models
from django.contrib.auth.models import User

class Persona(models.User):

	nombre 	= models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	telefono = models.IntegerField()
	email = models.CharField(max_length=100)
	fecha_nacimiento = models.DateField()
	
class Lider(Persona):

	persona = models.ForeignKey(Persona)

	
class Miembro(Persona):

	lider = models.OneToOneField(Lider)
	
class Colider(Miembro):
	
class Grupo(models.Model):

	lider = models.OneToOneField(Lider)


class Grupograma(models.Model):

    
		
		

		
		
		
