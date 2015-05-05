# from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy
from cuadrilla.forms import (
    BomberoForm,
)
from cuadrilla.models import Bombero
from django_filters.views import FilterView
import django_filters


class BomberoCreate(CreateView):
    model = Bombero
    form_class = BomberoForm


class BomberoDetail(DetailView):
    model = Bombero
    context_object_name = "bombero"


class BomberoUpdate(UpdateView):
    model = Bombero
    form_class = BomberoForm
    success_url = reverse_lazy("bombero_list")


class BomberoDelete(DeleteView):
    model = Bombero
    form_class = BomberoForm


class BomberoList(ListView):
    model = Bombero
    context_object_name = "bombero_list"
    paginate_by = 20


class BomberoFilterSet(django_filters.FilterSet):

    class Meta:
        model = Bombero
        fields = {
            'estado': ['icontains'],
            'nombre': ['icontains'],
            'apellido': ['icontains'],
        }


class BomberoListFilter(FilterView):
    model = Bombero
    filterset_class = BomberoFilterSet
    paginate_by = 20
    context_object_name = "bombero_list"
