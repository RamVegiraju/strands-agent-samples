# bedrock agentcore runtime
from bedrock_agentcore.runtime import BedrockAgentCoreApp
# strands agent & tools
from strands.models import BedrockModel
from strands import Agent, tool
from strands_tools import calculator # Import the calculator tool

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
def strands_agent_bedrock(payload, context):
    """
    Invoke the agent with a payload
    """
    user_input = payload.get("prompt")
    print("User Input:", user_input)
    print("Runtime Session ID:", context.session_id)
    print("Context Object Type:", type(context))
    response = agent(user_input)
    return response.message['content'][0]['text']

if __name__ == "__main__":
    app.run()