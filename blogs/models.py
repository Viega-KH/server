from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "категоре"
        verbose_name_plural = "категоре"

    def __str__(self):
        return f'категоре'

class news(models.Model):
    title = models.CharField(max_length=200, verbose_name="заголовок")
    content = CKEditor5Field(verbose_name="мазмун", config_name='extends')
    image = models.ImageField(upload_to='news/', verbose_name = "Фото")
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name='news', verbose_name="категоре")
    published_date = models.DateField(auto_now_add=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "новость"  
        verbose_name_plural = "новости" 

    def __str__(self):
        return f'новость'
