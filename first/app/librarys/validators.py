import re
from django.core.exceptions import ValidationError


def validation_librarys_address(librarys_address):
    if re.fullmatch(r'[A-ZА-ЯЁ0-9!?:-].*', librarys_address):
        return librarys_address
    else:
        raise ValidationError(
            message="не соответствует требованиям: (Россия, гор., ул., дом)"
        )


def validation_librarys_name(librarys_name):
    if re.fullmatch(r'[A-ZА-ЯЁ0-9!?:-].*', librarys_name):
        return librarys_name
    else:
        raise ValidationError(
            message="не соответствует требованиям: (A-ZА-ЯЁ0-9!?:-)"
        )
