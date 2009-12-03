from django.contrib import admin

class SlugFieldOnly(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

