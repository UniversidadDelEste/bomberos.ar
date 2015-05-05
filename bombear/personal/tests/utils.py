from django.contrib.auth.models import User
from cuadrilla.models import Bombero
import random
import string


def create_user(username='John', password='Doe', email='john@doe.com'):
    """Returns a user instance."""
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password)
    return user


def create_randstr(length, only_digits=False):
    """Returns a random string with the given length."""
    length = int(length)
    string_group = string.ascii_lowercase
    if only_digits is True:
        string_group = string.digits
    return ''.join(random.choice(string_group) for _ in range(length))


def create_bombero_test():
    """Returns a firefighter test object with random data."""
    bombero = Bombero.objects.create(
        nombre=create_randstr(10),
        apellido=create_randstr(13),
        documento=create_randstr(6, only_digits=True),
        tipo_de_documento='DNI',
        jerarquia='CABO',
        cargo='BOMBERO',
        estado='CUERPO ACTIVO',
        domicilio=create_randstr(9) + ' ' + create_randstr(4, only_digits=True),
        especialidad='FOURRIEL',
        ocupacion=create_randstr(21),
        oficio=create_randstr(20),
        grupo_sanguineo=create_randstr('5'),
        telefono_celular=create_randstr(8, only_digits=True),
        telefono_particular=create_randstr(6, only_digits=True),
        telefono_trabajo=create_randstr(8, only_digits=True),
        numero_del_hamdy=create_randstr(3, only_digits=True),
        estado_civil=create_randstr(5),
        capacitaciones=create_randstr(200),
        estudios=create_randstr(200),
        alergias=create_randstr(200),
        vacunas=create_randstr(200),
        pencionado=bool(random.randint(0, 1)),
        carnet_conducir=bool(random.randint(0, 1)),
        conductor_nautico=bool(random.randint(0, 1)),
        chofer=bool(random.randint(0, 1)),
        vencimiento_carnet_conducir="2030-03-18",
        fecha_de_nacimiento="1988-03-18",
        fecha_de_ingreso="2014-10-10",
        edad=23,
        hijos=create_randstr(1, only_digits=True),
        antiguedad=create_randstr(1, only_digits=True),
        numero_de_ioma=create_randstr(6, only_digits=True),
    )
    return bombero


def create_multiples_bomberos(length, verbose=False):
    """Create a lot of bomberos for test purposes."""
    counter = 0
    while counter <= length:
        bombero = create_bombero_test()
        if verbose:
            print('Bombero creado: {0} {1}'.format(
                bombero.nombre, bombero.apellido)
            )
        counter += 1
