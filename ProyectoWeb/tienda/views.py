from django.shortcuts import render
from .models import Producto

# Create your views here.
def tienda(request):

     productos=Producto.objects.all()
     return render(request,"tienda/tienda.html",{"productos":productos})#en el render de tienda.html, podre 
#acceder a los atributos del objeto productos, que se envian dentro de un dicc con la clave "productos"