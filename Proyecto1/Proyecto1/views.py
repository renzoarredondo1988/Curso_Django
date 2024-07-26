from django.http import HttpResponse
import datetime
from django.template import Template,Context

#Podemos hacer una clase con un constructor y asi poder ingresar con objetos o propiedades del objeto
#a nuestra web
class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request): #primera vista

    #Se puede dar formato al texto que escribamos como si fuera un HTML, no es lo mas elegante
    #lo logico es que se use plantillas (normalmente HTML) que separe el codigo del diseño
    #Si a un archivo le hacemos click derecho y damos copy path en el explorador de VSC, copia la ruta
    #Para usar una plantilla hay que crear un objeto del tipo Template. Luego, crear un contexto (datos
    #adicionales como varaibles, funciones, contenido dinamico). Ultimo paso es renderizar, con el metodo render

    #nombre="Juan" #Vemos que para usar una variable definida e insertarla en nuestra pagina, la agregamos
    #en Context a traves de un diccionario.

    

    #apellido="Diaz"

    p1=Persona("Renzo","Arredondo")
    temasDelCurso=["Plantillas","Modelos","Formularios","Vistas","Despliegue"]

    ahora=datetime.datetime.now()

    doc_externo=open("C:/Users/renzo/OneDrive/Escritorio/Cursos programacion/Curso Django/Proyecto1/plantillas/miplantilla.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora,"temas":temasDelCurso})#Estas variables se agregan en el HTML con {{}}

    documento=plt.render(ctx)

    return HttpResponse (documento)#la variable que contiene el texto la metemos en el return

def despedida(request):
    return HttpResponse("Hasta luego alumnos de Django")

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h1>
    "Fecha y hora actuales %s"
    
    </h1>
    </body>
    </html>
    """ % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request,edad,agnio):

    #edadActual=18
    periodo=agnio-2024
    edadFutura=edad+periodo
    documento="""<html>
    <body>
    <h2>
    "Para el año %s tendras %s"
    
    </h1>
    </body>
    </html>
    """ % (agnio,edadFutura)

    return HttpResponse(documento)

