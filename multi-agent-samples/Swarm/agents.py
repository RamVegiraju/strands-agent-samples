from strands import Agent
from strands.models import BedrockModel
from config import (
    MODEL_CONFIG,
    INFORMATIVE_TRAVEL_PROMPT,
    HOTEL_RECOMMENDATION_PROMPT,
    FLIGHT_AGENT_PROMPT,
    ACTIVITIES_AGENT_PROMPT,
    ITINERARY_AGENT_PROMPT
)

def get_model():
    """Create and return the configured model."""
    return BedrockModel(**MODEL_CONFIG)

def create_travel_agents():
    """Create and return all travel-related agents."""
    informative = Agent(
        name="informative",
        model=get_model(),
        system_prompt=INFORMATIVE_TRAVEL_PROMPT,
    )

    hotel = Agent(
        name="hotel",
        model=get_model(),
        system_prompt=HOTEL_RECOMMENDATION_PROMPT,
    )

    flight = Agent(
        name="flight",
        model=get_model(),
        system_prompt=FLIGHT_AGENT_PROMPT,
    )

    activities = Agent(
        name="activities",
        model=get_model(),
        system_prompt=ACTIVITIES_AGENT_PROMPT,
    )

    itinerary = Agent(
        name="itinerary",
        model=get_model(),
        system_prompt=ITINERARY_AGENT_PROMPT,
    )

    return [informative, hotel, flight, activities, itinerary] 