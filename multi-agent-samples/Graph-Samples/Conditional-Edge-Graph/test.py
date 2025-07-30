import random
from strands.multiagent import GraphBuilder
from strands.models import BedrockModel
from strands import Agent
from strands import tool
import re

def extract_clean_results(graph_result):
    """
    Clean result extraction using Strands GraphState properties.
    Based on Strands documentation: https://strandsagents.com/latest/documentation/docs/user-guide/concepts/multi-agent/graph/
    """
    results = {
        'status': graph_result.status,
        'execution_order': [node.node_id for node in graph_result.execution_order],
        'completed_count': graph_result.completed_nodes,
        'failed_count': graph_result.failed_nodes,
        'total_execution_time': sum(node.execution_time for node in graph_result.execution_order),
        'total_tokens': graph_result.accumulated_usage['totalTokens'],
        'node_results': {}
    }
    
    # Extract individual node results
    for node_id, node_result in graph_result.results.items():
        results['node_results'][node_id] = node_result.result.message['content'][0]['text']
    
    return results

# Model configuration
MODEL_CONFIG = {
    "model_id": "us.anthropic.claude-sonnet-4-20250514-v1:0",
    "region_name": "us-east-1"
}

model = BedrockModel(**MODEL_CONFIG)

# tool to calculate stock price
@tool
def stock_price_calculator(stock_name: str) -> dict:
    print(f"Calculating stock price for {stock_name}")
    stock_price = random.randint(100, 1000)
    return {f"Current price of {stock_name}": stock_price}

def submit_buy(state):
    #print(state)
    stock_retriever_result = state.results.get("retriever")
    if not stock_retriever_result:
        return False
    
    # Get the text content from the AgentResult
    agent_result = stock_retriever_result.result
    text_content = agent_result.message['content'][0]['text']
    #print(f"Text content: {text_content}")
    
    # Parse the price from the text (handle both $891 and plain 891)
    price_matches = re.findall(r'\$?(\d+)', text_content)
    
    if price_matches:
        result = int(price_matches[0])
        if result < 500:
            print(f"🟢 Routing to BUYER: Stock price ${result} < $500")
            return True
        return False
    
    return False


def submit_sell(state):
    #print(state)
    stock_retriever_result = state.results.get("retriever")
    if not stock_retriever_result:
        return False
    
    # Get the text content from the AgentResult
    agent_result = stock_retriever_result.result
    text_content = agent_result.message['content'][0]['text']
    #print(f"Text content: {text_content}")
    
    # Parse the price from the text (handle both $891 and plain 891)
    price_matches = re.findall(r'\$?(\d+)', text_content)
    
    if price_matches:
        result = int(price_matches[0])
        if result > 500:
            print(f"🔴 Routing to SELLER: Stock price ${result} > $500")
            return True
        return False
    
    return False

RETRIEVER_PROMPT = """You are a stock retriever agent. You are given a stock name and you use the stock_price_calculator tool to get a mock price of the stock.

You then return the price in a message, don't give any other information or recommendations.
"""

BUY_PROMPT = """You are a buy agent. You receive a stock price from the retriever agent and should recommend BUYING the stock. 

Use the price that was provided by the previous agent and make a buy recommendation. Don't worry about real-world prices - just use the retriever's price data to make your buy decision, no need to mention any reasoning or details.

Output Format: Recommend BUY for [STOCK] at $[PRICE].
"""

SELL_PROMPT = """You are a sell agent. You receive a stock price from the retriever agent and should recommend SELLING the stock.

Use the price that was provided by the previous agent and make a sell recommendation. Don't worry about real-world prices - just use the retriever's price data to make your sell decision, no need to mention any reasoning or details.

OutputFormat: Recommend SELL for [STOCK] at $[PRICE].
"""

retriever_agent = Agent(
    model=model,
    tools=[stock_price_calculator],
    system_prompt=RETRIEVER_PROMPT
)

buy_agent = Agent(
    model=model,
    system_prompt=BUY_PROMPT
)

sell_agent = Agent(
    model=model,
    system_prompt=SELL_PROMPT
)

builder = GraphBuilder()

# Add nodes to the graph
builder.add_node(retriever_agent, "retriever")
builder.add_node(buy_agent, "buyer")
builder.add_node(sell_agent, "seller")

# Add conditional edges based on the stock price
builder.add_edge("retriever", "buyer", condition=submit_buy)
builder.add_edge("retriever", "seller", condition=submit_sell)

# Set the entry point
builder.set_entry_point("retriever")

# Build the graph
graph = builder.build()

result = graph("I want to see what to do with Apple stock, get the stock price and make a decision to buy or sell.")

# Method 1: Using helper function for clean parsing
clean_results = extract_clean_results(result)

print("\n" + "="*50)
print("📊 CLEAN GRAPH RESULTS")
print("="*50)
print(f"📈 Status: {clean_results['status']}")
print(f"🔄 Execution Order: {clean_results['execution_order']}")
print(f"✅ Completed: {clean_results['completed_count']} | ❌ Failed: {clean_results['failed_count']}")

# Show stock price and decision
stock_price = clean_results['node_results']['retriever']
print(f"\n💰 Stock Price: ${stock_price}")

if 'buyer' in clean_results['node_results']:
    print(f"🟢 Decision: BUY")
    print(f"📝 Details: {clean_results['node_results']['buyer']}")
elif 'seller' in clean_results['node_results']:
    print(f"🔴 Decision: SELL") 
    print(f"📝 Details: {clean_results['node_results']['seller']}")

print(f"\n⏱️  Execution Time: {clean_results['total_execution_time']}ms")
print(f"💸 Tokens Used: {clean_results['total_tokens']}")
print("="*50) 