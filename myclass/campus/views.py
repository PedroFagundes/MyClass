# coding: utf-8

from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

from .models import Campus


class CampusListView(ListView):
	model = Campus
	fields = '__all__'
	context_object_name = 'campuss'
	template_name = 'campus/campus_list.html'

class CampusCreateView(CreateView):
	model = Campus
	fields = '__all__'
	success_url = reverse_lazy('campus_list')

class CampusUpdateView(UpdateView):
	model = Campus
	fields = '__all__'
	success_url = reverse_lazy('campus_list')