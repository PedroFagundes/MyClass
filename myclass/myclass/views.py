from django.shortcuts import render
from django.contrib.auth import logout
from django.views.generic import TemplateView


class Login(TemplateView):
	template_name = 'homesite/registration/login.html'

class Home(TemplateView):
	template_name = 'homesite/home.html'