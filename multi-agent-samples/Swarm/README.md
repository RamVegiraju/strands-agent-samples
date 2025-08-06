# Travel Planning Swarm

This sample demonstrates **swarm intelligence** using the Strands SDK to create a collaborative multi-agent system for travel planning.

## Overview

The swarm consists of 5 specialized agents that work together to create comprehensive travel itineraries:

- **Informative Agent**: Provides destination information and fun facts
- **Hotel Agent**: Recommends accommodations with pricing
- **Flight Agent**: Suggests airlines and flight options
- **Activities Agent**: Generates activity recommendations
- **Itinerary Agent**: Combines all information into a final travel plan

## Swarm Intelligence

This example explores how multiple AI agents can collaborate autonomously through:

- **Dynamic handoffs** between specialized agents
- **Collective decision making** for travel planning
- **Emergent behavior** from agent interactions
- **Self-organizing** workflow based on task requirements

## Quick Start

```bash
cd multi-agent-samples/Swarm
python main.py
```

## Structure

```
Swarm/
├── config.py      # Model configuration and agent prompts
├── agents.py      # Agent creation and initialization
├── main.py        # Main execution and swarm orchestration
└── README.md      # This file
```

## Example Output

The swarm will collaboratively plan a Tokyo trip, with agents automatically handing off tasks to create a complete itinerary including flights, hotels, and activities. 

## Additional Credits/Resources
Built off of the samples from the documentation and AWS Samples Repo below:
- https://github.com/strands-agents/samples/blob/main/01-tutorials/02-multi-agent-systems/02-swarm-agent/swarm.ipynb
- https://strandsagents.com/latest/documentation/docs/user-guide/concepts/multi-agent/swarm/#multi-modal-input-support
- Swarm Implementation: https://github.com/strands-agents/sdk-python/blob/main/src/strands/multiagent/swarm.py