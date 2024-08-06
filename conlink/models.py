from django.db import models

# Create your models here.
class contactlink(models.Model):
    location = models.CharField(max_length=200, null=True, verbose_name = "расположение")
    email = models.EmailField(max_length=200, null=True, verbose_name = "эмаль")
    telegram = models.URLField(max_length=200, null=True, verbose_name = "телеграмма")
    twitter = models.URLField(max_length=200, null=True, verbose_name = "Твиттер")
    instagram = models.URLField(max_length=200, null=True, verbose_name = "инстаграм")
    facebook = models.URLField(max_length=200, null=True, verbose_name = "Фейсбук")
    call = models.CharField(max_length=15, null=True, verbose_name = "телефон")


    class Meta:
        verbose_name = "связь"
        verbose_name_plural = "связь"


    def __str__(self):
        return f'связь'
