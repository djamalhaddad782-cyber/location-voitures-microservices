from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    owner_id = models.IntegerField()
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(default='https://via.placeholder.com/300x180?text=Car+Image')
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"