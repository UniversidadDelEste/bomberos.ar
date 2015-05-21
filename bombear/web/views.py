from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    """Homepage del sitio de bomberos."""

    template_name = "web/home.html"
