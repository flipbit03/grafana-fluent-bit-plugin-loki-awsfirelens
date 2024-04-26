# grafana-fluent-bit-plugin-loki-awsfirelens

Custom `grafana/fluent-bit-plugin-loki` image, with an added filter config for JSON parsing of logs coming from an AWS Firelens-enabled container.

- Reintroduced Amazon's `.log`-field parser found [here](https://github.com/aws-samples/amazon-ecs-firelens-examples/blob/mainline/examples/fluent-bit/parse-json/extra.conf)
  - This allows the log messages to be parsed as JSON and the fields to be extracted as labels in Loki
  - Useful if your ECS deployment logs are outputting JSON, and you want those json fields to be queryable in Grafana without having to resort to nested JSON parsing in LogQL, which can be cumbersome and inefficient.