from rest_framework import serializers
from .relations import VisiteCustomHyperlinkedRelatedField, VisiteCustomHyperlinkedIdentityField
from .models import Paziente, Visita


class PazienteSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    paziente_url = serializers.HyperlinkedIdentityField(view_name='pazienti-detail')

    class Meta:
        model = Paziente
        fields = (
            'id', 'nome', 'cognome', 'sesso', 'data_nascita', 'paziente_url')


class PazienteDetailSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # visite = VisiteCustomHyperlinkedRelatedField(many=True, view_name='visite-detail')
    paziente_url = serializers.HyperlinkedIdentityField(view_name='pazienti-detail')
    visite_url = serializers.HyperlinkedIdentityField(view_name='visite-list')

    class Meta:
        model = Paziente
        fields = (
            'id', 'nome', 'cognome', 'sesso', 'data_nascita', 'nazionalita', 'indirizzo_residenza', 'comune_residenza',
            'telefono', 'cellulare', 'email', 'profilo', 'owner', 'visite_url', 'paziente_url')


class VisitaSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    paziente_url = serializers.HyperlinkedIdentityField(view_name='pazienti-detail')
    visita_url = VisiteCustomHyperlinkedIdentityField(view_name='visite-detail', read_only=False)

    class Meta:
        model = Visita
        fields = ('id', 'data_visita', 'owner', 'paziente_url', 'visita_url')


class VisitaDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    paziente_url = serializers.HyperlinkedIdentityField(view_name='pazienti-detail')
    visita_url = VisiteCustomHyperlinkedIdentityField(view_name='visite-detail', read_only=False)

    class Meta:
        model = Visita
        fields = ('id', 'anamnesi', 'esame_obiettivo', 'esame_strumentale', 'diagnosi', 'terapia', 'owner',
                  'data_visita', 'paziente_url', 'visita_url')
