from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.reverse import reverse

from .models import Visita


class PazientiCustomHyperlinkedIdentityField(HyperlinkedIdentityField):
    view_name = 'pazienti-detail'
    #queryset = Visita.visite.all()

    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'pk': obj.paziente.pk,
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

#    url(r'^pazienti/(?P<pk>[0-9]+)/$', views.PazienteDetail.as_view(), name='pazienti-detail'),


class VisiteCustomHyperlinkedIdentityField(HyperlinkedIdentityField):
    view_name = 'visite-detail'
    #queryset = Visita.visite.all()

    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'pk': obj.pk,
            'paziente_pk': obj.paziente.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
            'paziente_pk': view_kwargs['paziente_pk'],
            'pk': view_kwargs['pk']
        }
        return self.get_queryset().get(**lookup_kwargs)


class VisiteCustomHyperlinkedRelatedField(HyperlinkedRelatedField):
    view_name = 'visite-detail'
    queryset = Visita.objects.all()

    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'pk': obj.pk,
            'paziente_pk': obj.paziente.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
            'paziente_pk': view_kwargs['paziente_pk'],
            'pk': view_kwargs['pk']
        }
        return self.get_queryset().get(**lookup_kwargs)
