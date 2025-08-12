import time
import random
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.trace.status import Status, StatusCode

# -- CONFIGURATION AREA --

OTEL_ENDPOINT = "http://localhost:4318/v1/traces"  # Change to your OTLP HTTP endpoint
SPAN_NAME = "GET /api/v1/internal"
SPAN_ATTRIBUTES = {
    "http.method": "GET",
    "http.status_code": 404,
    "db.statement": "select * from traces",
    "service.name": "my-python-app"
}
SPAN_STATUS_CODE = StatusCode.ERROR  # Or StatusCode.OK, StatusCode.UNSET
DURATION_SECS = 0.5

# -- INIT --

provider = TracerProvider()
trace.set_tracer_provider(provider)
exporter = OTLPSpanExporter(endpoint=OTEL_ENDPOINT)
processor = BatchSpanProcessor(exporter)
provider.add_span_processor(processor)
tracer = trace.get_tracer("manual-trace-debugger")

# -- SPAN EMISSION --

with tracer.start_as_current_span(SPAN_NAME) as span:
    span.set_status(Status(SPAN_STATUS_CODE))
    for k, v in SPAN_ATTRIBUTES.items():
        span.set_attribute(k, v)

    print(f"Sending span {hex(span.get_span_context().span_id)} in trace {hex(span.get_span_context().trace_id)}")
    time.sleep(DURATION_SECS)  # Simulate real span duration
