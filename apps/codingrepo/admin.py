from django.contrib import admin
from helpers.admin import SlugFieldOnly
from codingrepo.models import Language, License, CodeProject

admin.site.register(Language, SlugFieldOnly)
admin.site.register(License, SlugFieldOnly)
admin.site.register(CodeProject, SlugFieldOnly)
