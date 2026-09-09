from django.shortcuts import render, redirect
from .models import Visita, ConsultaCliente, TrabajoFoto

def obtener_ip_cliente(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def inicio(request):
    # Registrar la visita en la BD
    ip = obtener_ip_cliente(request)
    Visita.objects.create(ip_address=ip)
    
    # Procesar formulario de contacto
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        barrio = request.POST.get('barrio')
        telefono = request.POST.get('telefono')
        mensaje = request.POST.get('mensaje')
        
        ConsultaCliente.objects.create(
            nombre=nombre,
            barrio=barrio,
            telefono=telefono,
            mensaje=mensaje
        )
        return render(request, 'portal/inicio.html', {'mensaje_exito': True})

    return render(request, 'portal/inicio.html')

def trabajo(request):
    fotos = TrabajoFoto.objects.all().order_by('-fecha_subida')
    return render(request, 'portal/trabajo.html', {'fotos': fotos})