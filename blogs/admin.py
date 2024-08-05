from django.contrib import admin
from .models import category, news
from django import forms

class newsForm(forms.ModelForm):
    class Meta:
        model = news
        fields = '__all__'

class newsAdmin(admin.ModelAdmin):
    form = newsForm
    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'category',)
        }),
        ('content', {
            'fields': ('content',),
            'classes': ('wide',),  # Bu content maydonini kengaytiradi
        }),
    )
    readonly_fields = ('created_at',)  # `created_at` maydonini o'zgartirilmasligini ta'minlash

admin.site.register(category)
admin.site.register(news, newsAdmin)
