from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import statestic

class StatesticAdmin(admin.ModelAdmin):
    list_display = ('schools', 'techers', 'student', 'educati', 'techedu', 'chiledu', 'edit_icon')

    def edit_icon(self, obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        # Font Awesome ikonasidan foydalanish
        return format_html('<a href="{}" title="Edit"><i class="fas fa-edit"></i></a>', url)
    edit_icon.short_description = 'Edit'
    edit_icon.allow_tags = True

    # def has_add_permission(self, request):
    #     return False

admin.site.register(statestic, StatesticAdmin)
