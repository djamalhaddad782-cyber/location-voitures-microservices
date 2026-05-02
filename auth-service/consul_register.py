import consul
c = consul.Consul(host='consul', port=8500)
c.agent.service.register(
    name='auth-service',
    service_id='auth-1',
    address='auth-service',      # ← nom du conteneur, pas localhost
    port=8000,
    check=consul.Check.http('http://auth-service:8000/health/', interval='10s')
)
print("✅ Auth Service enregistré")