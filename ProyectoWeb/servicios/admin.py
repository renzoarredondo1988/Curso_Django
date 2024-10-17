from django.contrib import admin


from .models import Servicio



class ServicioAdmin(admin.ModelAdmin):
   readonly_fields=("created","updated")

# Register your models here.
admin.site.register(Servicio, ServicioAdmin)
