from django.shortcuts import render
from django.contrib.auth import logout
from django.views.generic import TemplateView


class HomeSiteView(TemplateView):
	template_name = 'homesite/registration/login.html'