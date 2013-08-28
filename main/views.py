# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from main.models import Grupo, Membresia, Persona


def index(request):
	return render_to_response('main/index.html', context_instance=RequestContext(request))

def grupos(request):
	grupos = Grupo.objects.all()

	return render_to_response('main/grupos.html', locals(), context_instance=RequestContext(request))

def grupo_detalle(request, grupo_id):

	grupo = get_object_or_404(Grupo, pk=grupo_id)
	membresia = Membresia.objects.filter(grupo=grupo_id)
	return render_to_response('main/grupo_detalle.html', locals(), context_instance=RequestContext(request))


def persona_detalle(request, persona_id, grupo_id, tipo):

	persona = get_object_or_404(Persona, pk=persona_id)
	grupo_id = grupo_id
	tipo = tipo
	return render_to_response('main/persona_detalle.html', locals(), context_instance=RequestContext(request))