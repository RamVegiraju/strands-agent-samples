from strands import Agent, tool
from strands_tools import calculator # Import the calculator tool
from strands.models import BedrockModel
# built-in tools
from strands_tools import calculator

# use for local testing
import argparse
import json

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

def strands_agent_bedrock(payload):
    """
    Invoke the agent with a payload
    """
    user_input = payload.get("prompt")
    response = agent(user_input)
    return response.message['content'][0]['text']

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("payload", type=str)
    args = parser.parse_args()
    response = strands_agent_bedrock(json.loads(args.payload))
    print(response)