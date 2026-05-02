from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Booking
from .serializers import BookingSerializer
from .tasks import send_booking_notification_async, update_car_availability_async
import requests
from rest_framework.permissions import AllowAny

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def create(self, request):
        serializer = BookingSerializer(data=request.data)
        
        if serializer.is_valid():
            booking = serializer.save()
            
            car_id = booking.car_id
            try:
                # Appel au service des voitures (nom du conteneur Docker)
                car_response = requests.get(f"http://car-service:8001/api/cars/{car_id}/")
                
                if car_response.status_code != 200:
                    booking.delete()
                    return Response({"error": "Voiture non trouvée"}, status=status.HTTP_400_BAD_REQUEST)
                
                car = car_response.json()
                car_brand = car.get('brand')
                car_model = car.get('model')
                owner_id = car.get('owner_id')
                
                booking.owner_id = owner_id
                booking.save()
                
                # Envoi notification asynchrone
                send_booking_notification_async.delay(
                    booking.id, booking.renter_id, owner_id, car_brand, car_model
                )
                
                print(f"📨 Réservation #{booking.id} créée - En attente validation admin")
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                
            except Exception as e:
                booking.delete()
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        booking = self.get_object()
        booking.status = 'cancelled'
        booking.save()
        
        try:
            requests.patch(f"http://car-service:8001/api/cars/{booking.car_id}/", json={"available": True})
        except Exception as e:
            print(f"Erreur: {e}")
        
        return Response({"status": "cancelled"})


class AdminBookingViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]  # Pas d'authentification (pour test)
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    @action(detail=True, methods=['patch'])
    def accept(self, request, pk=None):
        booking = self.get_object()
        booking.status = 'accepted'
        booking.save()
        
        # Rendre la voiture indisponible
        try:
            requests.patch(f"http://car-service:8001/api/cars/{booking.car_id}/", json={"available": False})
            print(f"✅ Réservation #{booking.id} ACCEPTÉE")
        except Exception as e:
            print(f"Erreur: {e}")
        
        return Response({'status': 'accepted', 'booking_id': booking.id})
    
    @action(detail=True, methods=['patch'])
    def refuse(self, request, pk=None):
        booking = self.get_object()
        booking.status = 'refused'
        booking.save()
        print(f"❌ Réservation #{booking.id} REFUSÉE")
        return Response({'status': 'refused', 'booking_id': booking.id})
    
    # ⬇️ NOUVELLE ACTION : Voiture prise par le client
    @action(detail=True, methods=['patch'])
    def car_taken(self, request, pk=None):
        booking = self.get_object()
        booking.status = 'car_taken'
        booking.save()
        print(f"🚗 Réservation #{booking.id} : voiture prise par le client")
        return Response({'status': 'car_taken', 'booking_id': booking.id})
    
    # ⬇️ NOUVELLE ACTION : Marquer comme terminée
    @action(detail=True, methods=['patch'])
    def complete(self, request, pk=None):
        booking = self.get_object()
        booking.status = 'completed'
        booking.save()
        # Libérer la voiture
        try:
            requests.patch(f"http://car-service:8001/api/cars/{booking.car_id}/", json={"available": True})
            print(f"🏁 Réservation #{booking.id} TERMINÉE, voiture libérée")
        except Exception as e:
            print(f"Erreur lors de la libération: {e}")
        return Response({'status': 'completed', 'booking_id': booking.id})