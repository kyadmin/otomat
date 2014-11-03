from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kyadmin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/',include('management.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
