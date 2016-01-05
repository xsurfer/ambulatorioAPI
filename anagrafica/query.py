from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404


class PazientiQuerySet(models.QuerySet):

    def visitePerPaziente(self, paziente_id):
        try:
            paziente = self.get(pk=paziente_id)
        except ObjectDoesNotExist:
            raise Http404
        print(paziente)
        return paziente.visite

class VisiteQuerySet(models.QuerySet):
    def perPaziente(self, paziente_id):
        try:
            paziente = self.get(pk=paziente_id)
        except ObjectDoesNotExist:
            raise Http404
        return self.filter(paziente_id=paziente_id).all()

    def perPazienteVisita(self, paziente_id, visita_id):
        return self.filter(id=visita_id, paziente_id=paziente_id )
