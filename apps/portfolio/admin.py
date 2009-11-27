from django.contrib import admin
from helpers.admin import SlugFieldOnly
from portfolio.models import Project, Technology, Photo, ProjectPhotoOrganizer

class PhotoInline(admin.TabularInline):
    model = ProjectPhotoOrganizer

class ProjectAdmin(SlugFieldOnly):
    inlines = [
        PhotoInline,
        ]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Photo, SlugFieldOnly)
admin.site.register(Technology, SlugFieldOnly)
