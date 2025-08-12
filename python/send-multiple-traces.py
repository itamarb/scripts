import time
import random
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.trace.status import Status, StatusCode

# -- CONFIGURATION AREA --

OTEL_ENDPOINT = "http://localhost:4318/v1/traces"  # Change to your OTLP HTTP endpoint
SPAN_NAME = "POST localhost"
SPAN_ATTRIBUTES = {
    "http.method": "GET",
    "http.url": "http://localhost:8090/system/health",
    "http.status_code": 403,
    "db.statement": "select * from spans"
}
SPAN_STATUS_CODE = StatusCode.ERROR  # Or StatusCode.OK, StatusCode.UNSET
TRACES_PER_MINUTE = 10
SLEEP_BETWEEN_TRACES = 60 / TRACES_PER_MINUTE  # 6 seconds per trace

# -- INIT --

provider = TracerProvider()
trace.set_tracer_provider(provider)
exporter = OTLPSpanExporter(endpoint=OTEL_ENDPOINT)
processor = BatchSpanProcessor(exporter)
provider.add_span_processor(processor)
tracer = trace.get_tracer("manual-trace-debugger")

# -- CONTINUOUS TRACE EMISSION --

print(f"Starting trace generation at {TRACES_PER_MINUTE} traces per minute...")
while True:
    duration_secs = random.uniform(0.5, 2.0)

    with tracer.start_as_current_span(SPAN_NAME) as span:
        span.set_status(Status(SPAN_STATUS_CODE))
        for k, v in SPAN_ATTRIBUTES.items():
            span.set_attribute(k, v)

        print(f"Sent span {hex(span.get_span_context().span_id)} in trace {hex(span.get_span_context().trace_id)} lasting {duration_secs:.2f}s")
        time.sleep(duration_secs)  # Simulate span duration

    # Sleep to maintain trace rate of 10/minute
    remaining_sleep = SLEEP_BETWEEN_TRACES - duration_secs
    if remaining_sleep > 0:
        time.sleep(remaining_sleep)
