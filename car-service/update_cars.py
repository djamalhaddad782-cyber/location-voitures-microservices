from cars.models import Car

Car.objects.all().delete()

cars = [
    {"brand": "Renault", "model": "Clio 5", "year": 2022, "price_per_day": 4000, "available": True, "image_url": "https://picsum.photos/id/111/400/300"},
    {"brand": "Peugeot", "model": "208", "year": 2023, "price_per_day": 3500, "available": True, "image_url": "https://picsum.photos/id/112/400/300"},
    {"brand": "Dacia", "model": "Sandero Stepway", "year": 2023, "price_per_day": 4000, "available": True, "image_url": "https://picsum.photos/id/107/400/300"},
    {"brand": "BMW", "model": "Série 1", "year": 2022, "price_per_day": 10000, "available": True, "image_url": "https://picsum.photos/id/113/400/300"},
    {"brand": "Kia", "model": "Sportage", "year": 2022, "price_per_day": 7000, "available": True, "image_url": "https://picsum.photos/id/116/400/300"},
    {"brand": "Audi", "model": "A3", "year": 2022, "price_per_day": 9500, "available": True, "image_url": "https://picsum.photos/id/114/400/300"},
]

for car in cars:
    Car.objects.create(**car)

print("Voitures ajoutées :", len(cars))