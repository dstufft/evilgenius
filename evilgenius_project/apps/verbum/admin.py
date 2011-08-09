from django.contrib import admin
from verbum.models import Post, Link


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}


class LinkAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}


admin.site.register(Post, PostAdmin)
admin.site.register(Link, LinkAdmin)