from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'del_proj.views.index', name='home'),
                       url(r'^delete/(?P<pk>\d+)$', 'delete.views.delete', name='delete'),
                       url(r'^admin/', include(admin.site.urls)),
)
