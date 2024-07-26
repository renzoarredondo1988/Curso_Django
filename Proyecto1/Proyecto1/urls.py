"""
URL configuration for Proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from Proyecto1.views import saludo, despedida,dameFecha,calculaEdad #debemos importar de nuestro proyecto el modulo views donde creamos la funcion
#saludo

urlpatterns = [
    path('admin/', admin.site.urls),#viene por defecto
    path("saludo/",saludo),#agregamos nuestro path con un nombre, mas la funcion
    path("nosveremos/",despedida),
    path("fecha/",dameFecha),
    path("edades/<int:edad>/<int:agnio>",calculaEdad)#La forma de indicarle a django que vamos a pasar por la URL un parametro es
    #con <parametro>, como por defecto es string, agregamos el int: para indicar que es un entero
    ]