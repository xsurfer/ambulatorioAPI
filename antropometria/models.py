from __future__ import unicode_literals

from django.db import models

from anagrafica.models import Paziente


class RilevamentoAntropometrico(models.Model):
    paziente = models.ForeignKey(Paziente, related_name='antropometria')
    created = models.DateTimeField(auto_now_add=True)
    peso = models.CharField(max_length=50, blank=False, null=False, )
    altezza = models.CharField(max_length=50, blank=False, null=False, )
    circonferenzaCranica = models.CharField(max_length=50, blank=False, null=False, )
    altezzaTronco = models.CharField(max_length=50, blank=False, null=False, )
    circonferenzaToracica = models.CharField(max_length=50, blank=False, null=False, )
    note = models.TextField(max_length=1000, null=False, blank=True)

    class Meta:
        ordering = ('created',)
        db_table = 'rilevamenti_antropometrici'