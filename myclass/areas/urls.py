from django.conf.urls import url

from .views import AreaListView, AreaCreateView, AreaUpdateView

urlpatterns = [
	url(r'^$', AreaListView.as_view(), name='areas_list'),
	url(r'^new_area', AreaCreateView.as_view(), name='area_create'),
	url(r'^area_update/(?P<pk>\d+)$', AreaUpdateView.as_view(), name='area_update'),
	# url(r'^nova/$', views.nova, name='nova_area'),
	# url(r'^salvar/(?P<id>\d+)/$', views.salvar, name='salvar_area'),
	# url(r'^lista/$', views.lista, name='lista_areas'),
	# url(r'^editar/(?P<area_id>\d+)/$', views.editar, name='editar_area'),
	# url(r'^excluir/(?P<area_id>\d+)/$', views.excluir, name='excluir_area')
]