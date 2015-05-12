from django.shortcuts import render
from django.views.generic import ListView, CreateView,UpdateView
from django.core.urlresolvers import reverse_lazy

from .models import Materias


class MateriaListView(ListView):
	model = Materias
	fields = '__all__'
	context_object_name = 'materias'
	template_name = 'materias/materias_list.html'

class MateriaCreateView(CreateView):
	model = Materias
	field = '__all__'
	success_url = reverse_lazy('materias_list')

class MateriaUpdateView(UpdateView):
	model = Materias
	fields = '__all__'
	success_url = reverse_lazy('materias_list')