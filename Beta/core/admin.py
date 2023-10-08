from django.contrib import admin
from core.models import Publicacion

# Register your models here.
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo','contenido','autor','fecha_creacion')
    pass
admin.site.register(Publicacion,PublicacionAdmin)
