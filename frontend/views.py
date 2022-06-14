from django.shortcuts import render

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

