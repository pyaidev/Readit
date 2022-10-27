from django.contrib import admin
from .models import Category, Tags, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')
    search_fields = ('title', )
    list_filter = ('category', )
    date_hierarchy = 'created_at'


admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Article, ArticleAdmin)

