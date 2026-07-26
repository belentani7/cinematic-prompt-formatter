"""
Cinematic Prompt Formatter - Translate cinematic language into AI image generation prompts.
"""

__version__ = "0.1.0"
__author__ = "Cinematic Prompt Formatter Contributors"

from formatter.formatter import format_prompt, format_batch, optimize_for_model
from formatter.parser import parse_lens, parse_lighting, parse_camera, parse_mood
from formatter.mapper import map_to_prompt
from formatter.presets import PRESETS, get_preset

__all__ = [
    "format_prompt",
    "format_batch",
    "optimize_for_model",
    "parse_lens",
    "parse_lighting",
    "parse_camera",
    "parse_mood",
    "map_to_prompt",
    "PRESETS",
    "get_preset",
]