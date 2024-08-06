from django.contrib import admin
from .models import positionlevel, infolevel, officelevel
from django.utils.translation import gettext_lazy as _

class PositionLevelAdmin(admin.ModelAdmin):
    list_display = ('title',)

class InfoLevelAdmin(admin.ModelAdmin):
    list_display = ('title', 'titletext', 'number_ch', 'number_ep', 'published_date',)
    list_filter = ('published_date',) 
    search_fields = ('title',)


class PositionFilter(admin.SimpleListFilter):
    title = _('Position')
    parameter_name = 'position'

    def lookups(self, request, model_admin):
        positions = set((obj.positiono.id, obj.positiono.title) for obj in model_admin.model.objects.all())
        return [(id, title) for id, title in positions]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(positiono__id__exact=self.value())
        return queryset

@admin.register(officelevel)
class OfficeLevelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'positiono', 'wslevel', 'acceptance', 'phone', 'published_date',)
    list_filter = (PositionFilter, 'wslevel',)  # Maxsus filtr va boshqa filtrlash
    search_fields = ('full_name', 'phone',)


admin.site.register(positionlevel, PositionLevelAdmin)
admin.site.register(infolevel, InfoLevelAdmin)