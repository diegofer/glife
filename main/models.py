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
	grupos = models.ForeignKey(Grupo)
	colideres = models.ForeignKey(Colider)

	
class Miembro(Persona):

	lider = models.OneToOneField(Lider)
	grupo = models.OneToOneField(Grupo)
	
class Colider(Miembro):
	"""
	Posee un lider y un grupo asignado
	al heredar del modelo Miembro
	"""

class Grupo(models.Model):

	lider = models.OneToOneField(Lider)
	colideres = models.ForeignKey(Colider)
	miembros = models.ForeignKey(Miembro)


#class Grupograma(models.Model):

    
		
		

		
		
		
