from django.contrib import admin
from .models import positionschool, infoschool, officeschool
from django.utils.translation import gettext_lazy as _

@admin.register(positionschool)
class PositionSchoolAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(infoschool)
class InfoSchoolAdmin(admin.ModelAdmin):
    list_display = ('title', 'titletext', 'number_pt', 'number_s', 'published_date')
    list_filter = ('published_date',)
    search_fields = ('title',)

class PositionFilter(admin.SimpleListFilter):
    title = _('position')
    parameter_name = 'position'

    def lookups(self, request, model_admin):
        positions = set((obj.positiono.id, obj.positiono.title) for obj in model_admin.model.objects.all())
        return [(id, title) for id, title in positions]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(positiono__id__exact=self.value())
        return queryset

@admin.register(officeschool)
class OfficeSchoolAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'positiono', 'wschool', 'acceptance', 'phone', 'published_date')
    list_filter = (PositionFilter, 'wschool',)
    search_fields = ('full_name', 'phone')
