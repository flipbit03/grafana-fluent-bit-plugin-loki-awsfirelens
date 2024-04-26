FROM fluent/fluent-bit:3.0.2

COPY fluent-bit/etc/stdout_tail.conf fluent-bit/etc/stdout_tail.conf
COPY fluent-bit/etc/fluent-bit.conf fluent-bit/etc/fluent-bit.conf
COPY fluent-bit/etc/parsers_custom.conf fluent-bit/etc/parsers_custom.conf