from django.contrib import admin
from .models import positionlevel, infolevel, officelevel

class PositionLevelAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('published_date',)  # Add filters here

class InfoLevelAdmin(admin.ModelAdmin):
    list_display = ('title', 'titletext', 'number_ch', 'number_ep', 'published_date',)
    list_filter = ('published_date', 'title',)  # Add filters here

class OfficeLevelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'positiono', 'wslevel', 'acceptance', 'phone', 'published_date',)
    list_filter = ('positiono', 'wslevel', 'published_date',)  # Add filters here

admin.site.register(positionlevel, PositionLevelAdmin)
admin.site.register(infolevel, InfoLevelAdmin)
admin.site.register(officelevel, OfficeLevelAdmin)
