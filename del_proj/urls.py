from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'del_proj.views.home', name='home'),
                       url(r'^delete/(?P<pk>\d+)$', include('delete.urls')),
                       url(r'^admin/', include(admin.site.urls)),
)
