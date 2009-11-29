from django.conf.urls.defaults import *

urlpatterns = patterns('speaking.views',
    url('^$', 'index', name='speaking-index'),
)
                       
