from django.views.generic import date_based
from blog.models import Post
from springsteen.views import service
from django.utils import simplejson


def privileged_post_queryset(view_func):
    def _wrapped_view(request, **kwargs):
        if request.user.is_authenticated():
            kwargs["queryset"] = Post.objects.all()
        else:
            kwargs["queryset"] = Post.objects.active()
        return view_func(request, **kwargs)
    return _wrapped_view

def homepage(request, **kwargs):
    defaults = {
        "date_field": "pub_date",
        "num_latest": 3,
        "template_name": "homepage.html",
        "template_object_name": "posts",
    }
    defaults.update(kwargs)
    return date_based.archive_index(request, **defaults)
homepage = privileged_post_queryset(homepage)

object_detail = privileged_post_queryset(date_based.object_detail)
archive_day = privileged_post_queryset(date_based.archive_day)
archive_month = privileged_post_queryset(date_based.archive_month)
archive_year = privileged_post_queryset(date_based.archive_year)
archive_index = privileged_post_queryset(date_based.archive_index)



from springsteen.views import search as default_search
from springsteen.views import service
from springsteen.services import Web
from django.utils import simplejson
 
class BlogSearch(Web):
    _service = "web"
    def __init__(self, query, params={}):
        super(Web, self).__init__(query, params)
        self.params['sites']='justinlilly.com'
 
def search(request, timeout=2000, max_count=5, services=(BlogSearch,), extra_params={}):
    return default_search(request, timeout, max_count, services, extra_params)
 
 
def my_retrieve_func(query, start, count):
    def random_data(query):
        return {
            'title': "random %s" % query,
            'url': "http://example.com/%s/" % query,
            'abstract': '%s %s %s' % (query,query,query),
            }
    results = [ random_data(query) for x in range(count) ]
    dict = { 'total_results': 1000, 'results': results, }
    return simplejson.dumps(dict)
 
def service2(request):
    return service(request, retrieve_func=my_retrieve_func)


def blog_retrieve_func(query, start, count):
    results = Post.objects.all()
