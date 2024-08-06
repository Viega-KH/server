from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import contactlink
from django.utils.html import format_html
from django.urls import reverse



@admin.register(contactlink)
class ContactLinkAdmin(admin.ModelAdmin):
    def edit_icon(self, obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        # Font Awesome ikonasidan foydalanish
        return format_html('<a href="{}" title="Edit"><i class="fas fa-edit"></i></a>', url)
    edit_icon.short_description = 'Edit'
    edit_icon.allow_tags = True
    
    list_display = ('email', 'telegram', 'instagram', 'facebook', 'call', 'edit_icon')
    
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.unregister(User)
admin.site.unregister(Group)