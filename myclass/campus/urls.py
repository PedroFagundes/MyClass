# coding utf-8

from django.conf.urls import url

from .views import CampusListView, CampusCreateView, CampusUpdateView


urlpatterns = [
	url(r'^$', CampusListView.as_view(), name='campus_list'),
	url(r'^new_campus', CampusCreateView.as_view(), name='campus_create'),
	url(r'^campus_update/(?P<pk>\d+)$', CampusUpdateView.as_view(), name='campus_update')
]