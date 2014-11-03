from django.conf.urls import patterns, include, url
from monitor import views

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'passive$',views.passive),
)
