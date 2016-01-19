from __future__ import unicode_literals

from django.db import models

from anagrafica.models import Paziente
from visite.query import VisiteQuerySet


class Visita(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    data_visita = models.DateField()
    paziente = models.ForeignKey(Paziente, related_name='visite')
    owner = models.ForeignKey('auth.User', related_name='visite')
    anamnesi = models.TextField(max_length=1000, null=False, blank=True)
    esame_obiettivo = models.TextField(max_length=1000, null=False, blank=True)
    conclusioni = models.TextField(max_length=1000, null=False, blank=True)

    objects = VisiteQuerySet.as_manager()

    class Meta:
        ordering = ('created',)
        db_table = 'visite'


    #diagnosi = models.TextField(max_length=1000, null=False, blank=True)
    #terapia = models.TextField(max_length=1000, null=False, blank=True)