from django.db import models
from school.models import infoschool
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


    
class wclases(models.Model):
    title = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(11)], verbose_name='класс')
    published_date = models.DateField(auto_now_add=True, blank=True, verbose_name = "время")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = "класс"
        verbose_name_plural = "класс"

class lesson(models.Model):
    wschool = models.ForeignKey(infoschool, on_delete=models.CASCADE, verbose_name = "школа")
    wclass = models.ForeignKey(wclases, on_delete=models.CASCADE, verbose_name = "класс")
    file = models.FileField(upload_to='lesson/', verbose_name = "файл", help_text='PDF или Word')
    published_date = models.DateField(auto_now_add=True, verbose_name = "время")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'список'
    
    class Meta:
        verbose_name = "список"
        verbose_name_plural = "список"