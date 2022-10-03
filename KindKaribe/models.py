import enum
# Create your models here.
from django.db import models


class Genere():
    Maschio = 'Maschio'
    Femmina = 'Femmina'


class Utente(models.Model):
    nome = models.CharField(max_length=200)
    cognome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    nTelefono = models.CharField(max_length=200)
