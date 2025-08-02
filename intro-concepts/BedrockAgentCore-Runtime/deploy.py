# create agentcore role
from bedrock_agentcore_starter_toolkit import Runtime
from boto3.session import Session
from utils import create_agentcore_role
import time

# create agentcore role
agent_name="agentcore_strands"
agentcore_iam_role = create_agentcore_role(agent_name=agent_name)

#create boto session
boto_session = Session()
region = boto_session.region_name
print(f"Region: {region}")

# instantiate Runtime
agentcore_runtime = Runtime()

# configure Runtime
response = agentcore_runtime.configure(
    entrypoint="strands_agent.py",
    execution_role=agentcore_iam_role['Role']['Arn'],
    auto_create_ecr=True,
    requirements_file="requirements.txt",
    region=region,
    agent_name=agent_name
)
print(f"Response: {response}")
launch_result = agentcore_runtime.launch()
print(f"Launch Result: {launch_result}")