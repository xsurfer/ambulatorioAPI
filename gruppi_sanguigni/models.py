from __future__ import unicode_literals

from django.db import models

from anagrafica.models import Paziente

GRUPPO_CHOICES = (
    ('0', '0'),
    ('A', 'A'),
    ('B', 'B'),
    ('AB', 'AB'),
)

RH_CHOICES = (
    ('POS', '+'),
    ('NEG', '-'),
)

class GruppoSanguigno(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    paziente = models.OneToOneField(Paziente, on_delete=models.CASCADE)
    gruppo = models.CharField(choices=GRUPPO_CHOICES, max_length=2, blank=False, null=False)
    rh = models.CharField(choices=RH_CHOICES, max_length=3, blank=False, null=False)

    class Meta:
        ordering = ('created',)
        db_table = 'gruppi_sanguigni'