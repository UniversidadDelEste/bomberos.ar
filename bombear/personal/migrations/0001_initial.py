# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bombero',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=255, verbose_name='Apellido')),
                ('documento', models.CharField(max_length=255, verbose_name='Numero de documento')),
                ('tipo_de_documento', models.CharField(max_length=255, verbose_name='Tipo de documento', choices=[('DNI', 'DNI'), ('PASAPORTE', 'PASAPORTE'), ('LIBRETA CIVICA', 'LIBRETA CIVICA')])),
                ('jerarquia', models.CharField(max_length=255, verbose_name='Jerarquia', choices=[('COMANDANTE GENERAL', 'COMANDANTE GENERAL'), ('COMANDANTE MAYOR', 'COMANDANTE MAYOR'), ('COMANDANTE', 'COMANDANTE'), ('OFICIAL 1', 'OFICIAL 1'), ('OFICIAL 2', 'OFICIAL 2'), ('OFICIAL 3', 'OFICIAL 3'), ('SUBOFICIAL MAYOR', 'SUBOFICIAL MAYOR'), ('SUBOFICIAL PRINCIPAL', 'SUBOFICIAL PRINCIPAL'), ('SARGENTO', 'SARGENTO'), ('CABO 1', 'CABO 1'), ('CABO', 'CABO'), ('BOMBERO', 'BOMBERO'), ('CADETE', 'CADETE'), ('ASPIRANTE', 'ASPIRANTE'), ('MASCOTA', 'MASCOTA')])),
                ('cargo', models.CharField(max_length=255, verbose_name='Cargo', choices=[('JEFE', 'JEFE'), ('2 JEFE', '2 JEFE'), ('OFICIALES JEFE', 'OFICIALES JEFE'), ('OFICIALES SUPERIORES', 'OFICIALES SUPERIORES'), ('SUBOFICIALES SUPERIORES', 'SUBOFICIALES SUPERIORES'), ('SUBOFICIALES SUBALTERNOS', 'SUBOFICIALES SUBALTERNOS'), ('BOMBERO', 'BOMBERO'), ('CADETES', 'CADETES')])),
                ('estado', models.CharField(max_length=255, verbose_name='Estado', choices=[('CUERPO ACTIVO', 'CUERPO ACTIVO'), ('CUERPO DE RESERVA', 'CUERPO DE RESERVA'), ('COMISION DIRECTIVA', 'COMISION DIRECTIVA'), ('PENSIONADO', 'PENSIONADO')])),
                ('domicilio', models.CharField(max_length=255, verbose_name='Domicilio')),
                ('especialidad', models.CharField(max_length=255, verbose_name='Especialidad', choices=[('CHOFER', 'CHOFER'), ('MAQUINISTA', 'MAQUINISTA'), ('ALTURA', 'ALTURA'), ('PRIMEROS AUXILIOS', 'PRIMEROS AUXILIOS'), ('FOURRIEL', 'FOURRIEL'), ('ADMINISTRATIVO', 'ADMINISTRATIVO'), ('MAT-PEL', 'MAT-PEL'), ('RADIO OPERADOR', 'RADIO OPERADOR'), ('BUSO', 'BUSO')])),
                ('ocupacion', models.CharField(max_length=255, verbose_name='Ocupacion actual')),
                ('oficio', models.CharField(max_length=255, verbose_name='Oficio')),
                ('telefono_celular', models.CharField(max_length=255, verbose_name='Telefono celular')),
                ('telefono_particular', models.CharField(max_length=255, blank=True, verbose_name='Telefono particular', null=True)),
                ('telefono_trabajo', models.CharField(max_length=255, blank=True, verbose_name='Telefono del trabajo', null=True)),
                ('numero_del_hamdy', models.CharField(max_length=255, blank=True, verbose_name='Numero del Handy', null=True)),
                ('estado_civil', models.CharField(max_length=255, verbose_name='Estado civil', choices=[('', ''), ('VIUDO', 'VIUDO'), ('SOLTERO', 'SOLTERO'), ('CASADO', 'CASADO'), ('DIVORCIADO', 'DIVORCIADO'), ('CONCUBINATO', 'CONCUBINATO')])),
                ('capacitaciones', models.TextField(blank=True, null=True, verbose_name='Cursos realizados')),
                ('estudios', models.TextField(blank=True, null=True, verbose_name='Estudios realizados')),
                ('pencionado', models.BooleanField(default=False, verbose_name='Pensionado')),
                ('carnet_conducir', models.BooleanField(default=False, verbose_name='Carnet de conducir')),
                ('conductor_nautico', models.BooleanField(default=False, verbose_name='Conductor nautico')),
                ('chofer', models.BooleanField(default=False, verbose_name='Chofer')),
                ('vencimiento_carnet_conducir', models.DateField(blank=True, null=True, verbose_name='Vencimiento del carnet de conducir')),
                ('fecha_de_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('fecha_de_ingreso', models.DateField(verbose_name='Fecha de ingreso')),
                ('hijos', models.IntegerField(default=0, verbose_name='Hijos')),
                ('antiguedad', models.IntegerField(default=0, verbose_name='Antiguedad')),
                ('numero_de_ioma', models.IntegerField(blank=True, null=True, verbose_name='Numero de IOMA')),
                ('foto', models.ImageField(upload_to='.', blank=True, null=True)),
            ],
            options={
                'ordering': ['apellido'],
            },
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('desde', models.DateField()),
                ('hasta', models.DateField()),
                ('lugar', models.CharField(max_length=255, default='')),
                ('bombero', models.ForeignKey(related_name='experiencias', to='personal.Bombero')),
            ],
            options={
                'verbose_name_plural': 'Años de Experiencia',
            },
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('parentesco', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=255, verbose_name='Apellido')),
                ('edad', models.CharField(max_length=255, blank=True, verbose_name='Edad', null=True)),
                ('otros_datos', models.TextField(blank=True, null=True)),
                ('bombero', models.ForeignKey(related_name='familiares', to='personal.Bombero')),
            ],
            options={
                'verbose_name_plural': 'Familiares',
            },
        ),
        migrations.CreateModel(
            name='FichaMedica',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('grupo_sanguineo', models.CharField(max_length=255, verbose_name='Grupo sanguineo', choices=[('', 'Grupo Saguineo'), ('AB', 'Grupo AB'), ('A', 'Grupo A'), ('B', 'Grupo B'), ('O', 'Grupo O')])),
                ('factor_sanguineo', models.CharField(max_length=255, verbose_name='Factor sanguineo', choices=[('', 'Factor Saguineo'), ('RH+', 'RH+'), ('RH-', 'RH-')])),
                ('vacunas', models.TextField(blank=True, default='', verbose_name='Vacunas')),
                ('alergias', models.TextField(blank=True, default='', verbose_name='Alergias', null=True)),
                ('otros_antecedentes', models.TextField(blank=True, default='', verbose_name='Otros antecedentes', null=True)),
                ('bombero', models.OneToOneField(to='personal.Bombero')),
            ],
            options={
                'verbose_name_plural': 'Fichas Medicas',
            },
        ),
    ]
