from django.shortcuts import render

# Create your views here.

from django import views
from .models import Prodotto, Immagine, Tipo



class Home(views.generic.TemplateView):
    template_name = "home.html"


class Catalogo(views.generic.ListView):
    template_name = "Catalogo.html"
    context_object_name = "prodottiPasticceria"

    def get_queryset(self):
        c = Prodotto.objects.all()
        return c.filter(Tipo=Tipo.Pasticceria)


class CatalogoG(views.generic.ListView):
    template_name = "Catalogo.html"
    context_object_name = "prodottiPasticceria"

    def get_queryset(self):
        c = Prodotto.objects.all()
        return c.filter(Tipo=Tipo.Vaschetta)





