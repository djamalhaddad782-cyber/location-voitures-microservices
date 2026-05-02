import consul
c = consul.Consul(host='consul', port=8500)
c.agent.service.register(
    name='car-service',
    service_id='car-1',
    address='car-service',
    port=8001,
    check=consul.Check.http('http://car-service:8001/health/', interval='10s')   # ← car-service, pas localhost
)
print("✅ Car Service enregistré")