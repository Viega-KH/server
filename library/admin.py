from django.contrib import admin
from .models import librarycategore, library


class LibraryCategoreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_per_page = 10


class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'categore', 'published_date')
    list_filter = ('categore', 'published_date')
    search_fields = ('name', 'categore__name')
    list_per_page = 10

admin.site.register(librarycategore, LibraryCategoreAdmin)
admin.site.register(library, LibraryAdmin)
