from django.contrib import admin
from .models import category, news
from django import forms

class newsForm(forms.ModelForm):
    class Meta:
        model = news
        fields = '__all__'

class newsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_date',)
    list_filter = ('category', 'published_date')
    search_fields = ('title',) 
    list_per_page = 10
    form = newsForm
    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'category',)
        }),
        ('Содержание', {
            'fields': ('content',),
            'classes': ('wide',),  
        }),
    )
    readonly_fields = ('created_at',)  

admin.site.register(category)
admin.site.register(news, newsAdmin)
