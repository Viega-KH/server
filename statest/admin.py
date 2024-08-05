from django.contrib import admin
from .models import statestic

class statesticAdmin(admin.ModelAdmin):
    list_display = ('schools', 'techers', 'student', 'educati', 'techedu', 'chiledu')

    def has_add_permission(self, request):
        return False

admin.site.register(statestic, statesticAdmin)
