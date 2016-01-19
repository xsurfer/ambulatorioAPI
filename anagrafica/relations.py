from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.reverse import reverse


class PazientiCustomHyperlinkedIdentityField(HyperlinkedIdentityField):
    view_name = 'pazienti-detail'
    #queryset = Visita.visite.all()

    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'pk': obj.paziente.pk,
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

#    url(r'^pazienti/(?P<pk>[0-9]+)/$', views.PazienteDetail.as_view(), name='pazienti-detail'),

