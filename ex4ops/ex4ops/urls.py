from django.conf.urls import patterns, include, url
from monitor import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ex4ops.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'passive$',views.passive),
    url(r'regip$',views.regip),
    url(r'regipbatch',views.regipbatch),
)
