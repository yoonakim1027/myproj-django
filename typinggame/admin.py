from django.contrib import admin

from typinggame.models import Typing


@admin.register(Typing)
class TypingAdmin(admin.ModelAdmin):
    list_display = ["id", 'name']
    search_fields = ['name']
