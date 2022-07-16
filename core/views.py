from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializer
from .carro import Carro

# Create your views here.[]
class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        productos = Producto.objects.all()

        nombre = self.request.GET.get('nombre')

        if nombre:
            productos = productos.filter(nombre=nombre)

        return productos

def index(request):
    return render (request, 'index.html')

def galeriaDeAdopcion(request):
    return render (request, 'galeriaDeAdopcion.html')

def quienesSomos(request):
    return render (request, 'quienesSomos.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method== 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto guardado"
        else:
            data["form"] = formulario
    return render (request, 'contacto.html', data)

def productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render (request, 'productos.html', data)

@permission_required('core.add_producto')
def agregar_productos(request):
    
    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid:
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario
    return render (request, 'productos/agregar_productos.html', data)
@permission_required('core.view_producto')
def listar_productos(request):

    productos = Producto.objects.all()
    data = {
        'productos': productos
    }

    return render (request, 'productos/listar_productos.html',data)
    
@permission_required('core.change_producto')
def modificar_productos(request, id):

    producto = Producto.objects.get (codigo=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto )
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect (to= "productos")
        data["form"] = formulario

    return render (request, 'productos/modificar_productos.html',data)
@permission_required('core.delete_producto')
def eliminar_producto(request, id):
    producto = Producto.objects.get (codigo=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect (to= "productos")

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect (to= "index")
        data["form"] = formulario
    
    return render(request, 'registration/registro.html', data)


def agregar_carro(request, producto_id):
    carro= Carro(request)
    producto = Producto.objects.get(codigo=producto_id)
    carro.agregar(producto)
    return redirect("productos")


def elimar_carro(request, producto_id):
    carro= Carro(request)
    producto = Producto.objects.get(codigo=producto_id)
    carro.eliminar(producto)
    return redirect("productos")


def restar_carro(request, producto_id):
    carro= Carro(request)
    producto = Producto.objects.get(codigo=producto_id)
    carro.restar_producto(producto)
    return redirect("productos")


def limpiar_carro(request):
    carro= Carro(request)
    carro.limpiar()
    return redirect("productos")

def carro(request):
    return render (request, 'carro.html')
    