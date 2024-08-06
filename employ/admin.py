from django.contrib import admin
from .models import department, leadership

@admin.register(department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_per_page = 10

@admin.register(leadership)
class LeadershipAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'department', 'phone', 'email', 'acceptance', 'published_date',)
    list_filter = ('published_date', 'acceptance', )  # `department` bo'yicha filtr qo'shish
    search_fields = ('full_name', 'department__name', 'phone', 'email')  # `department__name` orqali qidirish
    list_per_page = 10
