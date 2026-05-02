from celery import shared_task
import requests
import time

@shared_task
def send_booking_notification_async(booking_id, renter_id, owner_id, car_brand, car_model):
    time.sleep(2)
    print(f"\n{'='*50}")
    print(f"📧 [ASYNC] Notification de réservation")
    print(f"{'='*50}")
    print(f"   Réservation N°: {booking_id}")
    print(f"   Voiture: {car_brand} {car_model}")
    print(f"   Locataire ID: {renter_id}")
    print(f"   Propriétaire ID: {owner_id}")
    print(f"{'='*50}\n")
    return {"status": "sent", "booking_id": booking_id}

@shared_task
def update_car_availability_async(car_id, available):
    try:
        time.sleep(1)
        url = f"http://car-service:8001/api/cars/{car_id}/"
        response = requests.patch(url, json={"available": available})
        print(f"🔄 [ASYNC] Voiture #{car_id} → disponible: {available}")
        return {"status": "success", "car_id": car_id}
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return {"status": "error", "car_id": car_id}