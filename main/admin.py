# -*- coding: utf-8 -*-

from django.contrib import admin
from main.models import Persona, Grupo, Membresia


admin.site.register(Persona)
admin.site.register(Grupo)
admin.site.register(Membresia)