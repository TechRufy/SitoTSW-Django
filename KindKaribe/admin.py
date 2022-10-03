from django.contrib import admin

# Register your models here.

from .models import Prodotto, Immagine, Categoria, MetodoPagamento, Utente

admin.site.register(Prodotto)
admin.site.register(Immagine)
admin.site.register(Categoria)
admin.site.register(MetodoPagamento)
admin.site.register(Utente)
