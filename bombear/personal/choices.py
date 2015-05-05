from django.utils.translation import ugettext_lazy as _


ESTADO_CIVIL_ES_AR = (
    ('', _('')),
    ('VIUDO', _('VIUDO')),
    ('SOLTERO', _('SOLTERO')),
    ('CASADO', _('CASADO')),
    ('DIVORCIADO', _('DIVORCIADO')),
    ('CONCUBINATO', _('CONCUBINATO')),
)


JERARQUIAS_ES_AR = (
    ('COMANDANTE GENERAL', _('COMANDANTE GENERAL')),
    ('COMANDANTE MAYOR', _('COMANDANTE MAYOR')),
    ('COMANDANTE', _('COMANDANTE')),
    ('OFICIAL 1', _('OFICIAL 1')),
    ('OFICIAL 2', _('OFICIAL 2')),
    ('OFICIAL 3', _('OFICIAL 3')),
    ('SUBOFICIAL MAYOR', _('SUBOFICIAL MAYOR')),
    ('SUBOFICIAL PRINCIPAL', _('SUBOFICIAL PRINCIPAL')),
    ('SARGENTO', _('SARGENTO')),
    ('CABO 1', _('CABO 1')),
    ('CABO', _('CABO')),
    ('BOMBERO', _('BOMBERO')),
    ('CADETE', _('CADETE')),
    ('ASPIRANTE', _('ASPIRANTE')),
    ('MASCOTA', _('MASCOTA')),
)


CARGOS_ES_AR = (
    ('JEFE', _('JEFE')),
    ('2 JEFE', _('2 JEFE')),
    ('OFICIALES JEFE', _('OFICIALES JEFE')),
    ('OFICIALES SUPERIORES', _('OFICIALES SUPERIORES')),
    ('SUBOFICIALES SUPERIORES', _('SUBOFICIALES SUPERIORES')),
    ('SUBOFICIALES SUBALTERNOS', _('SUBOFICIALES SUBALTERNOS')),
    ('BOMBERO', _('BOMBERO')),
    ('CADETES', _('CADETES')),
)


ESTADOS_ES_AR = (
    ('CUERPO ACTIVO', _('CUERPO ACTIVO')),
    ('CUERPO DE RESERVA', _('CUERPO DE RESERVA')),
    ('COMISION DIRECTIVA', _('COMISION DIRECTIVA')),
    ('PENSIONADO', _('PENSIONADO')),
)

ESPECIALIDADES_ES_AR = (
    ('CHOFER', _('CHOFER')),
    ('MAQUINISTA', _('MAQUINISTA')),
    ('ALTURA', _('ALTURA')),
    ('PRIMEROS AUXILIOS', _('PRIMEROS AUXILIOS')),
    ('FOURRIEL', _('FOURRIEL')),
    ('ADMINISTRATIVO', _('ADMINISTRATIVO')),
    ('MAT-PEL', _('MAT-PEL')),
    ('RADIO OPERADOR', _('RADIO OPERADOR')),
    ('BUSO', _('BUSO')),
)

TIPO_CHOFER_ES_AR = (
    ('NO', _('NO')),
    ('VEHICULOS LIVIANOS', _('VEHICULOS LIVIANOS')),
    ('TODOS', _('TODOS')),
)

TIPO_DOCUMENTO_ES_AR = (
    ('DNI', _('DNI')),
    ('PASAPORTE', _('PASAPORTE')),
    ('LIBRETA CIVICA', _('LIBRETA CIVICA')),
)

BOOL_ES_AR = (
    (True, 'SI'),
    (False, 'NO'),
)

GRUPO_SANGUINEO = (
    ('', 'Grupo Saguineo'),
    ('AB', 'Grupo AB'),
    ('A', 'Grupo A'),
    ('B', 'Grupo B'),
    ('O', 'Grupo O')
)

FACTOR_SANGUINEO = (
    ('', 'Factor Saguineo'),
    ('RH+', 'RH+'),
    ('RH-', 'RH-')
)
