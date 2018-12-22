from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
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
    pk_url_kwarg = "id"

    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        return HttpResponse("override something")
    #success_url =

class DiffEqListView(ListView):
    model = DiffEq
    
