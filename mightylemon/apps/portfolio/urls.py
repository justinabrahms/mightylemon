from django.conf.urls.defaults import *

urlpatterns = patterns('portfolio.views',
    url('^$', 'index', name='portfolio-index'),
    # not used in this iteration
    # url('technology/(?P<technology_slug>[-\w]+)', 'by_technology', name='portfolio-bytech'),
    # url('(?P<project_slug>[-\w]+)', 'project', name='portfolio-project'),
)
                       
