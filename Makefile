.PHONY: build
build:
	docker build . -t flipbit03/grafana-fluent-bit-plugin-loki-awsfirelens:2.9.7

.PHONY: push
push:
	docker push flipbit03/grafana-fluent-bit-plugin-loki-awsfirelens:2.9.7