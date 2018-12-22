from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from cre_ode_app.models import DiffEq
#from scripy.integrate import odeint




# Create your views here.
class DiffEqCreateView(CreateView):
    model = DiffEq
    fields = ['lhs']
    success_url = reverse_lazy('cre_ode_app_create')

class DiffEqDetailView(DetailView):
    model = DiffEq
    fields = ['rhs']
    #success_url =
