from django.contrib import admin
from .models import contact

class contactAdmin(admin.ModelAdmin):
    list_per_page = 10
    readonly_fields = ('full_name', 'subject', 'phone', 'message')
    list_display = ('full_name', 'subject', 'phone', 'published_date',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(contact, contactAdmin)