
from django.conf import settings
from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse
from django.contrib import admin

admin.autodiscover()

# override the default handler500 so i can pass MEDIA_URL
handler500 = "mightylemon.views.server_error"

urlpatterns = patterns("",
    url(r"^about/$", "django.views.generic.simple.direct_to_template", {
        "template": "about.html",
    }, name="about_me"),
    url(r"^hire-me/$", "django.views.generic.simple.direct_to_template", {
    "template": "hire-me.html",
    }),
    url(r"^coding/", include('codingrepo.urls')),
    url(r"^admin/doc/", include("django.contrib.admindocs.urls")),
    url(r"^admin/(.*)", admin.site.root),
    url(r"^blog/", include("blog.urls")),
    url(r"^comments/", include("django.contrib.comments.urls")),
    # url(r"^links/", include("links.urls")),
    # url(r"^events/", include("events.urls")),
    url(r"^work/", include("portfolio.urls")),
    url(r"^speaking/", include("speaking.urls")),
    url(r"^api/", include("api.urls")),
    url(r"^$", "django.views.generic.simple.redirect_to", {'url':'/blog/'}, name="oebfare_home"),
)

if settings.LOCAL_DEVELOPMENT:
    urlpatterns += patterns("django.views",
        url(r"^static/(?P<path>.*)", "static.serve", {
            "document_root": settings.MEDIA_ROOT,
        })
    )
