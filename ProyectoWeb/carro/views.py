from django.shortcuts import render
from .carro import Carro
from tienda.models import Producto
from django.shortcuts import redirect


# Create your views here.

def agregar_producto(request,producto_id): #producto_id proviene de la URL que se llama al acceder a esta vista.

    carro=Carro(request) #Cada vez que necesitas interactuar con el carrito, creas una nueva instancia
    #de Carro. Esto es necesario porque cada vez que un usuario realiza una acción (como agregar un
    #  producto), quieres acceder y modificar el carrito en función de la sesión actual del usuario.
    #Es decir, en cada interaccion se llama al constructor y se "sobreescriben" los datos del objeto carro

    producto=Producto.objects.get(id=producto_id) #Esta línea busca un objeto Producto en la base de datos
    #cuyo id coincide con el producto_id que se pasó como argumento.

    carro.agregar(producto=producto)#Usas producto=producto para indicar que el argumento producto de la
    #función agregar debe recibir el objeto producto que acabas de recuperar de la base de datos.

    return redirect("Tienda")

def eliminar_producto(request,producto_id):
    
    carro=Carro(request)

    producto=Producto.objets.get(id=producto_id)

    carro.eliminar(producto=producto)

    return redirect("Tienda")

def restar_producto(request,producto_id):
    
    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)

    carro.restar_producto(producto=producto)

    return redirect("Tienda")

def limpiar_carro(request,producto_id):
    
    carro=Carro(request)

    carro.limpiar_carro()

    return redirect("Tienda")