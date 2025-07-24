from strands import Agent
from strands.telemetry import StrandsTelemetry
from strands.models.bedrock import BedrockModel

print("Starting Langfuse tracing")
strands_telemetry = StrandsTelemetry().setup_otlp_exporter()