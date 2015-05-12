from django.conf.urls import url

from .views import CursoListView, CursoCreateView, CursoUpdateView

urlpatterns = [
	url(r'^$', CursoListView.as_view(), name='cursos_list'),
	url(r'^new_curso', CursoCreateView.as_view(), name='curso_create'),
	url(r'^curso_update/(?P<pk>\d+)$', CursoUpdateView.as_view(), name='curso_update')
]