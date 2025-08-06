import boto3
import json

# substitute with your own agent ARN and region
agent_arn = "ENTER_YOUR_AGENT_ARN_HERE"
region = "Enter region here"

agentcore_client = boto3.client(
    'bedrock-agentcore',
    region_name=region
)

boto3_response = agentcore_client.invoke_agent_runtime(
    agentRuntimeArn=agent_arn,
    qualifier="DEFAULT",
    payload=json.dumps({"prompt": "What is 5 times 8?"})
)

#print(boto3_response)

# Fix: Use 'response' key and handle JSON structure properly
response_body = boto3_response['response'].read().decode()
result_json = json.loads(response_body)
print(f"Output: {json.dumps(result_json)}")
