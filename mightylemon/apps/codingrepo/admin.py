from django.contrib import admin
from helpers.admin import SlugFieldOnly
from codingrepo.models import CodeProject

admin.site.register(CodeProject, SlugFieldOnly)
