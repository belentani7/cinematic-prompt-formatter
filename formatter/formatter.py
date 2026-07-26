"""
Main formatter for converting cinematic descriptions to AI prompts.
"""

import re
from typing import List, Optional

from formatter.mapper import (
    LENS_MAP,
    LIGHTING_MAP,
    CAMERA_MAP,
    MOOD_MAP,
    COLOR_MAP,
    map_single_term,
)
from formatter.presets import PRESETS, get_preset


def format_prompt(cinematic_description: str, style: Optional[str] = None, model: str = "sdxl") -> str:
    """
    Convert a cinematic description into an optimized prompt.

    Args:
        cinematic_description: Natural language cinematic terms (e.g., "dolly in, rim light, cyberpunk mood")
        style: Optional preset style name to apply
        model: Target model (sdxl, flux, sd15)

    Returns:
        Formatted prompt string with weighted tags

    Example:
        >>> format_prompt("dolly in, rim light, cyberpunk mood")
        '(dolly zoom, vertigo effect:1.1), (rim lighting, edge light:1.2), (cyberpunk, neon glow, rain:1.3)'
    """
    # Parse the description into individual terms
    terms = parse_description(cinematic_description)

    # Map each term to its prompt tag
    prompt_parts = []
    for term in terms:
        mapped = map_single_term(term)
        if mapped:
            prompt_parts.append(mapped)
        else:
            # Keep original term if no mapping found
            prompt_parts.append(f"({term})")

    # Build the base prompt
    base_prompt = ", ".join(prompt_parts)

    # Apply preset if specified
    if style:
        preset = get_preset(style)
        if preset:
            base_prompt = apply_preset(base_prompt, preset)

    # Optimize for target model
    optimized = optimize_for_model(base_prompt, model)

    return optimized


def format_batch(descriptions: List[str], style: Optional[str] = None, model: str = "sdxl") -> List[str]:
    """
    Format multiple cinematic descriptions.

    Args:
        descriptions: List of cinematic descriptions
        style: Optional preset style name
        model: Target model

    Returns:
        List of formatted prompts
    """
    return [format_prompt(desc, style=style, model=model) for desc in descriptions]


def optimize_for_model(prompt: str, model: str) -> str:
    """
    Optimize a prompt for a specific AI model.

    Args:
        prompt: Base formatted prompt
        model: Target model (sdxl, flux, sd15)

    Returns:
        Model-optimized prompt
    """
    model_lower = model.lower().strip()

    if model_lower in ("sdxl", "sdxl-1.0", "sdxl-turbo"):
        return optimize_sdxl(prompt)
    elif model_lower in ("flux", "flux-1", "flux-schnell", "flux-dev"):
        return optimize_flux(prompt)
    elif model_lower in ("sd15", "sd-1.5", "stable-diffusion-v1-5"):
        return optimize_sd15(prompt)
    else:
        return prompt


def optimize_sdxl(prompt: str) -> str:
    """
    Optimize prompt for SDXL.
    SDXL responds well to weighted tokens and detailed descriptions.
    """
    # SDXL likes quality boosters
    boosters = [
        "masterpiece",
        "best quality",
        "highly detailed",
        "professional",
    ]

    # Add boosters at the beginning
    optimized = ", ".join(boosters) + ", " + prompt

    return optimized


def optimize_flux(prompt: str) -> str:
    """
    Optimize prompt for Flux.
    Flux works better with natural language and less weighting.
    """
    # Convert weight syntax for Flux
    # Flux doesn't use (token:weight) as much, prefers natural language
    optimized = re.sub(r'\(([^:]+):(\d+\.?\d*)\)', r'\1', prompt)

    # Clean up any double commas or spaces
    optimized = re.sub(r',\s*,', ',', optimized)
    optimized = re.sub(r'\s+', ' ', optimized)

    # Add quality terms in natural language
    optimized = "professional photography, " + optimized

    return optimized.strip()


def optimize_sd15(prompt: str) -> str:
    """
    Optimize prompt for Stable Diffusion 1.5.
    SD1.5 responds well to weighted tokens and specific triggers.
    """
    # SD1.5 likes quality boosters
    boosters = [
        "masterpiece",
        "best quality",
        "highly detailed",
    ]

    # Add boosters
    optimized = ", ".join(boosters) + ", " + prompt

    # Ensure weights are in valid range (SD1.5 can be sensitive)
    def cap_weight(match):
        token = match.group(1)
        weight = float(match.group(2))
        # Cap at 1.5 for SD1.5 stability
        weight = min(weight, 1.5)
        if weight == int(weight):
            weight = int(weight)
        return f"({token}:{weight})"

    optimized = re.sub(r'\(([^:]+):(\d+\.?\d*)\)', cap_weight, optimized)

    return optimized


def apply_preset(prompt: str, preset: dict) -> str:
    """
    Apply a preset style to a prompt.

    Args:
        prompt: Base formatted prompt
        preset: Preset dictionary with prefix, suffix, and modifiers

    Returns:
        Prompt with preset applied
    """
    parts = []

    # Add preset prefix
    if "prefix" in preset:
        parts.append(preset["prefix"])

    # Add the original prompt
    parts.append(prompt)

    # Add preset suffix
    if "suffix" in preset:
        parts.append(preset["suffix"])

    # Add any additional modifiers
    if "modifiers" in preset:
        parts.extend(preset["modifiers"])

    return ", ".join(parts)


def parse_description(description: str) -> List[str]:
    """
    Parse a natural language cinematic description into individual terms.

    Args:
        description: Natural language description

    Returns:
        List of individual terms
    """
    # Split by commas, "and", or just spaces with proper noun detection
    # Handle common separators
    description = description.replace(" and ", ", ")
    description = description.replace(" with ", ", ")

    # Split by comma
    terms = [t.strip() for t in description.split(",")]

    # Further split by space if we have multi-word terms that should be single
    # But keep certain multi-word terms together
    multi_word_terms = {
        "dolly in", "dolly out", "dolly zoom", "rim light", "low key",
        "high key", "soft light", "hard light", "golden hour", "blue hour",
        "god rays", "push in", "pull out", "zoom in", "zoom out",
        "rack focus", "whip pan", "fly on wall", "over shoulder",
        "low angle", "high angle", "birds eye", "worms eye",
        "film noir", "neo noir", "post apocalyptic", "music video",
        "teal orange", "black and white", "high saturation",
        "high contrast", "low contrast", "lifted blacks", "crushed blacks",
        "film grain", "color shifted", "split tone", "film stock",
    }

    result = []
    for term in terms:
        term_lower = term.lower().strip()
        if term_lower in multi_word_terms:
            result.append(term_lower.replace(" ", "_"))
        else:
            # Check if it's a single term or needs splitting
            words = term.split()
            if len(words) > 1:
                # Try joining as-is first
                joined = "_".join(w.lower() for w in words)
                if map_single_term(joined):
                    result.append(joined)
                else:
                    # Try individual words
                    for word in words:
                        if map_single_term(word.lower()):
                            result.append(word.lower())
            else:
                result.append(term_lower)

    return [t for t in result if t]


def list_available_terms():
    """List all available cinematic terms organized by category."""
    from formatter.mapper import get_all_terms
    return get_all_terms()


def search_terms(query: str):
    """Search for terms matching a query."""
    from formatter.mapper import search_terms as mapper_search
    return mapper_search(query)