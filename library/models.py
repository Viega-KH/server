from django.db import models


class librarycategore(models.Model):
    name = models.CharField(max_length=225, verbose_name = "категория")
    def __str__(self):
        return f'категория'
            

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категория"



class library(models.Model):
    categore = models.ForeignKey(librarycategore, on_delete=models.CASCADE, verbose_name = "категория")
    name = models.CharField(max_length=255, verbose_name = "название книги")
    file = models.FileField(upload_to='library/', verbose_name="файл", help_text='PDF или Word')
    published_date = models.DateField(auto_now_add=True, verbose_name = "время")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'книги'

        
    class Meta:
        verbose_name = "книги"
        verbose_name_plural = "книги"