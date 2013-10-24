
from django.contrib import admin

from .models import PageImage, DefaultImage

class PageImageAdmin(admin.ModelAdmin):
    list_display = ['page', 'file', 'type']
    list_display_links = ['page', 'file']
admin.site.register(PageImage, PageImageAdmin)

class DefaultImageAdmin(admin.ModelAdmin):
    list_display = ['type', 'file']
    list_display_links = ['type', 'file']
admin.site.register(DefaultImage, DefaultImageAdmin)
