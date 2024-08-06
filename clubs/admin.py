from django.contrib import admin
from .models import club, infoschool

@admin.register(club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'students', 'wschool', 'leader', 'days', 'meeting_time', 'published_date')
    list_filter = ('published_date', 'days')
    search_fields = ('name', 'leader', 'wschool__title')
    list_per_page = 20
