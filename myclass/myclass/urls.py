from django.conf.urls import patterns, include, url
from django.contrib import admin


from .views import Login, Home

urlpatterns = [
    # Examples:
    # url(r'^$', 'myclass.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', Login.as_view()),
    url(r'^home/$', Home.as_view(), name='home'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^admin/', include(admin.site.urls)),

	url(r'^areas/', include('areas.urls'), name = 'areas'),
	url(r'^campus/', include('campus.urls'), name = 'campus'),
	url(r'^cursos/', include('cursos.urls'), name = 'cursos'),
    url(r'^materias/', include('materias.urls'), name='materias')
]