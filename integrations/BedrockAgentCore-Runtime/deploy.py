# create agentcore role
from bedrock_agentcore_starter_toolkit import Runtime
from boto3.session import Session
import time

#create boto session to capture region
boto_session = Session()
region = boto_session.region_name
print(f"Region: {region}")

# instantiate Runtime
agentcore_runtime = Runtime()

# configure Runtime
response = agentcore_runtime.configure(
    entrypoint="strands_agent.py",
    auto_create_execution_role=True,
    auto_create_ecr=True,
    requirements_file="requirements.txt",
    region=region,
    agent_name="strands_agent"
)
launch_result = agentcore_runtime.launch()

# Poll for status borrowed from here: https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/01-AgentCore-runtime/03-advanced-concepts/02-understanding-runtime-context/understanding_runtime_context.ipynb
status_response = agentcore_runtime.status()
status = status_response.endpoint['status']
end_status = ['READY', 'CREATE_FAILED', 'DELETE_FAILED', 'UPDATE_FAILED']
while status not in end_status:
    time.sleep(10)
    status_response = agentcore_runtime.status()
    status = status_response.endpoint['status']
    print(status)
print(f"Status: {status}")
print(f"Endpoint ARN: {launch_result.agent_arn}")