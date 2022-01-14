from django.contrib import admin

from youtubemusic.models import Music, User


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ["id", 'title']
    search_fields = ['title']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", 'name']
    search_fields = ['name']


