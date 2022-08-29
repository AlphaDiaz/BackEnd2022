from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import datetime 
#NO OLVIDAR IMPORTAR SIN EQUIVOCARSE EN EL LEXICO


# Create your views here.
#CREAR NUESTRA PRIMERA VISTA EN PYTHON

def display(request):#INGRESA DATOS DE ENTRADA EN NUESTRA VISTA
    return HttpResponse("<h1> HELLO WORD 🌎 FELIPE DIAZ</H1>") #Para que funcione se debe importarse el httpRequest como esta rriba con from...



#SEGUNDA VISTA DE NUESTRA APP

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b> Fecha y Hora Actual: </b>" +str(dt)
    return HttpResponse(s)


def botonera(request):
    btn = "<button>CLICK AQUI!</button>"
    return HttpResponse(btn)

""" def testDeImagen(request):
    img = ("<img></img>")  """