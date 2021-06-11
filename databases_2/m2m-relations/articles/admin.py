from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, ArticleSection, Section


class ArticleSectionInlineFormset(BaseInlineFormSet):
    def clean(self):
        section_count = 0
        for form in self.forms:
            if form.cleaned_data and form.cleaned_data['main_title']:
                section_count += 1
            if section_count == 0:
                raise ValidationError('Укажите основной раздел')
            if section_count > 1:
                raise ValidationError('Основным может быть только один раздел')

            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            # form.cleaned_data
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleSectionInline(admin.TabularInline):
    model = ArticleSection
    formset = ArticleSectionInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleSectionInline]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass


@admin.register(ArticleSection)
class SectionAdmin(admin.ModelAdmin):
    pass
