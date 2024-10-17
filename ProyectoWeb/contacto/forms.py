from django import forms


class FormularioContactos(forms.Form):

    nombre=forms.CharField(label="Nombre",required=True)
    email=forms.CharField(label="Email",required=True)
    contenido=forms.CharField(label="Contenido",required=True,widget=forms.Textarea)



