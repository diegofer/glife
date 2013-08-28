from django.db import models
from django.contrib.auth.models import User



class Persona(models.Model):

	nombre 	   = models.CharField(max_length=50)
	apellido   = models.CharField(max_length=50)
	telefono   = models.IntegerField()
	email       = models.CharField(max_length=100, unique=True)
	fecha_nacimiento = models.DateField()

	def __unicode__(self):
		return '%s %s' %(self.nombre, self.apellido) 




class Grupo(models.Model):

	direccion = models.CharField(max_length=150)
	dia       = models.CharField(max_length=10)
	hora      = models.TimeField()

	def __unicode__(self):
		return self.direccion	




class Membresia(models.Model):

	MIEMBRO   = 'mb'
	LIDER     = 'lid'
	COLIDER   = 'col'

	TIPO_CHOICES = (
		(MIEMBRO, 'Miembro'),
		(LIDER, 'Lider'),
		(COLIDER, 'Colider'),
	)

	persona  = models.OneToOneField(Persona)
	grupo    = models.ForeignKey(Grupo)
	tipo     = models.CharField(max_length=3, choices=TIPO_CHOICES, default=MIEMBRO)



