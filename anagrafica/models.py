from __future__ import unicode_literals

from django.db import models
from django_countries.fields import CountryField

from anagrafica.query import PazientiQuerySet

SESSO_CHOICES = (
    ('M', 'Maschio'),
    ('F', 'Femmina'),
)


class Paziente(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='pazienti')
    nome = models.CharField(max_length=50, blank=False, null=False, )
    cognome = models.CharField(max_length=50, blank=False, null=False, )
    sesso = models.CharField(choices=SESSO_CHOICES, max_length=1, blank=False, null=False)
    codice_fiscale = models.CharField(max_length=16, blank=True, null=False, )
    data_nascita = models.DateField(max_length=100, blank=True, null=False, )
    nazionalita = CountryField(blank=False, null=False, default='IT')
    indirizzo_residenza = models.CharField(max_length=100, null=False, blank=False)
    comune_residenza = models.CharField(max_length=100, null=False, blank=False)
    telefono = models.CharField(max_length=25, null=False, blank=True)
    cellulare = models.CharField(max_length=25, null=False, blank=True)
    email = models.EmailField(max_length=254, unique=False, null=True, blank=True)

    objects = PazientiQuerySet.as_manager()

    class Meta:
        ordering = ('created',)
        db_table = 'pazienti'