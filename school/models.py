from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class positionschool(models.Model):
    title = models.CharField(max_length=100, verbose_name = "позиция")
    published_date = models.DateField(auto_now_add=True, verbose_name = "время")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "позиции"
        verbose_name_plural = "позиции"


class infoschool(models.Model):
    title = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)])
    titletext = models.CharField(max_length=200)
    number_pt = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)])
    number_s = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)])
    published_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = "школы"
        verbose_name_plural = "школы"



class officeschool(models.Model):
    positiono = models.ForeignKey(positionschool, on_delete=models.CASCADE, related_name='positionschool', verbose_name = "позиция")
    wschool = models.ForeignKey(infoschool, on_delete=models.CASCADE, verbose_name = "школы")
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
    
    

    
