from piston.handler import BaseHandler, AnonymousBaseHandler
from django.shortcuts import get_object_or_404
from blog.models import Post

class AnonBlogPostHandler(AnonymousBaseHandler):
    model = Post
    fields = ('title', 'body', 'tags', 'pub_date')

class BlogPostHandler(BaseHandler):
    model = Post
    allowed_methods = ('GET',)
    exclude = ('id','enable_comments','markup_type','create_date', 'permalink')
    anonymous = AnonBlogPostHandler

    def list(self, request):
        obj_list = Post.objects.filter(active=True)
        return obj_list

    def read(self, request, **kwargs):
        if kwargs.get('post_slug', None):
            post = get_object_or_404(Post, slug=post_slug, active=True)
            return post
        else:
            return Post.objects.filter(active=True)

