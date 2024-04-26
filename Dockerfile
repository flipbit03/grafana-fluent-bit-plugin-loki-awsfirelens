FROM grafana/fluent-bit-plugin-loki:2.9.7

# Found in https://github.com/aws-samples/amazon-ecs-firelens-examples/blob/mainline/examples/fluent-bit/parse-json/extra.conf
# This config has been slightly modified, since the 'parsers.conf' path has
# changed in the newer version of grafana/fluent-bit-plugin-loki
COPY jsonparse.conf /fluent-bit/etc/jsonparse.conf

# That's it.