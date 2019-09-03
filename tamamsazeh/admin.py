from django.contrib import admin
from tamamsazeh.models import Article, Post


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Article, ArticleAdmin)
