from django.contrib import admin

from youtubemusic.models import Music


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ["id", 'title']
    search_fields = ['title']