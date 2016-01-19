from __future__ import unicode_literals

from django.db import models


class EsameStrumentale(models.Model):
    #paziente = models.ForeignKey(Paziente, related_name='esamiStrumentali')
    created = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=50, blank=False, null=False, )
    descrizione = models.TextField(max_length=1000, null=False, blank=True)

    class Meta:
        ordering = ('created',)
        db_table = 'esami_strumentali'


class EsameLaboratorio(models.Model):
    #paziente = models.ForeignKey(Paziente, related_name='esamiLaboratorio')
    created = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=50, blank=False, null=False, )
    descrizione = models.TextField(max_length=1000, null=False, blank=True)

    class Meta:
        ordering = ('created',)
        db_table = 'esami_laboratorio'
