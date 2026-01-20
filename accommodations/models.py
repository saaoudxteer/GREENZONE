from django.db import models
from django.urls import reverse

class Accommodation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField(default=1)
    is_green = models.BooleanField(default=True)

    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='accommodations/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)