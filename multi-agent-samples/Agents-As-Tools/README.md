# Agents Orchestrator

A multi-agent orchestrator system built with the Strands SDK that routes queries to specialized agents for research and AWS service tasks.

## 📁 Project Structure

```
Agents-As-Tools/
├── __init__.py          # Package initialization
├── main.py              # Entry point with CLI interface
├── orchestrator.py      # Main orchestrator class
├── config.py           # Configuration and model settings
├── tools.py            # Custom tool implementations
├── utils.py            # Utility functions
├── requirements.txt    # Python dependencies
└── README.md          # This documentation
```

## 🚀 Quick Start

### Installation

1. Install dependencies (best to use a virtual environment):
```bash
pip install -r requirements.txt
```

2. Set up AWS credentials:
```bash
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=us-east-1
```

### Usage

Run the application:
```bash
python3 main.py
```

This will automatically run the predefined example queries to demonstrate the orchestrator functionality.

## 🏗️ Architecture

### Core Components

- **AgentsOrchestrator**: Main class that routes queries to appropriate agents
- **Research Assistant**: Processes web links and summarizes content  
- **AWS Assistant**: Handles AWS service queries for your account
- **Configuration**: Centralized model and prompt management
- **Utilities**: Helper functions for logging, validation, and formatting

### Available Tools

1. **research_assistant(url)**: Fetches and summarizes web content
2. **aws_assistant(query)**: Answers AWS service questions

## 📋 Example Queries

**Research queries:**
- "Research this link: https://strandsagents.com/docs/ and summarize it"
- "What's on this webpage: https://aws.amazon.com/bedrock/"

**AWS queries:**
- "List all S3 buckets in my account"
- "What EC2 instances are currently running?"

## 🔧 Configuration

Edit `config.py` to modify:
- Model settings (model ID, region, temperature)
- Agent prompts
- System behavior

## 🛠️ Development

### Adding New Tools

1. Create tool function in `tools.py` with `@tool` decorator
2. Add to `get_available_tools()` function  
3. Update system prompt in `config.py`

### Customizing Agents

Modify prompts in `config.py` to change agent behavior and capabilities.

## 📝 Logging

The application uses Python's built-in logging with:
- INFO level for general operations
- ERROR level for exceptions
- Structured logging for query/response pairs

## ⚙️ Requirements

- Python 3.8+
- AWS credentials configured
- Access to Amazon Bedrock Claude models

## 🔒 Security Notes

- Input sanitization implemented
- Query length limits enforced
- Error handling prevents information leakage
- Logging includes privacy-conscious truncation 