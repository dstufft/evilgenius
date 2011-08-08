from django.contrib import admin
from verbum.models import Post, Link


class PostAdmin(admin.ModelAdmin):
    pass


class LinkAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Link, LinkAdmin)