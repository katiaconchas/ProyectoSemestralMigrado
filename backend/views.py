import email
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Usuario, Usuario_signup
# Create your views here.
def signIn(request):
    return render(request, 'signIn.html')

def signUp(request):
    return render(request, 'signUp.html')

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
    return render(request, 'PetsFriends_usuario.html')

def guardarUsuario(request):
    v_email=request.POST.get('email')
    v_password=request.POST.get('password')
    v_pnombre=request.POST.get('pnombre')
    v_appaterno=request.POST.get('appaterno')

    nuevo=Usuario_signup()
    nuevo.email=v_email
    nuevo.password=v_password
    nuevo.pnombre=v_pnombre
    nuevo.appaterno=v_appaterno

    Usuario_signup.save(nuevo)

    #return redirect('/')

    mensaje="El usuario se ha registrado correctamente"
    
    return redirect('/sign_in/')

