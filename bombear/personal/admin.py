from django.contrib import admin
from personal.models import (
    FichaMedica,
    Experiencia,
    Familiar,
    Bombero,
)


class BomberoAdmin(admin.ModelAdmin):

    list_display = ('nombre_completo', 'dni', 'telefono_celular', 'especialidad', 'estado')
    search_fields = ('nombre', 'apellido', 'documento',
                     'domicilio', 'telefono_celular')
    list_filter = ('especialidad', 'jerarquia', 'chofer',)


class ExperienciaAdmin(admin.ModelAdmin):

    search_fields = ('bombero__nombre', 'bombero__apellido',
                     'bombero__documento',)


class FichaMedicaAdmin(admin.ModelAdmin):

    search_fields = ('bombero__nombre', 'bombero__apellido',
                     'bombero__documento',)


class FamiliarAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'parentesco', 'bombero')

    search_fields = ('bombero__nombre', 'bombero__apellido',
                     'bombero__documento',)


admin.site.register(Bombero, BomberoAdmin)
admin.site.register(Familiar, FamiliarAdmin)
admin.site.register(Experiencia, ExperienciaAdmin)
admin.site.register(FichaMedica, FichaMedicaAdmin)
