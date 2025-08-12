import time
import random
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.metrics import get_meter_provider, set_meter_provider

# -- CONFIGURATION AREA --

OTEL_ENDPOINT = "http://localhost:4318/v1/metrics"
METRIC_NAME = "custom.random.metric"
LABELS = {"host": "localhost", "env": "dev", "service.name": "my-service"}
METRICS_PER_MINUTE = 10
SLEEP_BETWEEN_METRICS = 60 / METRICS_PER_MINUTE

# -- INIT METRICS EXPORTER --

exporter = OTLPMetricExporter(endpoint=OTEL_ENDPOINT)
reader = PeriodicExportingMetricReader(exporter, export_interval_millis=1000)

provider = MeterProvider(metric_readers=[reader])
set_meter_provider(provider)
meter = get_meter_provider().get_meter("custom-metric-debugger")

# Use an up-down counter as a workaround for Gauge (more widely supported)
metric_instrument = meter.create_up_down_counter(
    name=METRIC_NAME,
    description="Random fluctuating value",
    unit="1"
)

print(f"Starting metric generation at {METRICS_PER_MINUTE} samples per minute...")

# -- CONTINUOUS EMISSION --

value = 0
while True:
    # Random walk simulation
    delta = random.randint(-5, 50)
    value += delta
    metric_instrument.add(delta, attributes=LABELS)
    print(f"Reported {METRIC_NAME} += {delta} -> total {value}")
    time.sleep(SLEEP_BETWEEN_METRICS)
