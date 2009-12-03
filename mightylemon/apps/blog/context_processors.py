from django.conf import settings
from django.core.cache import cache
from blog.models import Post

def blog(request):
    return {
        'blog': request.blog,
    }

def stats(request):
    if not settings.DEBUG:
        return {
            'STATS_CODE': settings.STATS_CODE,
            }
    return {
        'STATS_CODE': "<!-- debug mode enabled / no stats tracking -->",
        }

def date_ranges(request):
    months = cache.get('post_month_range')
    if not months:
        months = sorted(Post.objects.dates('pub_date', 'month'), reverse=True)
        cache.set('post_month_range', months, settings.CACHE_MIDDLEWARE_SECONDS)
    years = cache.get('post_year_range')
    if not years:
        years = sorted(Post.objects.dates('pub_date', 'year'), reverse=True)
        cache.set('post_year_range', years, settings.CACHE_MIDDLEWARE_SECONDS)
    
    return {
        'POST_DATE_MONTHS': months[:5],
        'POST_DATE_YEARS': years,
        }
