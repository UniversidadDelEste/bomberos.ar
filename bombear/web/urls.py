from django.conf.urls import patterns, url
from . import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
]
