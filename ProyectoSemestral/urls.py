"""ProyectoSemestral URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from frontend.views import cuerpo, donacion, gatos, home, nosotros, otros, Perros, PetsFriends, signIn, signUp, home, modificar, guardarProducto, eliminarProducto, guardarProductoModificado, buscarProducto
from backend.views import signIn, validarUsuario, PetsFriends_usuario, guardarUsuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PetsFriends),
    path('cuerpo/', cuerpo),
    path('donacion/', donacion),
    path('gatos/', gatos),
    path('nosotros/', nosotros),
    path('otros/', otros),
    path('Perros/', Perros),
    path('signIn/', signIn),
    path('signUp/', signUp),
    path('signIn/', signIn),
    path('validarUsuario/', validarUsuario),
    path('PetsFriends_usuario/', PetsFriends_usuario),
    path('guardarUsuario/', guardarUsuario),
    path('api/', include('api.urls')),
    path('api/', home),
    path('modificar/', modificar),
    path('guardarProducto/', guardarProducto),
    path('eliminarProducto', eliminarProducto),
    path('guardarProductoModificado/', guardarProductoModificado),
    path('buscarProducto/', buscarProducto)


]
