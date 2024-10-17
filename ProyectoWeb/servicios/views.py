from django.shortcuts import render
from servicios.models import Servicio #importo la ruta el archivo models de la app servicios
# Create your views here.
def servicios(request):

     servicios=Servicio.objects.all() #con este metodo le indico a django que importe todos los objetos de la clase Servicio

     return render(request,"servicios/servicios.html", {"servicios":servicios})