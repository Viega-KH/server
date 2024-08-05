from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class positionlevel(models.Model):
    title = models.CharField(max_length=100, verbose_name = "позиция")
    published_date = models.DateField(auto_now_add=True, verbose_name = "время")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "позиции"
        verbose_name_plural = "позиции"


class infolevel(models.Model):
    title = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)], verbose_name = "Номер школы")
    titletext = models.CharField(max_length=200, verbose_name = "Название школы")
    number_ch =  models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)], verbose_name = "количество студентов")
    number_ep  =  models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)], verbose_name = "количество учителей")
    published_date = models.DateField(auto_now_add=True, verbose_name = "позиция")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
    
    
    class Meta:
        verbose_name = "организация"
        verbose_name_plural = "организация"


class officelevel(models.Model):
    positiono = models.ForeignKey(positionlevel, on_delete=models.CASCADE, verbose_name = "позиция")
    wslevel = models.ForeignKey(infolevel, on_delete=models.CASCADE, verbose_name = "Д.О.У")
    full_name = models.CharField(max_length=100, verbose_name = "имя Фамилия")
    acceptance = models.CharField(max_length=100, verbose_name = "день поступления")
    phone = models.CharField(max_length=13, verbose_name = "Телефон")
    image = models.ImageField(upload_to='offis/', default='default/o1.jpg', verbose_name = "Фото")
    published_date = models.DateField(auto_now_add=True, verbose_name = "время")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "лидерство"
        verbose_name_plural = "лидерство"

    
