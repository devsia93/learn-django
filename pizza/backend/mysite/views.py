from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .utils import *
from .forms import *


class PizzaCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model = Pizza
    model_form = PizzaForm
    template = 'mysite/pizza_create_form.html'
    raise_exception = True


class PizzaDetail(ObjectDetailMixin, View):
    model = Pizza
    template = 'mysite/pizza_detail.html'


class PizzaUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Pizza
    model_form = PizzaForm
    template = 'mysite/pizza_update_form.html'
    raise_exception = True


class PizzaDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Pizza
    redirect_url = 'pizzes_list_url'
    template = 'mysite/pizza_delete_form.html'
    raise_exception = True


def pizzes_list(request):
    pizzes = Pizza.objects.all()
    return render(request, 'mysite/index.html', context={'pizzes': pizzes})


class TopingCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model = Toping
    model_form = TopingForm
    template = 'mysite/toping_create_form.html'
    raise_exception = True


class TopingDetail(ObjectDetailMixin, View):
    model = Toping
    template = 'mysite/toping_detail.html'


class TopingUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Toping
    model_form = TopingForm
    template = 'mysite/toping_update_form.html'
    raise_exception = True


class TopingDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Toping
    redirect_url = 'topings_list_url'
    template = 'mysite/toping_delete_form.html'
    raise_exception = True
