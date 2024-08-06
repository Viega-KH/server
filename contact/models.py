from django.db import models


class contact(models.Model):
    full_name = models.CharField(max_length=200, verbose_name = "полное имя")
    subject = models.CharField(max_length=200, verbose_name = "заголовок")
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name = "телефон")
    message = models.TextField(verbose_name = "содержание")
    published_date = models.DateField(auto_now_add=True, blank=True, null=True, verbose_name = "время")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "время")

    class Meta:
        verbose_name = "последнее"
        verbose_name_plural = "последнее"


    def __str__(self):
        return f"последнее"
