from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'main.views.index', name='index'),
    url(r'^grupos$', 'main.views.grupos', name='grupos'),
    url(r'^grupos/grupo/(?P<grupo_id>\d+)/$', 'main.views.grupo_detalle', name='grupo'),
    url(r'^persona/(?P<persona_id>\d+)/(?P<grupo_id>\d+)/(?P<tipo>\w+)/$', 'main.views.persona_detalle', name='persona'),
)