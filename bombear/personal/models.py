#-*- encoding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.utils.encoding import python_2_unicode_compatible
from .choices import (
    GRUPO_SANGUINEO, FACTOR_SANGUINEO,
    CARGOS_ES_AR, ESTADOS_ES_AR,
    JERARQUIAS_ES_AR, TIPO_DOCUMENTO_ES_AR,
    ESPECIALIDADES_ES_AR, ESTADO_CIVIL_ES_AR,
)
from datetime import date
import os


@python_2_unicode_compatible
class Bombero(models.Model):
    nombre = models.CharField(
        max_length=255,
        verbose_name=_('Nombre'))
    apellido = models.CharField(
        max_length=255,
        verbose_name=_('Apellido'))
    documento = models.CharField(
        max_length=255,
        verbose_name=_('Numero de documento'))
    tipo_de_documento = models.CharField(
        choices=TIPO_DOCUMENTO_ES_AR,
        max_length=255,
        verbose_name=_('Tipo de documento'))
    jerarquia = models.CharField(
        choices=JERARQUIAS_ES_AR,
        max_length=255,
        verbose_name=_('Jerarquia'))
    cargo = models.CharField(
        choices=CARGOS_ES_AR,
        max_length=255,
        verbose_name=_('Cargo'))
    estado = models.CharField(
        choices=ESTADOS_ES_AR,
        max_length=255,
        verbose_name=_('Estado'))
    domicilio = models.CharField(
        max_length=255,
        verbose_name=_('Domicilio'))
    especialidad = models.CharField(
        choices=ESPECIALIDADES_ES_AR,
        max_length=255,
        verbose_name=_('Especialidad'))
    ocupacion = models.CharField(
        max_length=255,
        verbose_name=_('Ocupacion actual'))
    oficio = models.CharField(
        max_length=255,
        verbose_name=_('Oficio'))
    telefono_celular = models.CharField(
        max_length=255,
        verbose_name=_('Telefono celular'))
    telefono_particular = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Telefono particular'))
    telefono_trabajo = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Telefono del trabajo'))
    numero_del_hamdy = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Numero del Handy'))
    estado_civil = models.CharField(
        choices=ESTADO_CIVIL_ES_AR,
        max_length=255,
        verbose_name=_('Estado civil'))
    capacitaciones = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Cursos realizados'))
    estudios = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Estudios realizados'))
    pencionado = models.BooleanField(
        default=False,
        verbose_name=_('Pensionado')
    )
    carnet_conducir = models.BooleanField(
        default=False,
        verbose_name=_('Carnet de conducir')
    )
    conductor_nautico = models.BooleanField(
        default=False,
        verbose_name=_('Conductor nautico')
    )
    chofer = models.BooleanField(
        default=False,
        verbose_name=_('Chofer')
    )
    vencimiento_carnet_conducir = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('Vencimiento del carnet de conducir')
    )
    fecha_de_nacimiento = models.DateField(
        verbose_name=_('Fecha de nacimiento')
    )
    fecha_de_ingreso = models.DateField(
        verbose_name=_('Fecha de ingreso')
    )
    hijos = models.IntegerField(
        default=0,
        verbose_name=_('Hijos')
    )
    antiguedad = models.IntegerField(
        default=0,
        verbose_name=_('Antiguedad')
    )
    numero_de_ioma = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('Numero de IOMA')
    )
    foto = models.ImageField(upload_to=".", null=True, blank=True)

    @property
    def edad(self):
        delta = date.today() - self.fecha_de_nacimiento
        return int((delta.days / (365.2425)))

    @property
    def es_chofer(self):
        if self.carnet_conducir:
            delta_days = (
                self.vencimiento_carnet_conducir - date.today()
            ).days
            if delta_days > 1:  # Si el carnet vence maniana
                return True
        return False

    def get_absolute_url(self):
        return reverse('bombero_view', args=[self.id])

    def foto_default(self):
        foto = self.foto
        if foto and hasattr(foto, 'url'):
            return foto
        else:
            return os.path.join(
                settings.STATIC_URL,
                'cuadrilla/imgs/firefighter_icon.jpg'
            )

    class Meta:
        ordering = ['apellido']

    @property
    def nombre_completo(self):
        return "{0}, {1}".format(self.apellido, self.nombre)

    @property
    def dni(self):
        return "{0} {1}".format(self.tipo_de_documento, self.documento)

    def __str__(self):
        return "{0}, {1}".format(self.apellido, self.nombre)


@python_2_unicode_compatible
class FichaMedica(models.Model):
    """Historial medico de un bombero."""

    bombero = models.OneToOneField(Bombero)
    grupo_sanguineo = models.CharField(
        max_length=255,
        choices=GRUPO_SANGUINEO,
        verbose_name=_('Grupo sanguineo'))
    factor_sanguineo = models.CharField(
        max_length=255,
        choices=FACTOR_SANGUINEO,
        verbose_name=_('Factor sanguineo'))
    vacunas = models.TextField(
        blank=True,
        default="",
        verbose_name=_('Vacunas'))
    alergias = models.TextField(
        null=True,
        blank=True,
        default="",
        verbose_name=_('Alergias'))
    otros_antecedentes = models.TextField(
        null=True,
        blank=True,
        default="",
        verbose_name=_('Otros antecedentes'))

    class Meta:
        verbose_name_plural = 'Fichas Medicas'

    def __str__(self):
        bombero = "Ficha medica de {0} {1}".format(
            self.bombero.apellido, self.bombero.nombre)
        return "{0}".format(bombero)


@python_2_unicode_compatible
class Experiencia(models.Model):
    """Experiencia de un bombero."""

    bombero = models.ForeignKey(Bombero, related_name="experiencias")
    desde = models.DateField()
    hasta = models.DateField()
    lugar = models.CharField(max_length=255, default="")

    class Meta:
        verbose_name_plural = 'Años de Experiencia'

    def __str__(self):
        experiencia = "{0} - Experiencia desde {1} hasta {2}".format(
            self.bombero, self.desde, self.hasta)
        return "{0}".format(experiencia)


@python_2_unicode_compatible
class Familiar(models.Model):
    """Experiencia de un bombero."""

    bombero = models.ForeignKey(Bombero, related_name="familiares")
    parentesco = models.CharField(max_length=255)
    nombre = models.CharField(
        max_length=255,
        verbose_name=_('Nombre'))
    apellido = models.CharField(
        max_length=255,
        verbose_name=_('Apellido'))
    edad = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Edad'))
    otros_datos = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Familiares"

    @property
    def nombre_completo(self):
        return "{0}, {1}".format(self.apellido, self.nombre)

    def __str__(self):
        return "{0} {1} {2} de {3} {4}".format(
            self.nombre, self.apellido, self.parentesco,
            self.bombero.nombre, self.bombero.apellido)
