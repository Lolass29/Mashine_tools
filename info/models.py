from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.TextField(default='No description')

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Model_Mashine_Tools(models.Model):
    TipChoice = [
        ('TURNING', 'Turning'),
        ('DRILLING', 'Drilling'),
        ('GRINDING', 'Grinding'),
        ('COMBINED', 'Combined'),
        ('GEAR_PROCESSING', 'Gear_Processing'),
        ('MILLING', 'Milling'),
        ('PLANING', 'Planing'),
        ('SPLIT', 'Split'),
        ('DIFFERENT', 'Different'),
    ]

    name = models.CharField(max_length=50)
    tip = models.CharField(max_length=50, choices=TipChoice, default='Different')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    characteristic = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = 'Models'
        ordering = ['company', 'price']

    def __str__(self):
        return f"{self.name} {self.company} {self.price}"
