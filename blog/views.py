from django.shortcuts import get_object_or_404, redirect, render

from .forms import AlbumForm, BuscarPostForm, IntegranteForm, PostForm
from .models import Album, Integrante, Post


def inicio(request):
    """Muestra las publicaciones cargadas, ordenadas por fecha descendente."""
    posts = Post.objects.all().order_by('-fecha', '-id')
    return render(request, 'blog/inicio.html', {'posts': posts})


def crear_post(request):
    """Permite cargar una nueva publicación del blog."""
    form = PostForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('inicio')

    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Crear publicación'})


def crear_integrante(request):
    """Permite registrar un integrante de Airbag."""
    form = IntegranteForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('listar_integrantes')

    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Agregar integrante'})


def crear_album(request):
    """Permite registrar un álbum de Airbag."""
    form = AlbumForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('listar_albumes')

    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Agregar álbum'})


def listar_integrantes(request):
    """Lista los integrantes cargados."""
    integrantes = Integrante.objects.all().order_by('nombre')
    return render(request, 'blog/integrantes.html', {'integrantes': integrantes})


def listar_albumes(request):
    """Lista los álbumes cargados."""
    albumes = Album.objects.all().order_by('-anio', 'titulo')
    return render(request, 'blog/albumes.html', {'albumes': albumes})


def buscar_post(request):
    """Busca publicaciones por título o contenido."""
    form = BuscarPostForm(request.GET or None)
    resultados = []
    termino = ''

    if form.is_valid():
        termino = form.cleaned_data['busqueda']
        resultados = Post.objects.filter(titulo__icontains=termino).order_by('-fecha', '-id')

    return render(
        request,
        'blog/buscar.html',
        {'form': form, 'resultados': resultados, 'termino': termino},
    )


def acerca(request):
    """Muestra información sobre el proyecto y la temática elegida."""
    return render(request, 'blog/acerca.html')


def eliminar_post(request, id):
    """Elimina una publicación existente desde la página de inicio."""
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.delete()

    return redirect('inicio')
