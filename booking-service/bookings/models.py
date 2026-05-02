from django.db import models

class Booking(models.Model):
    STATUS_CHOICES = [
         ('pending', 'En attente'),
    ('accepted', 'Acceptée'),
    ('car_taken', 'Voiture prise par le client'),
    ('refused', 'Refusée'),
    ('cancelled', 'Annulée'),
    ('completed', 'Terminée'),
    ]
    
    car_id = models.IntegerField()
    renter_id = models.IntegerField()
    owner_id = models.IntegerField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Réservation #{self.id} - Voiture {self.car_id}"