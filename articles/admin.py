from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Chapter, ArticleChapter


class ArticleChapterInlineFormset(BaseInlineFormSet):
    def clean(self):
        flag = 0
        for form in self.forms:

            if form.cleaned_data.get('DELETE'):
                continue

            if form.cleaned_data.get('is_main'):
                flag += 1

            if flag > 1:
                raise ValidationError('Основным может быть только один раздел.')

        if flag == 0:
            raise ValidationError('Укажите основной раздел.')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleChapterInLine(admin.TabularInline):
    model = ArticleChapter
    extra = 3
    formset = ArticleChapterInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleChapterInLine]


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['name']
