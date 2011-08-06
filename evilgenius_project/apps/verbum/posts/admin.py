from django.contrib import admin

from verbum.posts.models import Post

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)