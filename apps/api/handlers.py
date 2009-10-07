from piston.handler import BaseHandler, AnonymousBaseHandler
from django.shortcuts import get_object_or_404
from blog.models import Post

class AnonBlogPostHandler(AnonymousBaseHandler):
    model = Post
    fields = ('post_url','tags','title','blog_title','published_on','slug')

class BlogPostHandler(BaseHandler):
    model = Post
    allowed_methods = ('GET',)
    exclude = ('id','enable_comments','markup_type','create_date', 'permalink', 'body')
    fields = ('post_url','tags','title','blog_title','published_on','slug')
    anonymous = AnonBlogPostHandler

    def list(self, request):
        obj_list = Post.objects.filter(active=True)
        return obj_list

    @classmethod
    def published_on(self, post_obj):
        return post_obj.pub_date

    @classmethod
    def blog_title(self, post_obj):
        return post_obj.blog.title

    @classmethod
    def post_url(self, post_obj):
        return post_obj.get_absolute_url()

    def read(self, request, **kwargs):
        post_slug = kwargs.get('post_slug', None)
        if post_slug:
            post = get_object_or_404(Post, slug=post_slug, active=True)
            return post
        else:
            return Post.objects.filter(active=True)

