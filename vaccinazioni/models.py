from __future__ import unicode_literals

from django.db import models
from anagrafica.models import Paziente


class Vaccino(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=50, blank=False, null=False, )
    descrizione = models.TextField(max_length=1000, null=False, blank=True)

    class Meta:
        ordering = ('created',)
        db_table = 'vaccini'


class Vaccinazione(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    paziente = models.ForeignKey(Paziente, on_delete=models.CASCADE)
    tipo_vaccinazione = models.OneToOneField(Vaccino, on_delete=models.CASCADE)
    note = models.TextField(max_length=1000, null=False, blank=True)

    class Meta:
        ordering = ('created',)
        db_table = 'vaccinazioni'