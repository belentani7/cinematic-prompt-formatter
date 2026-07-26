"""
Preset styles for common cinematic looks.
"""

from typing import Dict, Optional, Any

# =============================================================================
# PRESET DEFINITIONS
# =============================================================================

PRESETS: Dict[str, Dict[str, Any]] = {
    "hollywood_cinematic": {
        "name": "Hollywood Cinematic",
        "description": "Big budget Hollywood blockbuster look",
        "prefix": "cinematic film still, professional,",
        "suffix": ", cinematic color grading, dramatic lighting, film grain, anamorphic lens",
        "modifiers": [
            "(film grain:0.8)",
            "(cinematic color grading:1.2)",
            "(dramatic lighting:1.1)",
            "(depth of field:1.1)",
        ],
        "recommended_terms": ["anamorphic", "rim_light", "dolly_in", "dramatic"],
        "optimal_weights": {
            "lens": 1.3,
            "lighting": 1.2,
            "camera": 1.1,
            "mood": 1.1,
        },
    },
    "indie_film": {
        "name": "Indie Film",
        "description": "Independent film aesthetic, raw and authentic",
        "prefix": "indie film still, natural,",
        "suffix": ", natural lighting, film grain, 35mm film, handheld feel",
        "modifiers": [
            "(film grain:0.9)",
            "(natural lighting:1.1)",
            "(handheld:0.8)",
            "(authentic:1.0)",
        ],
        "recommended_terms": ["35mm", "natural", "handheld", "gritty", "moody"],
        "optimal_weights": {
            "lens": 1.1,
            "lighting": 1.0,
            "camera": 0.9,
            "mood": 1.0,
        },
    },
    "music_video": {
        "name": "Music Video",
        "description": "Stylized music video aesthetic",
        "prefix": "music video still, stylized,",
        "suffix": ", vibrant colors, dynamic lighting, high contrast, neon glow",
        "modifiers": [
            "(vibrant colors:1.2)",
            "(dynamic lighting:1.1)",
            "(high contrast:1.1)",
            "(stylized:1.2)",
        ],
        "recommended_terms": ["neon", "high_saturation", "dynamic", "energetic", "cyberpunk"],
        "optimal_weights": {
            "lens": 1.0,
            "lighting": 1.2,
            "camera": 1.1,
            "mood": 1.2,
        },
    },
    "commercial": {
        "name": "Commercial",
        "description": "Clean commercial/advertising look",
        "prefix": "professional commercial photograph,",
        "suffix": ", studio lighting, clean background, product photography, high resolution",
        "modifiers": [
            "(studio lighting:1.2)",
            "(clean:1.1)",
            "(professional:1.2)",
            "(high resolution:1.0)",
        ],
        "recommended_terms": ["studio", "soft_light", "clean", "minimalist", "bright"],
        "optimal_weights": {
            "lens": 1.0,
            "lighting": 1.2,
            "camera": 1.0,
            "mood": 0.9,
        },
    },
    "anime": {
        "name": "Anime",
        "description": "Anime-inspired aesthetic",
        "prefix": "anime style, cel shading,",
        "suffix": ", vibrant colors, detailed eyes, anime aesthetic, Japanese animation",
        "modifiers": [
            "(anime:1.3)",
            "(cel shading:1.1)",
            "(vibrant:1.2)",
            "(detailed eyes:1.0)",
        ],
        "recommended_terms": ["vibrant", "fantasy", "magical", "dramatic", "ethereal"],
        "optimal_weights": {
            "lens": 0.9,
            "lighting": 1.1,
            "camera": 0.8,
            "mood": 1.3,
        },
    },
    "realistic": {
        "name": "Realistic",
        "description": "Photorealistic style",
        "prefix": "photorealistic, hyperrealistic,",
        "suffix": ", sharp focus, high detail, professional photography, 8K UHD",
        "modifiers": [
            "(photorealistic:1.3)",
            "(sharp focus:1.2)",
            "(high detail:1.1)",
            "(8K UHD:0.9)",
        ],
        "recommended_terms": ["natural", "daylight", "50mm", "clean", "natural_light"],
        "optimal_weights": {
            "lens": 1.2,
            "lighting": 1.1,
            "camera": 1.0,
            "mood": 0.9,
        },
    },
    "horror": {
        "name": "Horror",
        "description": "Dark horror aesthetic",
        "prefix": "horror film still, dark,",
        "suffix": ", eerie lighting, shadows, unsettling atmosphere, film grain",
        "modifiers": [
            "(eerie:1.2)",
            "(shadows:1.1)",
            "(unsettling:1.2)",
            "(dark:1.1)",
        ],
        "recommended_terms": ["low_key", "handheld", "horror", "ominous", "tense"],
        "optimal_weights": {
            "lens": 1.0,
            "lighting": 1.3,
            "camera": 1.1,
            "mood": 1.3,
        },
    },
    "noir": {
        "name": "Film Noir",
        "description": "Classic film noir aesthetic",
        "prefix": "film noir, black and white,",
        "suffix": ", high contrast, chiaroscuro, dramatic shadows, venetian blinds",
        "modifiers": [
            "(black and white:1.2)",
            "(high contrast:1.3)",
            "(chiaroscuro:1.2)",
            "(dramatic:1.1)",
        ],
        "recommended_terms": ["noir", "chiaroscuro", "low_key", "dutch", "tense"],
        "optimal_weights": {
            "lens": 1.1,
            "lighting": 1.3,
            "camera": 1.1,
            "mood": 1.4,
        },
    },
    "cyberpunk": {
        "name": "Cyberpunk",
        "description": "Neon-soaked cyberpunk aesthetic",
        "prefix": "cyberpunk, futuristic,",
        "suffix": ", neon glow, rain, holograms, dystopian, high-tech",
        "modifiers": [
            "(neon:1.3)",
            "(futuristic:1.2)",
            "(dystopian:1.1)",
            "(high contrast:1.1)",
        ],
        "recommended_terms": ["cyberpunk", "neon", "futuristic", "moody", "dramatic"],
        "optimal_weights": {
            "lens": 1.0,
            "lighting": 1.3,
            "camera": 1.0,
            "mood": 1.3,
        },
    },
    "fantasy": {
        "name": "Fantasy",
        "description": "Magical fantasy aesthetic",
        "prefix": "fantasy, magical,",
        "suffix": ", enchanted, ethereal glow, mystical atmosphere, soft light",
        "modifiers": [
            "(magical:1.2)",
            "(ethereal:1.1)",
            "(enchanted:1.1)",
            "(soft light:1.0)",
        ],
        "recommended_terms": ["fantasy", "ethereal", "magical", "soft_light", "mystical"],
        "optimal_weights": {
            "lens": 1.0,
            "lighting": 1.1,
            "camera": 0.9,
            "mood": 1.3,
        },
    },
    "vintage": {
        "name": "Vintage",
        "description": "Nostalgic vintage film look",
        "prefix": "vintage photograph, retro,",
        "suffix": ", film grain, faded colors, warm tones, analog film",
        "modifiers": [
            "(film grain:1.0)",
            "(vintage:1.2)",
            "(warm tones:1.1)",
            "(faded:1.0)",
        ],
        "recommended_terms": ["vintage", "warm", "sepia", "film_grain", "nostalgic"],
        "optimal_weights": {
            "lens": 1.0,
            "lighting": 1.0,
            "camera": 1.0,
            "mood": 1.2,
        },
    },
    "documentary": {
        "name": "Documentary",
        "description": "Realistic documentary style",
        "prefix": "documentary photograph, candid,",
        "suffix": ", natural light, photojournalistic, authentic, available light",
        "modifiers": [
            "(documentary:1.1)",
            "(natural:1.2)",
            "(authentic:1.1)",
            "(candid:1.0)",
        ],
        "recommended_terms": ["natural", "handheld", "documentary", "realistic", "candid"],
        "optimal_weights": {
            "lens": 1.1,
            "lighting": 1.0,
            "camera": 1.0,
            "mood": 0.9,
        },
    },
    "ethereal": {
        "name": "Ethereal",
        "description": "Otherworldly, dreamlike aesthetic",
        "prefix": "ethereal, otherworldly,",
        "suffix": ", soft glow, dreamy, soft focus, pastel colors, angelic",
        "modifiers": [
            "(ethereal:1.3)",
            "(soft focus:1.1)",
            "(dreamy:1.2)",
            "(glow:1.1)",
        ],
        "recommended_terms": ["ethereal", "soft", "dreamy", "mystical", "pastel"],
        "optimal_weights": {
            "lens": 1.0,
            "lighting": 1.1,
            "camera": 0.9,
            "mood": 1.3,
        },
    },
    "action": {
        "name": "Action",
        "description": "Dynamic action movie style",
        "prefix": "action film still, dynamic,",
        "suffix": ", motion blur, dramatic angle, intense, explosive",
        "modifiers": [
            "(dynamic:1.2)",
            "(intense:1.1)",
            "(dramatic:1.1)",
            "(motion:1.0)",
        ],
        "recommended_terms": ["handheld", "dynamic", "dramatic", "energetic", "tense"],
        "optimal_weights": {
            "lens": 1.0,
            "lighting": 1.1,
            "camera": 1.2,
            "mood": 1.1,
        },
    },
    "romance": {
        "name": "Romance",
        "description": "Romantic, emotional aesthetic",
        "prefix": "romantic, emotional,",
        "suffix": ", soft light, warm colors, intimate, tender, golden hour",
        "modifiers": [
            "(romantic:1.2)",
            "(soft:1.1)",
            "(intimate:1.1)",
            "(warm:1.0)",
        ],
        "recommended_terms": ["romantic", "soft", "golden_hour", "intimate", "warm"],
        "optimal_weights": {
            "lens": 1.1,
            "lighting": 1.1,
            "camera": 0.9,
            "mood": 1.2,
        },
    },
}


def get_preset(name: str) -> Optional[Dict[str, Any]]:
    """
    Get a preset by name.

    Args:
        name: Preset name (case-insensitive)

    Returns:
        Preset dictionary or None if not found
    """
    name_lower = name.lower().strip().replace(" ", "_").replace("-", "_")
    return PRESETS.get(name_lower)


def list_presets() -> Dict[str, str]:
    """
    List all available presets.

    Returns:
        Dictionary mapping preset names to descriptions
    """
    return {
        name: preset["description"]
        for name, preset in PRESETS.items()
    }


def get_preset_names() -> list:
    """Get list of all preset names."""
    return list(PRESETS.keys())


def get_recommended_terms(preset_name: str) -> list:
    """Get recommended terms for a preset."""
    preset = get_preset(preset_name)
    if preset:
        return preset.get("recommended_terms", [])
    return []


def get_optimal_weights(preset_name: str) -> dict:
    """Get optimal weight multipliers for a preset."""
    preset = get_preset(preset_name)
    if preset:
        return preset.get("optimal_weights", {})
    return {}