from strands import Agent, tool
from strands_tools import calculator # Import the calculator tool
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands.models import BedrockModel
# built-in tools
from strands_tools import calculator

# use for local testing
import argparse
import json

# create agentcore role
from utils import create_agentcore_role

agent_name="agentcore_strands"
agentcore_iam_role = create_agentcore_role(agent_name=agent_name)

# instantiate BedrockAgentCoreApp
app = BedrockAgentCoreApp()

# Define Model
MODEL_CONFIG = {
    "model_id": "us.anthropic.claude-sonnet-4-20250514-v1:0",
    "region_name": "us-east-1",
}
model = BedrockModel(**MODEL_CONFIG)

# Define Agent
agent = Agent(
    model=model,
    tools=[calculator]
)

@app.entrypoint
def strands_agent_bedrock(payload):
    """
    Invoke the agent with a payload
    """
    user_input = payload.get("prompt")
    response = agent(user_input)
    return response.message['content'][0]['text']

if __name__ == "__main__":
    app.run()







