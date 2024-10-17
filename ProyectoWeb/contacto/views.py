from django.shortcuts import render,HttpResponse, redirect
from .forms import FormularioContactos
from django.core.mail import EmailMessage #Para configurar el envio de correos electronicos al enviar formulario


# Create your views here.
def contacto(request):

     formulario_contacto=FormularioContactos()

     if request.method=='POST':
          formulario_contacto=FormularioContactos(data=request.POST)
          if formulario_contacto.is_valid():
               nombre=request.POST.get("nombre")
               email=request.POST.get("email")
               contenido=request.POST.get("contenido")

               email=EmailMessage("Mensaje desde App Django",
                                  "El usuario con el nombre {} con la direccion {} escribe lo siguiente {}/n/n ".format(nombre,email,contenido),
                                  "",["renzo.mau1988@gmail.com"],reply_to=[email]
                                 )
               
               try:
                    email.send()
                    return redirect("/contacto/?valido")
               except:
                    return redirect("/contacto/?novalido")

          return redirect("/contacto/?valido")

     return render(request,"contacto/contacto.html",{"miFormulario":formulario_contacto})