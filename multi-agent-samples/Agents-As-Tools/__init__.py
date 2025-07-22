"""Agents Orchestrator Package - A multi-agent system for specialized task routing."""

from .orchestrator import AgentsOrchestrator
from .config import get_model
from .tools import get_available_tools

__version__ = "1.0.0"
__author__ = "Your Name"
__description__ = "A multi-agent orchestrator system using Strands SDK"

__all__ = [
    "AgentsOrchestrator",
    "get_model",
    "get_available_tools"
] 