from __future__ import unicode_literals
from django.core.validators import RegexValidator as _RegexValidator
import unicodedata
from django.utils import six


class AccentsAgnosticRegexValidator(_RegexValidator):
    """
    This validator performs a validation after normalizing the unicode
      string. This means: will validate as if the string value did not
      have accents in letters.
    """

    def __call__(self, value):
        return super(AccentsAgnosticRegexValidator, self).__call__(
            ''.join(c for c in unicodedata.normalize('NFD', six.text_type(value)) if unicodedata.category(c) != 'Mn')
        )


class NameRegexValidator(AccentsAgnosticRegexValidator):
    """
    This validator performs a validaron on written names / words, on any
      kind of alphabet which can be reduced to latin letters. Perhaps
      strange characters (e.g. greek, cyrillic) can be "normalized" to
      latin letters, and so such characters will count as valid instead
      of bust.
    """

    MODE_ONLY_LETTERS = 0
    MODE_ACCEPT_NUMBERS = 1
    MODE_ALPHANUMERIC = 2
    MODE_ALPHANUMERIC_EXTENDED = 3

    def __init__(self, mode=MODE_ONLY_LETTERS, *args, **kwargs):
        try:
            super(NameRegexValidator, self).__init__([
                r'^\s*[A-Za-z]+(\'[A-Za-z]+)?(\s+[A-Za-z]+(\'[A-Za-z]+)?)*\s*$',
                r'^\s*([A-Za-z]+(\'[A-Za-z]+)?|\d+)(\s+([A-Za-z]+(\'[A-Za-z]+)?|\d+))*\s*$',
                r'^\s*[A-Za-z0-9]+(\'[A-Za-z0-9]+)?(\s+[A-Za-z0-9]+(\'[A-Za-z0-9]+)?)*\s*$',
                r'^\s*[A-Za-z0-9-]+(\'[A-Za-z0-9-]+)?(\s+[A-Za-z0-9-]+(\'[A-Za-z0-9-]+)?)*\s*$'
            ][mode], *args, **kwargs)
        except IndexError:
            raise ValueError('An invalid mode value (i.e. not in the 0-3 range) was assigned to NameRegexValidator')