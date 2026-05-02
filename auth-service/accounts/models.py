from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES = (
        ('user', 'Utilisateur'),
        ('owner', 'Propriétaire'),
        ('admin', 'Administrateur'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='user')
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"