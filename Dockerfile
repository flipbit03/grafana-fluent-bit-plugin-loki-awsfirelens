FROM fluent/fluent-bit:3.0.2

COPY fluent-bit/etc/stdout-tail.conf fluent-bit/etc/stdout-tail.conf
COPY fluent-bit/etc/parsers-cogram.conf fluent-bit/etc/parsers-cogram.conf
COPY fluent-bit/etc/fluent-bit.conf fluent-bit/etc/fluent-bit.conf