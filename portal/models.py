from django.db import models

class Visita(models.Model):
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Visita el {self.fecha.strftime('%d/%m/%Y %H:%M')}"

class ConsultaCliente(models.Model):
    nombre = models.CharField(max_length=100)
    barrio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.barrio}"

class TrabajoFoto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, blank=True)
    imagen = models.ImageField(upload_to='trabajos/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo