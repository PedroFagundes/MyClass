from django.conf.urls import url

from .views import AreaListView, AreaCreateView, AreaUpdateView

urlpatterns = [
	url(r'^$', AreaListView.as_view(), name='areas_list'),
	url(r'^new_area', AreaCreateView.as_view(), name='area_create'),
	url(r'^area_update/(?P<pk>\d+)$', AreaUpdateView.as_view(), name='area_update'),
]