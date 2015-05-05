from django.contrib import admin
from personal.models import (
    FichaMedica,
    Bombero,
)

# Register your models here.
admin.site.register(Bombero)
admin.site.register(FichaMedica)
