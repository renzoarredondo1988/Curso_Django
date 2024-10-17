from django.shortcuts import render
from blog.models import Categoria,Post #importo la ruta el archivo models de la app blog

# Create your views here.

def blog(request):
     
    posts=Post.objects.all() #con este metodo le indico a django que importe todos los objetos de la clase Servicio


    return render(request,"blog/blog.html",{"posts":posts})

def categoria(request,categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request,'blog/categoria.html',{'categoria':categoria,"posts":posts})