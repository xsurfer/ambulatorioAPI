from django.db import models


class VisiteQuerySet(models.QuerySet):
    pass
    # def perPaziente(self, paziente_id):
    #     try:
    #         paziente = self.get(paziente_id=paziente_id)
    #     except ObjectDoesNotExist:
    #         raise Http404
    #     return self.filter(paziente_id=paziente.id).all()
    #
    # def perPazienteVisita(self, paziente_id, visita_id):
    #     return self.filter(id=visita_id, paziente_id=paziente_id )
