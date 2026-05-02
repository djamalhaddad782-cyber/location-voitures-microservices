from rest_framework import viewsets, parsers
from .models import Car
from .serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.JSONParser]