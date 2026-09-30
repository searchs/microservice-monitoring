# Logstash Logging Pattern

This note consolidates the useful logging/ELK lesson from the retired `elk-logger` repository without carrying its old ELK 7.6 Docker stack or notebook checkpoints.

## Goal

Application services should emit structured logs that can be shipped asynchronously to a central log pipeline without blocking request handling.

A simple topology is:

```text
service -> structured logger -> Logstash/collector -> Elasticsearch/OpenSearch -> Kibana/dashboard
```

## Application guidance

Prefer structured JSON events containing stable fields such as:

- timestamp
- service name
- environment
- log level
- message/event name
- request/correlation ID
- trace/span ID when tracing is enabled
- relevant domain identifiers that are safe to log

Do **not** log passwords, access tokens, full payment details, private keys or unnecessary personal data.

## Delivery guidance

- use a bounded queue/buffer rather than blocking the request thread on network I/O
- define retry/backoff behaviour explicitly
- decide whether log loss is acceptable during collector outages
- expose dropped/failed-log metrics
- prefer standard transports/protocols supported by the current observability stack

## Logstash example

A minimal pipeline can accept JSON over TCP and send it to Elasticsearch/OpenSearch:

```conf
input {
  tcp {
    port => 5000
    codec => json_lines
  }
}

filter {
  mutate {
    add_field => { "pipeline" => "application-logs" }
  }
}

output {
  elasticsearch {
    hosts => ["http://elasticsearch:9200"]
    index => "application-logs-%{+YYYY.MM.dd}"
  }
}
```

Treat this as a pattern rather than a pinned ELK-version configuration; exact plugin syntax should be verified against the deployed stack.

## Provenance

The earlier `elk-logger` repository was based on an ELK 7.6-era Docker setup and included a small Python/notebook experiment for sending logs to Logstash. Only the durable structured/asynchronous logging lesson is retained here. Its tracked `.env` contained only an ELK version value, not a credential.
