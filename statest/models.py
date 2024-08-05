from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class statestic(models.Model):
    schools = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99999)], verbose_name = "школа")
    techers = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99999)], verbose_name = "учитель")
    student = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99999)], verbose_name = "ученик")
    educati = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99999)], verbose_name = "Д.О.У")
    techedu = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99999)], verbose_name = "учитель Д.О.У")
    chiledu = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99999)], verbose_name = "ученик Д.О.У")

    def __str__(self):
        return f'{self.schools}-{self.educati}'
    
    
    class Meta:
        verbose_name = "статистика"
        verbose_name_plural = "статистика"

