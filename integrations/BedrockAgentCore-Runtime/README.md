# Bedrock AgentCore Runtime Integration

A simple integration for deploying and invoking Strands agents using AWS Bedrock AgentCore.

## [YouTube Video Coming]()

## Additional Resources/Credits
Most of this examples code is derived/built off of the samples in the below official AgentCore samples, give them a look!
- [Bedrock AgentCore Samples](https://github.com/awslabs/amazon-bedrock-agentcore-samples)

## Files

- `strands_agent.py` - Main Strands agent implementation
- `deploy.py` - Deploy agent to Bedrock AgentCore, this will also by default create the IAM role and Docker image for you.
- `invoke.py` - Invoke deployed agent
- `local_test.py` - Test agent locally before deployment

Execute deploy.py first to create the hosted endpoint you can invoke. Invoke shows how to use [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore/client/invoke_agent_runtime.html) to invoke the hosted endpoint. Invoke with session context shows session persistence.