from django.contrib import admin

from .models import Publications


class PublicationsAdmin(admin.ModelAdmin):
    list_display = ('image', 'description', 'likes')
    list_display_links = ('description',)
    search_fields = ('user', 'description', 'likes')
    

admin.site.register(Publications, PublicationsAdmin)