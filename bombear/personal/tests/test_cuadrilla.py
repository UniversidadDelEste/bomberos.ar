from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from cuadrilla.models import Bombero
from cuadrilla.tests.utils import create_user


class BomberoDetailViewTest(TestCase):

    def setUp(self):
        self.username = 'John'
        self.password = 'Doe'
        self.email = 'john@doe.com'
        self.user = create_user(self.username, self.password, self.email)
        self.obj = Bombero.objects.create(
            fecha_de_nacimiento="1988-03-18",
            fecha_de_ingreso="2014-10-10",
            edad=23
        )
        self.client = Client()

    def test_bombero_detail_view(self):
        """Nuevo bombero"""

        # No estamos logueados, entonces no podemos ver el detalle del bombero
        response = self.client.get(
            reverse("bombero_view", args=[self.obj.id]),
            follow=True)
        assert "account/login.html" in [
            template.name for template in response.templates
        ]

        # Nos logueamos y podemos ver el detalle del bombero
        self.client.login(
            username=self.username,
            password=self.password
        )
        response = self.client.get(
            reverse("bombero_view", args=[self.obj.id]),
            follow=True)
        assert "cuadrilla/bombero_detail.html" in [
            template.name for template in response.templates
        ]

    def tearDown(self):
        Bombero.objects.all().delete()
