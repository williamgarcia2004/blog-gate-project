from django.core.validators import RegexValidator

validar_title = RegexValidator(
    regex=r"^.{10,150}$",
    message="El formato del título no es válido"
)