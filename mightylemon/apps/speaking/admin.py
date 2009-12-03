from django.contrib import admin
from helpers.admin import SlugFieldOnly
from speaking.models import Talk, Conference, TalkLink

admin.site.register(Talk, SlugFieldOnly)
admin.site.register(Conference, SlugFieldOnly)
admin.site.register(TalkLink, SlugFieldOnly)
