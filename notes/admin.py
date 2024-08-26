from django.contrib import admin
from .models import Note


@admin.register(Note)
class AdminNote(admin.ModelAdmin):
    list_display = ("id", "author")
    list_display_links = list_display
    list_filter = ('id', 'author')
    search_fields = ('id', 'author')
