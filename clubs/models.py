from django.db import models
from school.models import infoschool
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class club(models.Model):
    students = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)], verbose_name = "студенты")
    wschool = models.ForeignKey(infoschool, on_delete=models.CASCADE, verbose_name = "школа")
    name = models.CharField(max_length=255, verbose_name = "урок")
    leader = models.CharField(max_length=255, verbose_name = "учитель")
    days = models.CharField(max_length=255, verbose_name = "день")
    meeting_time = models.CharField(max_length=255, verbose_name = "час")
    published_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "урок"

    def __str__(self):
        return self.name