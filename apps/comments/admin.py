from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email')
    search_help_text = 'you can search with name and email fields'


