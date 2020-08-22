from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Drug(models.Model):
    name = models.TextField()
    code = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Vaccination(models.Model):
    rut = models.TextField()
    dose = models.FloatField(
        validators=[MinValueValidator(0.15), MaxValueValidator(1.0)]
    )
    date = models.DateField(auto_now_add=True)
    drug = models.ForeignKey(
        Drug,
        related_name='vaccinations',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f'Vaccination for {self.rut}'
