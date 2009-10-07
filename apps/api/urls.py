from django.conf import settings
from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import BlogPostHandler

blogpost_handler = Resource(BlogPostHandler)

urlpatterns = patterns('',
    url('posts/(?P<post_slug>[-\w]+)/$', blogpost_handler, {'emitter_format':'xml'}),
    url('posts/$', blogpost_handler, {'emitter_format':'xml'}),
)
                        
