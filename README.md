#  Monitoring Microservices - Python


## Outline
- Setup at least 2 microservices (Flask apis)
- Dockerize the applications
- Docker-compose the apps with docker-compose.yml and build 
- Setup deployment with Kubernetes (k8)
- Install and configure Odigos
- Install and configure Jaeger
- Deploy Jaeger to k8
- Enable tracing on k8 (```bash kubectl apply -f https://raw.githubusercontent.com/keyval-dev/opentelemetry-go-instrumentation/master/docs/getting-started/jaeger.yaml -n tracing
``)
- Forward k8 ports(```bash kubectl port-forward -n tracing svc/jaeger 16686:16686
``)
- Connect Odigos and Jaeger
- Use Jaeger UI to trace logs et al (```bash http://localhost:16686``)