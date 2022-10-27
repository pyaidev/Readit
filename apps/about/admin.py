from django.contrib import admin

from .models import FeedBack


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position')
    search_fields = ('name', 'position')


admin.site.register(FeedBack, FeedBackAdmin)
