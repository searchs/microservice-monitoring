# Microservice Monitoring & Observability Lab

This repository is an **engineering lab / case study** for instrumenting and observing small microservice systems across local containers and Kubernetes.

It combines simple Python/Flask services with Docker, Kubernetes and observability tooling so tracing, logging and deployment patterns can be explored without coupling the experiments to a commercial product.

## What this lab covers

- multiple small Flask API services
- Docker images and Docker Compose
- Kubernetes deployment manifests
- distributed tracing concepts
- Jaeger-based trace exploration
- Odigos/OpenTelemetry-oriented instrumentation experiments
- logging pipeline guidance, including the consolidated Logstash notes under `docs/logging/`

## Repository structure

```text
src/                     Sample microservices
k8s/                     Kubernetes manifests
docs/                    Observability and logging notes
docker-compose.yaml       Local multi-service environment
```

## Example local workflow

Bring up the local services with Docker Compose, then use the Kubernetes manifests when working through cluster-specific observability experiments.

For a local Jaeger service running in Kubernetes, a typical port-forwarding pattern is:

```bash
kubectl port-forward -n tracing svc/jaeger 16686:16686
```

Then access the Jaeger UI at `http://localhost:16686`.

Exact installation commands for external observability tools can age quickly; use their current upstream documentation rather than treating historical URLs or manifests in this lab as authoritative production installation instructions.

## Logging

The repository also contains durable logging guidance migrated from the earlier `elk-logger` experiment. See:

- [`docs/logging/logstash.md`](docs/logging/logstash.md)

That material captures topology, configuration and security/operations considerations without preserving obsolete ELK-specific scaffolding as a separate repository.

## Case-study boundary

This is not a production observability platform. Before applying a pattern to a production workload, revisit:

- telemetry data sensitivity and redaction
- sampling and retention
- authentication and network exposure
- resource limits and cardinality
- collector/high-availability architecture
- version compatibility
- alerting/SLO integration
- cost and operational ownership

Promote validated patterns into maintained products or platform repositories rather than expanding this lab into an operational dependency.
