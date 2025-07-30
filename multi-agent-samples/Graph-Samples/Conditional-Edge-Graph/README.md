# Conditional Edge Graph

Stock trading decision system using conditional graph routing in Strands.

## How it Works

1. **Retriever** gets mock stock price
2. **Conditional routing** based on price:
   - Price < $500 → Buy agent  
   - Price > $500 → Sell agent
3. **Agent** makes buy/sell recommendation

## Quick Start

```bash
python main.py
```

## Structure

```
├── main.py      # Main execution
├── config.py    # Model & prompts  
├── tools.py     # Stock price tool
├── utils.py     # Routing logic
└── README.md    # This file
```

## Example Output

```
📊 CONDITIONAL GRAPH RESULTS
📈 Status: completed
🔄 Execution Order: ['retriever', 'buyer']
💰 Stock Price: $239
�� Decision: BUY
```