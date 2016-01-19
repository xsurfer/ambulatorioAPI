from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics
from anagrafica.models import Paziente

from .serializers import VisitaSerializer, VisitaDetailSerializer
from .models import Visita


# /pazienti/{paziente}/visite
class VisitaList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = VisitaSerializer

    def get_paziente_id(self):
        return self.kwargs.get('pk', None)

    def perform_create(self, serializer):
        owner = User.objects.get(pk=1)
        paziente = Paziente.objects.get(pk=self.get_paziente_id())
        serializer.save(owner=owner, paziente=paziente)
        #serializer.save(owner=self.request.user)

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