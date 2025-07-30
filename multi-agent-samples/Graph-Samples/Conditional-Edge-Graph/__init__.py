"""
Conditional Edge Graph - Strands Multi-Agent Example

A simple stock trading decision system using conditional graph routing.
Routes to buy/sell agents based on stock price thresholds.
"""

from .main import main, run_graph, build_conditional_graph
from .utils import extract_clean_results

__version__ = "1.0.0"
__all__ = ["main", "run_graph", "build_conditional_graph", "extract_clean_results"] 