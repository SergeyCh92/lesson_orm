from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Tags, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main = False
        for form in self.forms:
            if 'is_main' in form.cleaned_data and form.cleaned_data['is_main']:
                if not main:
                    main = True
                else:
                    raise ValidationError('Основным может быть только один тэг.')
        if not main:
            raise ValidationError('Необходимо выбрать хотя бы один тэг в качестве основного.')
        return super().clean()


class ArticleLabelInline(admin.TabularInline):
    model = Tags
    formset = RelationshipInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    inlines = [ArticleLabelInline]


@admin.register(Scope)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    # inlines = [ArticleLabelInline]


@admin.register(Tags)
class ArticleLabelAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'tag']
