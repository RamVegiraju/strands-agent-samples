import uuid
import boto3
import json

# substitute with your own agent ARN and region
agent_arn = "ENTER_YOUR_AGENT_ARN_HERE"
region = "Enter region here"

# boto3 agentcore invoke client
agentcore_client = boto3.client(
    'bedrock-agentcore',
    region_name=region
)

session_id = uuid.uuid4()
print(f"📋 Starting Session 1: {session_id}")

payload_one = {"prompt": "What is 5 times 8?"}
payload_two = {"prompt": "Take the result of the previous calculation and multiply it by 2"}

invoke_response = agentcore_client.invoke_agent_runtime(
    agentRuntimeArn=agent_arn,
    runtimeSessionId=str(session_id),
    payload=json.dumps(payload_one)
    )

response_body = invoke_response['response'].read().decode()
result_json = json.loads(response_body)
print(f"Output One: {json.dumps(result_json)}")

# See if the session is still active and we can use same session id for context
invoke_response_two = agentcore_client.invoke_agent_runtime(
    agentRuntimeArn=agent_arn,
    runtimeSessionId=str(session_id),
    payload=json.dumps(payload_two)
    )

response_body_two = invoke_response_two['response'].read().decode()
result_json_two = json.loads(response_body_two)
print(f"Output Two: {json.dumps(result_json_two)}")


# failed to get other session context with new session id example
session_id_two = uuid.uuid4()

# example of failed to get other session context with new session id
print(f"📋 Starting Session 2: {session_id_two}")

payload_three = {"prompt": "What is 5 times the result of the previous calculation?"}

invoke_response_three = agentcore_client.invoke_agent_runtime(
    agentRuntimeArn=agent_arn,
    runtimeSessionId=str(session_id_two),
    payload=json.dumps(payload_three)
    )

response_body_three = invoke_response_three['response'].read().decode()
result_json_three = json.loads(response_body_three)
print(f"Output Three: {json.dumps(result_json_three)}")