from django.db import models

class department(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name = "позиция")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'позиция'
    
    class Meta:
        verbose_name = "позиция"
        verbose_name_plural = "позиция"

class leadership(models.Model):
    full_name = models.CharField(max_length=200, verbose_name = "имя Фамилия")
    department = models.ForeignKey(department, on_delete=models.CASCADE, related_name='leaders', verbose_name = "позиция")
    phone = models.CharField(max_length=15, verbose_name = "телефон")
    email = models.EmailField(verbose_name = "электронная почта")
    acceptance = models.CharField(max_length=100, verbose_name = "день поступления")
    image = models.ImageField(upload_to='leadership/', default='default/o1.jpg', verbose_name = "Фото")
    published_date = models.DateField(auto_now_add=True, verbose_name = "время")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Лидер"


    class Meta:
        verbose_name = "Лидер"
        verbose_name_plural = "Лидер"