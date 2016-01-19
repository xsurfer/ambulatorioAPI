from rest_framework import serializers

from .relations import VisiteCustomHyperlinkedIdentityField, \
    PazientiCustomHyperlinkedIdentityField
from .models import Visita


class VisitaSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    paziente_url = PazientiCustomHyperlinkedIdentityField(view_name='pazienti-detail')
    visita_url = VisiteCustomHyperlinkedIdentityField(view_name='visite-detail', read_only=False)

    class Meta:
        model = Visita
        fields = ('id', 'data_visita', 'owner', 'paziente_url', 'visita_url')


class VisitaDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    paziente_url = PazientiCustomHyperlinkedIdentityField(view_name='pazienti-detail')
    visita_url = VisiteCustomHyperlinkedIdentityField(view_name='visite-detail', read_only=False)

    class Meta:
        model = Visita
        fields = ('id', 'anamnesi', 'esame_obiettivo', 'conclusioni', 'owner',
                  'data_visita', 'paziente_url', 'visita_url')
