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
        for prodotto in c:
            imm = prodotto.immagine_set
            for roba in imm.all():
                prodotto.__setattr__("immag", roba)

        print(c[0].immagine_set.all().first().URL.removeprefix("%20"))
        return c.filter(Tipo=Tipo.Pasticceria)


class CatalogoG(views.generic.ListView):
    template_name = "Catalogo.html"
    context_object_name = "prodottiPasticceria"

    def get_queryset(self):
        c = Prodotto.objects.all()
        for prodotto in c:
            imm = prodotto.immagine_set
            for roba in imm.all():
                prodotto.__setattr__("immag", roba)

        print(c[0].immag.URL)
        return c.filter(Tipo=Tipo.Vaschetta)
