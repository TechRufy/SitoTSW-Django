# Create your models here.
from django.db import models
from enumchoicefield import ChoiceEnum, EnumChoiceField


class Genere(ChoiceEnum):
    Maschio = 'Maschio'
    Femmina = 'Femmina'


class Circuito(ChoiceEnum):
    MasterCard = "Mastercard"
    Visa = "Visa"
    AmericanExpress = "AmericanExpress"


class Tipo(ChoiceEnum):
    Vaschetta = "Vaschetta"
    Pasticceria = "Pasticceria"


class Peso(ChoiceEnum):
    Piccola = 500
    Media = 750
    Grande = 1000


class Utente(models.Model):
    Nome = models.CharField(max_length=200, null=True)
    Cognome = models.CharField(max_length=200, null=True)
    Email = models.EmailField(max_length=200, primary_key=True)
    Password = models.CharField(max_length=200, null=False)
    Ntelefono = models.CharField(max_length=200, null=True)
    Genere = EnumChoiceField(Genere, default=Genere.Maschio)
    Admin = models.BooleanField(default=0)
    CodiceFiscale = models.CharField(max_length=16, null=True)
    DataNascita = models.DateField(null=True)


class MetodoPagamento(models.Model):
    Intestatario = models.CharField(max_length=200)
    NumeroCarta = models.CharField(max_length=200)
    MeseScadenza = models.IntegerField()
    AnnoScadenza = models.IntegerField()
    CVV = models.IntegerField()
    Circuito = EnumChoiceField(Circuito, default=Circuito.MasterCard)
    Possessore = models.ForeignKey(Utente, on_delete=models.CASCADE)


class Categoria(models.Model):
    Nome = models.CharField(max_length=200, primary_key=True)
    Descrizione = models.CharField(max_length=200, default="")


class Prodotto(models.Model):
    Nome = models.CharField(max_length=200)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Tipo = EnumChoiceField(Tipo, default=Tipo.Pasticceria)
    Peso = EnumChoiceField(Peso, null=True)
    Prezzo = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    Descrizione = models.CharField(max_length=200, default="")
    QuantitaDisponibile = models.IntegerField(default=0)
    IVA = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    Visibile = models.BooleanField(default=1)

    def save(self, *args, **kwargs):
        if not self.Peso:
            self.Peso = None
        super(Prodotto, self).save(*args, **kwargs)


class Immagine(models.Model):
    URL = models.CharField(max_length=200, default="default.jpg")
    testoALT = models.CharField(max_length=200, default="ALT")
    Prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
