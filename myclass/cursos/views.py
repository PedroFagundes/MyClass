from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

from .models import Cursos


class CursoListView(ListView):
	model = Cursos
	fields = '__all__'
	context_object_name = 'cursos'
	template_name = 'cursos/cursos_list.html'

class CursoCreateView(CreateView):
	model = Cursos
	fields = '__all__'
	success_url = reverse_lazy('cursos_list')

class CursoUpdateView(UpdateView):
	model = Cursos
	fields = '__all__'
	success_url = reverse_lazy('cursos_list')