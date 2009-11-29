from django.conf.urls.defaults import *

urlpatterns = patterns('codingrepo.views',
    url('^(?P<slug>[-\w]+)', 'detail', name='code-detail'),
    url('^$', 'index', name='code-index'),
)
