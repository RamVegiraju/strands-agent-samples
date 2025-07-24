# Sequential Graph Example

A simple example demonstrating **sequential graph execution** using Strands GraphBuilder with two agents:

1. **Data Creation Agent** → Generates CSV files with mock transaction data
2. **Data Analysis Agent** → Analyzes the CSV file and creates a report

## 🏗️ Graph Structure

```
Data Creation → Data Analysis
```

The second agent receives both the original prompt and the output from the first agent.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- AWS credentials configured
- Access to Amazon Bedrock Claude models

### Installation
This example uses the 1.0.1 version of the Strands SDK (updated Graph Builder construct)
```bash
pip install strands-agents strands-agents-tools
```

### Run the Example
```bash
cd multi-agent-samples/Graph-Samples/Sequential-Graph
python main.py
```

## 📁 Project Structure

```
Sequential-Graph/
├── __init__.py     # Package initialization
├── config.py       # Model configuration and agent prompts
├── main.py         # Main execution logic
└── README.md       # This file
```

## 🔧 How It Works

```python
# 1. Build the graph
builder = GraphBuilder()
builder.add_node(data_creation_agent, "data_creation")
builder.add_node(data_analysis_agent, "data_analysis")
builder.add_edge("data_creation", "data_analysis")  # Sequential dependency
builder.set_entry_point("data_creation")

# 2. Execute
graph = builder.build()
result = graph("Your prompt here")
```

## 📊 Example Output

```
Graph Execution Finished!
Final Status: COMPLETED
Graph execution successful!
Execution order: ['data_creation', 'data_analysis']
```

The agents will create CSV files and analysis reports in the current directory.

## 🛠️ Customization

- **Modify prompts**: Edit `config.py` to change agent behavior
- **Change model**: Update `MODEL_CONFIG` in `config.py`
- **Add more agents**: Extend the graph in `build_sequential_graph()`

## 📝 Files Created

When you run the example, it creates:
- `June.csv` - Mock transaction data
- `June.txt` - Analysis report

This example demonstrates the core GraphBuilder pattern for building deterministic multi-agent workflows. 