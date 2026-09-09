from django.contrib import admin
from .models import Visita, ConsultaCliente, TrabajoFoto

@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'ip_address')
    readonly_fields = ('fecha', 'ip_address')

@admin.register(ConsultaCliente)
class ConsultaClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'barrio', 'telefono', 'fecha_creacion')
    search_fields = ('nombre', 'barrio', 'telefono')

@admin.register(TrabajoFoto)
class TrabajoFotoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_subida')