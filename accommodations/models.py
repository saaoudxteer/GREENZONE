from django.db import models
from django.urls import reverse

class Accommodation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField(default=1)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    is_green = models.BooleanField(default=False)
    image = models.ImageField(upload_to='accommodations/', null=True, blank=True)  # 👈 simple et direct
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('accommodation_detail', args=[str(self.id)])
