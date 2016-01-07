import re

from django.core.exceptions import ValidationError
from django.core.validators import EMPTY_VALUES
from localflavor.it.util import vat_number_validation, ssn_validation
from rest_framework.fields import RegexField
from django.utils.translation import ugettext_lazy as _


class ITSocialSecurityNumberField(RegexField):
    """
    A form field that validates Italian Tax code (codice fiscale) for both persons and entities.

    For reference see http://www.agenziaentrate.it/ and search for:

    * 'Informazioni sulla codificazione delle persone fisiche' for persons' SSN
    * 'Codice fiscale Modello AA5/6' for entities' SSN

    .. versionchanged:: 1.1

    The ``ITSocialSecurityNumberField`` now also accepts SSN values for
    entities (numeric-only form).
    """
    default_error_messages = {
        'invalid': _('Enter a valid Tax code.'),
    }

    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        super(ITSocialSecurityNumberField, self).__init__(r'^\w{3}\s*\w{3}\s*\w{5}\s*\w{5}$|\d{10}',
                                                          *args, **kwargs)

    def clean(self, value):
        value = super(ITSocialSecurityNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return ''
        value = re.sub('\s', '', value).upper()
        # Entities SSN are numeric-only
        if value.isdigit():
            try:
                return vat_number_validation(value)
            except ValueError:
                raise ValidationError(self.error_messages['invalid'])
        # Person SSN
        else:
            try:
                return ssn_validation(value)
            except (ValueError, IndexError):
                raise ValidationError(self.error_messages['invalid'])