import consul
c = consul.Consul(host='consul', port=8500)
c.agent.service.register(
    name='booking-service',
    service_id='booking-1',
    address='booking-service',
    port=8002,
    check=consul.Check.http('http://booking-service:8002/health/', interval='10s')  # ← booking-service, pas localhost
)
print("✅ Booking Service enregistré")