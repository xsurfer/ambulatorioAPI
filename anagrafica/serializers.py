from rest_framework import serializers

from anagrafica.fields import ITSocialSecurityNumberField
from .models import Paziente
from visite.relations import VisiteCustomHyperlinkedIdentityField


class PazienteSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    paziente_url = serializers.HyperlinkedIdentityField(view_name='pazienti-detail')

    class Meta:
        model = Paziente
        fields = (
            'id', 'nome', 'cognome', 'sesso', 'data_nascita', 'paziente_url')


class PazienteDetailSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    codice_fiscale = ITSocialSecurityNumberField()
    # visite = VisiteCustomHyperlinkedRelatedField(many=True, view_name='visite-detail')
    paziente_url = serializers.HyperlinkedIdentityField(view_name='pazienti-detail')
    visite_url = serializers.HyperlinkedIdentityField(view_name='visite-list')

    class Meta:
        model = Paziente
        fields = (
            'id', 'nome', 'cognome', 'sesso', 'codice_fiscale', 'data_nascita', 'nazionalita', 'indirizzo_residenza', 'comune_residenza',
            'telefono', 'cellulare', 'email', 'profilo', 'esenzioni' , 'owner', 'visite_url', 'paziente_url')

