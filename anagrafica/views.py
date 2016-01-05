from django.shortcuts import get_object_or_404
import django_filters

from rest_framework import generics, permissions, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .permissions import IsOwnerOrReadOnly

from .serializers import PazienteSerializer, VisitaSerializer, PazienteDetailSerializer, VisitaDetailSerializer
from .models import Paziente, Visita


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'pazienti': reverse('pazienti-list', request=request, format=format),
    })


# /pazienti/
class PazienteList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    # queryset = Paziente.objects.all()
    serializer_class = PazienteSerializer
    # filter_class = PazienteFilter
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nome', 'cognome')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Paziente.objects.all()


# /pazienti/{paziente}
class PazienteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    queryset = Paziente.objects.all()
    serializer_class = PazienteDetailSerializer


# /pazienti/{paziente}/visite
class VisitaList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    # queryset = get_queryset()
    serializer_class = VisitaSerializer

    def get_paziente_id(self):
        return self.kwargs.get('pk', None)

    def perform_create(self, serializer):
        id = self.get_paziente_id()
        paziente = Paziente.objects.get(id)
        serializer.save(owner=self.request.user, paziente=paziente)

    def get_queryset(self):
        return Visita.objects.perPaziente(self.get_paziente_id())


# /visite/{paziente}/{id_visita}
class VisitaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    serializer_class = VisitaDetailSerializer

    def get_paziente_id(self):
        return self.kwargs.get('paziente_pk', None)

    def get_visita_id(self):
        return self.kwargs.get('pk', None)

    def get_object(self):
        obj = get_object_or_404(Visita, pk=self.get_visita_id(), paziente_id=self.get_paziente_id())
        # obj = Visita.visite.perPazienteVisita(paziente_id=self.get_paziente_id(),
        #                                      visita_id=self.get_visita_id()).get_object_or_404()
        print(obj.paziente.nome)
        return obj
