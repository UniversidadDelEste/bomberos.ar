from django import forms
from cuadrilla import choices
from cuadrilla.models import Bombero
from django.utils.translation import ugettext_lazy as _
from django_summernote.widgets import SummernoteWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, Column


class BomberoForm(forms.ModelForm):

    tipo_de_documento = forms.CharField(
        label="",
        widget=forms.Select(choices=choices.TIPO_DOCUMENTO_ES_AR,
                            )
    )
    jerarquia = forms.CharField(
        label="",
        widget=forms.Select(choices=choices.JERARQUIAS_ES_AR,
                            )
    )
    cargo = forms.CharField(
        label="",
        widget=forms.Select(choices=choices.CARGOS_ES_AR,
                            )
    )
    estado = forms.CharField(
        label="",
        widget=forms.Select(choices=choices.ESTADOS_ES_AR,
                            )
    )
    grupo_sanguineo = forms.CharField(
        label="",
        widget=forms.Select(choices=choices.GRUPO_SANGUINEO,
                            )
    )

    def __init__(self, *args, **kwargs):
        super(BomberoForm, self).__init__(*args, **kwargs)
        self.datos_personales = FormHelper(self)
        self.datos_personales.form_tag = False
        self.datos_personales.form_class = 'col s6'
        self.helper = FormHelper(self)
        self.helper.form_class = 'col s6'
        self.helper.form_tag = False

        self.datos_personales.layout = Layout(
            Column(
                Field('apellido'),
                css_class='col s6'
            ),
            Column(
                Field('nombre'),
                css_class='col s6'
            ),
            Row(
                Column(
                    Field('fecha_de_nacimiento'),
                    css_class='col s6'
                ),
                Column(
                    Field('edad'),
                    css_class='col s6'
                ),
            ),
            Row(
                Column(
                    Field('tipo_de_documento'),
                    css_class='col s6'
                ),
                Column(
                    Field('documento'),
                    css_class='col s6'
                ),
            ),
            Row(
                Column(
                    Field('foto'),
                    css_class='col s12'
                )
            ),
            Row(
                Column(
                    Field('domicilio'),
                    css_class='col s6'
                ),
            ),

            Row(
                Column(
                    Field('fecha_de_nacimiento'),
                ),
                Column(
                    Field('fecha_de_ingreso'),
                ),
            ),
            Row(
                Column(
                    Field('telefono_celular'),
                    css_class='col s6'
                ),
                Column(
                    Field('telefono_particular'),
                    css_class='col s6'
                ),
            ),
            Row(
                Column(
                    Field('telefono_trabajo'),
                    css_class='col s6'
                ),
                Column(
                    Field('numero_del_hamdy'),
                    css_class='col s6'
                ),
            ),
            Row(
                Column(
                    Field('oficio'),
                    css_class='col s6'
                ),
                Column(
                    Field('especialidad'),
                    css_class='col s6'
                ),
            ),
            Row(
                Column(
                    Field('ocupacion'),
                    css_class='col s6'
                ),
                Column(
                    Field('cargo'),
                    css_class='col s6'
                ),
            ),
            Row(
                Column(
                    Field('jerarquia'),
                    css_class='col s6'
                ),
                Column(
                    Field('estado'),
                    css_class='col s6'
                ),
            ),
            Row(
                Column(
                    Field('antiguedad'),
                    css_class='col s6'
                ),
            ),
            Row(
                Column(
                    Field('estado_civil'),
                    css_class='col s6'
                ),
                Column(
                    Field('hijos'),
                    css_class='col s6'
                ),
            ),
            Row(
                Column(
                    Field('estudios'),
                    css_class='col s6 force_span'
                ),
                Column(
                    Field('capacitaciones'),
                    css_class='col s6 force_span'
                ),
            ),
            Row(
                Column(
                    Field('vacunas'),
                    css_class='col s6 force_span'
                ),
                Column(
                    Field('alergias'),
                    css_class='col s6 force_span'
                ),
            ),
            Row(
                Column(
                    Field('grupo_sanguineo'),
                    css_class='col s6'
                ),
                Column(
                    Field('numero_de_ioma'),
                    css_class='col s6'
                ),
            ),
            Row(
                Column(
                    Field('carnet_conducir'),
                    css_class='col s6'
                ),
                Column(
                    Field('vencimiento_carnet_conducir'),
                    css_class='col s6'
                ),
            ),
            Row(
                Column(
                    Field('chofer'),
                    css_class='col s6'
                ),
                Column(
                    Field('conductor_nautico'),
                    css_class='col s6'
                ),
            ),
            Row(
                Column(
                    Field('pencionado'),
                    css_class='col s6'
                ),
            ),
        )

    class Meta:
        model = Bombero
        exclude = []
        widgets = {
            'estudios': SummernoteWidget(),
            'capacitaciones': SummernoteWidget(),
            'vacunas': SummernoteWidget(),
            'alergias': SummernoteWidget(),
        }
