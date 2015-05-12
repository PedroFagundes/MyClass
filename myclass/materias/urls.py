from django.conf.urls import url

from .views import MateriaListView, MateriaCreateView, MateriaUpdateView


urlpatterns = [
	url(r'^$', MateriaListView.as_view(), name='materias_list'),
	url(r'^new_materia', MateriaCreateView.as_view(), name='materia_create'),
	url(r'^materia_update/(?P<pk>\d+)$', MateriaUpdateView.as_view(), name='materia_update')
]