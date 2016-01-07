from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
from django_filters import CharFilter

from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.filters import FilterSet
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .serializers import PazienteSerializer, VisitaSerializer, PazienteDetailSerializer, VisitaDetailSerializer
from .models import Paziente, Visita


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'pazienti': reverse('pazienti-list', request=request, format=format),
    })

class PazienteFilter(FilterSet):
    nome = CharFilter(name='nome', lookup_type='iexact')
    cognome = CharFilter(name='cognome', lookup_type='iexact')
    codice_fiscale = CharFilter(name='codice_fiscale', lookup_type='iexact')

    class Meta:
        model  = Paziente
        fields = ('nome', 'cognome', 'sesso', 'data_nascita', 'codice_fiscale' )

# /pazienti/
class PazienteList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    serializer_class = PazienteSerializer
    #filter_backends = (filters.SearchFilter,)
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
    filter_class = PazienteFilter
    #filter_fields = ('nome', 'cognome','sesso', 'data_nascita')
    search_fields = ('nome', 'cognome')

    def perform_create(self, serializer):
        owner = User.objects.get(pk=1)
        serializer.save(owner=owner)
        #serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Paziente.objects.all()


# /pazienti/{paziente}
class PazienteDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    queryset = Paziente.objects.all()
    serializer_class = PazienteDetailSerializer


# /pazienti/{paziente}/visite
class VisitaList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = VisitaSerializer

    def get_paziente_id(self):
        return self.kwargs.get('pk', None)

    def get_queryset(self):
        return Paziente.objects.visitePerPaziente(self.get_paziente_id())


# /visite/{paziente}/{id_visita}
class VisitaDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    serializer_class = VisitaDetailSerializer

    def get_paziente_id(self):
        return self.kwargs.get('paziente_pk', None)

    def get_visita_id(self):
        return self.kwargs.get('pk', None)

    def get_object(self):
        obj = get_object_or_404(Visita, pk=self.get_visita_id(), paziente_id=self.get_paziente_id())
        return obj