from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User

# Sérialiseur principal (pour création et affichage courant)
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'role')
        read_only_fields = ('role',)
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        user.role = 'user'   # Par défaut
        user.save()
        return user

# Sérialiseur minimal pour l’admin (lecture seule, sans mot de passe)
class UserReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']