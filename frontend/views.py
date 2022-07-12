from django.shortcuts import render, redirect
from .models import Producto


# Create your views here.
def cuerpo(request):
    return render(request, 'cuerpo.html')

def donacion(request):
    return render(request, 'donacion.html')

def gatos(request):
    return render(request, 'gatos.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def otros(request):
    return render(request, 'otros.html')

def Perros(request):
    return render(request, 'Perros.html')

def PetsFriends(request):
    return render(request, 'PetsFriends.html')

def signIn(request):
    return render(request, 'signIn.html')

def signUp(request):
    return render(request, 'signUp.html')

def index(request):
    return render(request, 'index.html')

def modificar(request):
    return render(request, 'modificar.html')


def home(request):
    v_producto=Producto.objects.all()
    datos={'producto': v_producto}
    return render(request, 'index.html', datos)    


def guardarProducto(request):
    
    v_idproducto=request.POST.get('idproducto')
    v_nomproducto=request.POST.get('nombre')
    v_preproducto=request.POST.get('precio')
    v_stockproducto=request.POST.get('stock')

    nuevo=Producto()
    nuevo.idProducto=v_idproducto
    nuevo.nombre=v_nomproducto
    nuevo.stock=v_stockproducto
    nuevo.precio=v_preproducto

    Producto.save(nuevo)

    return redirect('../api/')
    
    #no toma el request y dice que falta un argumento posicional.
def eliminarProducto(request, p_idProducto):
    buscado=Producto.objects.get(idProducto=p_idProducto)
    if(buscado):
        Producto.delete(buscado)
        return redirect(request, '../api/')



def buscarProducto(request, p_idProducto):
    buscado=Producto.objects.get(idProducto=p_idProducto)
    datos={'producto': buscado}
    return render(request, 'modificar.html', datos)

def guardarProductoModificado(request):
    v_idproducto=request.POST.get('idproducto')
    v_nomproducto=request.POST.get('nombre')
    v_preproducto=request.POST.get('precio')
    v_stockproducto=request.POST.get('stock')

    buscado=Producto.objects.get(idProducto=v_idproducto)

    if(buscado):
        buscado.idproducto=v_idproducto
        buscado.nombre=v_nomproducto
        buscado.stock=v_stockproducto
        buscado.precio=v_preproducto

        Producto.save(buscado)
        return redirect('../api/')

