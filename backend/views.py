import email
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Usuario
# Create your views here.
def signIn(request):
    return render(request, 'signIn.html')

def validarUsuario(request):
    #Recibimos los datos desde el formulario que fueron
    #pasados vias POST
    v_email=request.POST.get('email')
    v_password=request.POST.get('password')

    try:
    #Buscamos el usuario en la base de datos
        usu=Usuario.objects.get(email=v_email, password=v_password)

        if usu:
            request.session['usuario'] = v_email
            return redirect('/PetsFriends_usuario/')
    except:
        return redirect('/signIn/')


def PetsFriends_usuario(request):
    if 'usuario' not in request.session:
        return redirect('/signIn/')
    return render(request, 'Pets_Friends_usuario.html')