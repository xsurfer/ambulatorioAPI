from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404


class PazientiQuerySet(models.QuerySet):

    def visitePerPaziente(self, paziente_id):
        try:
            paziente = self.get(pk=paziente_id)
        except ObjectDoesNotExist:
            raise Http404
        return paziente.visite

