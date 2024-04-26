FROM grafana/fluent-bit-plugin-loki:2.9.7

# Copy the configuration file
COPY jsonparse.conf /fluent-bit/etc/jsonparse.conf