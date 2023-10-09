from django.shortcuts import render, redirect, get_object_or_404
from .models import Publicacion
from .forms import PublicacionForm

def listar_publicaciones(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha_creacion')
    return render(request, 'core/lista_publicaciones.html', {'publicaciones': publicaciones})

def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_publicaciones')
    else:
        form = PublicacionForm()
    
    return render(request, 'core/nueva_publicacion.html', {'form': form})

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'core/detalle_publicacion.html', {'publicacion': publicacion})

