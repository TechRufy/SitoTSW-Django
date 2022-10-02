from django.db import models

# Create your models here.
from django.db import models


class utente(models.Model):
    nome = models.CharField(max_length=200)