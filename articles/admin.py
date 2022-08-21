from django.contrib import admin

from .models import Article, Chapter


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Chapter)
class ArticleAdmin(admin.ModelAdmin):
    pass
