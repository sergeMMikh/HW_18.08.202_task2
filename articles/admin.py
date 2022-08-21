from django.contrib import admin

from .models import Article, Chapter, ArticleChapter


class ArticleChapterInLine(admin.TabularInline):
    model = ArticleChapter
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleChapterInLine]


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['name']


