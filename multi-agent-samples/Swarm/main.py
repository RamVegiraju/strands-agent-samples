import logging
from strands.multiagent import Swarm
from agents import create_travel_agents

def setup_logging():
    """Configure logging for the swarm."""
    logging.getLogger("strands.multiagent").setLevel(logging.DEBUG)
    logging.basicConfig(
        format="%(levelname)s | %(name)s | %(message)s",
        handlers=[logging.StreamHandler()]
    )

def create_swarm(agents):
    """Create and configure the travel planning swarm."""
    return Swarm(
        agents,
        max_handoffs=20,
        max_iterations=20,
        execution_timeout=900.0,  # 15 minutes
        node_timeout=300.0,       # 5 minutes per agent
        repetitive_handoff_detection_window=8,  # There must be >= 3 unique agents in the last 8 handoffs
        repetitive_handoff_min_unique_agents=3
    )

def main():
    """Main execution function."""
    setup_logging()
    agents = create_travel_agents()
    swarm = create_swarm(agents)
    
    result = swarm("Plan me a trip to Tokyo, generate me an end to end itinerary that includes flights, hotels, and activities.")
    print(f"Status: {result.status}")
    print(f"Node history: {[node.node_id for node in result.node_history]}")

if __name__ == "__main__":
    main()