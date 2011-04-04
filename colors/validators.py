import re

from django.core.validators import RegexValidator
from django.utils.translation import ugettext as _

class HexColorCodeValidator(RegexValidator):
	regex = re.compile(r'([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})')
	message = _(u"Enter a valid hex color code.")