from django.contrib import admin

from .models import Autor, Articulo, Comentario
from django.contrib import admin

admin.site.register(Autor)
admin.site.register(Articulo)
admin.site.register(Comentario)


