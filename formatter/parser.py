"""
Parse cinematic terms into structured dictionaries.
"""

from typing import Dict, Optional


def parse_lens(term: str) -> Dict[str, str]:
    """
    Parse a lens term into its components.

    Args:
        term: Lens term to parse (e.g., 'anamorphic', '35mm', '85mm')

    Returns:
        Dictionary with focal_length, type, and characteristics
    """
    term_lower = term.lower().strip()

    lens_data = {
        "anamorphic": {
            "focal_length": "variable",
            "type": "anamorphic",
            "characteristics": "oval bokeh, lens flares, 2.39:1 aspect ratio, cinematic"
        },
        "35mm": {
            "focal_length": "35mm",
            "type": "wide-normal",
            "characteristics": "natural perspective, slight wide angle, versatile"
        },
        "50mm": {
            "focal_length": "50mm",
            "type": "standard",
            "characteristics": "human eye perspective, natural, minimal distortion"
        },
        "85mm": {
            "focal_length": "85mm",
            "type": "portrait",
            "characteristics": "flattering compression, shallow depth of field, bokeh"
        },
        "135mm": {
            "focal_length": "135mm",
            "type": "telephoto",
            "characteristics": "extreme compression, background separation, intimate"
        },
        "24mm": {
            "focal_length": "24mm",
            "type": "wide",
            "characteristics": "dramatic distortion, expansive, environmental"
        },
        "14mm": {
            "focal_length": "14mm",
            "type": "ultra-wide",
            "characteristics": "extreme perspective, barrel distortion, immersive"
        },
        "fisheye": {
            "focal_length": "8-15mm",
            "type": "fisheye",
            "characteristics": "circular distortion, 180-degree view, surreal"
        },
        "tilt-shift": {
            "focal_length": "variable",
            "type": "tilt-shift",
            "characteristics": "miniature effect, selective focus, architectural"
        },
        "macro": {
            "focal_length": "60-200mm",
            "type": "macro",
            "characteristics": "extreme close-up, 1:1 magnification, detail"
        },
        "telephoto": {
            "focal_length": "200mm+",
            "type": "super-telephoto",
            "characteristics": "compression, wildlife, sports, surveillance"
        },
        "prime": {
            "focal_length": "variable",
            "type": "prime",
            "characteristics": "fixed focal length, sharp, fast aperture"
        },
        "zoom": {
            "focal_length": "variable",
            "type": "zoom",
            "characteristics": "versatile, variable focal length, convenience"
        },
    }

    if term_lower in lens_data:
        return lens_data[term_lower]

    return {
        "focal_length": "unknown",
        "type": "unknown",
        "characteristics": term_lower
    }


def parse_lighting(term: str) -> Dict[str, str]:
    """
    Parse a lighting term into its components.

    Args:
        term: Lighting term to parse (e.g., 'rim_light', 'low_key')

    Returns:
        Dictionary with type, direction, intensity, and color
    """
    term_lower = term.lower().strip().replace(" ", "_").replace("-", "_")

    lighting_data = {
        "rim_light": {
            "type": "rim",
            "direction": "behind",
            "intensity": "moderate",
            "color": "neutral or warm"
        },
        "rim": {
            "type": "rim",
            "direction": "behind",
            "intensity": "moderate",
            "color": "neutral or warm"
        },
        "low_key": {
            "type": "low-key",
            "direction": "side",
            "intensity": "low",
            "color": "cool or neutral"
        },
        "low-key": {
            "type": "low-key",
            "direction": "side",
            "intensity": "low",
            "color": "cool or neutral"
        },
        "high_key": {
            "type": "high-key",
            "direction": "multiple",
            "intensity": "high",
            "color": "bright, neutral"
        },
        "high-key": {
            "type": "high-key",
            "direction": "multiple",
            "intensity": "high",
            "color": "bright, neutral"
        },
        "chiaroscuro": {
            "type": "chiaroscuro",
            "direction": "side",
            "intensity": "high contrast",
            "color": "warm highlights, cool shadows"
        },
        "backlight": {
            "type": "back",
            "direction": "behind",
            "intensity": "moderate to high",
            "color": "varies"
        },
        "back": {
            "type": "back",
            "direction": "behind",
            "intensity": "moderate to high",
            "color": "varies"
        },
        "soft_light": {
            "type": "soft",
            "direction": "diffused",
            "intensity": "low to moderate",
            "color": "neutral"
        },
        "soft": {
            "type": "soft",
            "direction": "diffused",
            "intensity": "low to moderate",
            "color": "neutral"
        },
        "hard_light": {
            "type": "hard",
            "direction": "direct",
            "intensity": "high",
            "color": "neutral"
        },
        "hard": {
            "type": "hard",
            "direction": "direct",
            "intensity": "high",
            "color": "neutral"
        },
        "golden_hour": {
            "type": "golden hour",
            "direction": "low angle",
            "intensity": "moderate",
            "color": "warm golden"
        },
        "golden": {
            "type": "golden hour",
            "direction": "low angle",
            "intensity": "moderate",
            "color": "warm golden"
        },
        "blue_hour": {
            "type": "blue hour",
            "direction": "ambient",
            "intensity": "low",
            "color": "cool blue"
        },
        "blue": {
            "type": "blue hour",
            "direction": "ambient",
            "intensity": "low",
            "color": "cool blue"
        },
        "neon": {
            "type": "neon",
            "direction": "multiple",
            "intensity": "moderate to high",
            "color": "vibrant, saturated"
        },
        "practical": {
            "type": "practical",
            "direction": "in-scene",
            "intensity": "varies",
            "color": "varies"
        },
        "key_light": {
            "type": "key",
            "direction": "45 degrees",
            "intensity": "primary",
            "color": "neutral"
        },
        "fill_light": {
            "type": "fill",
            "direction": "opposite key",
            "intensity": "secondary",
            "color": "neutral"
        },
        "top_light": {
            "type": "top",
            "direction": "overhead",
            "intensity": "moderate",
            "color": "neutral"
        },
        "under_light": {
            "type": "under",
            "direction": "below",
            "intensity": "moderate",
            "color": "often cool"
        },
        "motivated": {
            "type": "motivated",
            "direction": "scene-dictated",
            "intensity": "natural",
            "color": "contextual"
        },
        "natural": {
            "type": "natural",
            "direction": "ambient",
            "intensity": "varies",
            "color": "daylight balanced"
        },
        "studio": {
            "type": "studio",
            "direction": "controlled",
            "intensity": "controlled",
            "color": "adjustable"
        },
        "volumetric": {
            "type": "volumetric",
            "direction": "atmospheric",
            "intensity": "moderate",
            "color": "light shafts"
        },
        "god_rays": {
            "type": "god rays",
            "direction": "through openings",
            "intensity": "moderate",
            "color": "warm"
        },
        "moonlight": {
            "type": "moonlight",
            "direction": "overhead",
            "intensity": "low",
            "color": "cool blue"
        },
        "candlelight": {
            "type": "candlelight",
            "direction": "point source",
            "intensity": "low",
            "color": "warm orange"
        },
        "firelight": {
            "type": "firelight",
            "direction": "point source",
            "intensity": "low to moderate",
            "color": "warm orange"
        },
        "fluorescent": {
            "type": "fluorescent",
            "direction": "overhead",
            "intensity": "moderate",
            "color": "cool, greenish"
        },
        "tungsten": {
            "type": "tungsten",
            "direction": "point source",
            "intensity": "moderate",
            "color": "warm orange"
        },
        "daylight": {
            "type": "daylight",
            "direction": "natural",
            "intensity": "high",
            "color": "5600K balanced"
        },
        "mixed": {
            "type": "mixed",
            "direction": "multiple",
            "intensity": "varies",
            "color": "color temperature contrast"
        },
    }

    if term_lower in lighting_data:
        return lighting_data[term_lower]

    return {
        "type": term_lower,
        "direction": "unknown",
        "intensity": "unknown",
        "color": "unknown"
    }


def parse_camera(term: str) -> Dict[str, str]:
    """
    Parse a camera movement term into its components.

    Args:
        term: Camera movement term (e.g., 'dolly_in', 'steadicam')

    Returns:
        Dictionary with movement, speed, and angle
    """
    term_lower = term.lower().strip().replace(" ", "_").replace("-", "_")

    camera_data = {
        "dolly_in": {
            "movement": "dolly in",
            "speed": "slow to moderate",
            "angle": "eye level"
        },
        "dolly_out": {
            "movement": "dolly out",
            "speed": "slow to moderate",
            "angle": "eye level"
        },
        "dolly": {
            "movement": "dolly",
            "speed": "moderate",
            "angle": "eye level"
        },
        "steadicam": {
            "movement": "steadicam",
            "speed": "smooth, variable",
            "angle": "eye level"
        },
        "handheld": {
            "movement": "handheld",
            "speed": "erratic",
            "angle": "variable"
        },
        "crane": {
            "movement": "crane",
            "speed": "sweeping",
            "angle": "elevated"
        },
        "tracking": {
            "movement": "tracking",
            "speed": "moderate",
            "angle": "eye level"
        },
        "pan": {
            "movement": "pan",
            "speed": "slow to fast",
            "angle": "fixed height"
        },
        "tilt": {
            "movement": "tilt",
            "speed": "slow to fast",
            "angle": "fixed position"
        },
        "whip_pan": {
            "movement": "whip pan",
            "speed": "very fast",
            "angle": "fixed height"
        },
        "drone": {
            "movement": "aerial drone",
            "speed": "variable",
            "angle": "elevated, bird's eye"
        },
        "aerial": {
            "movement": "aerial",
            "speed": "variable",
            "angle": "elevated"
        },
        "orbit": {
            "movement": "orbit",
            "speed": "slow to moderate",
            "angle": "eye level"
        },
        "push_in": {
            "movement": "push in",
            "speed": "slow",
            "angle": "eye level"
        },
        "pull_out": {
            "movement": "pull out",
            "speed": "slow",
            "angle": "eye level"
        },
        "zoom_in": {
            "movement": "zoom in",
            "speed": "variable",
            "angle": "fixed"
        },
        "zoom_out": {
            "movement": "zoom out",
            "speed": "variable",
            "angle": "fixed"
        },
        "rack_focus": {
            "movement": "rack focus",
            "speed": "slow to fast",
            "angle": "fixed"
        },
        "static": {
            "movement": "static",
            "speed": "none",
            "angle": "fixed"
        },
        "locked_off": {
            "movement": "locked off",
            "speed": "none",
            "angle": "fixed"
        },
        "jib": {
            "movement": "jib",
            "speed": "smooth",
            "angle": "variable"
        },
        "slider": {
            "movement": "slider",
            "speed": "slow, smooth",
            "angle": "eye level"
        },
        "float": {
            "movement": "floating",
            "speed": "slow, ethereal",
            "angle": "eye level"
        },
        "swedish": {
            "movement": "Swedish angle",
            "speed": "static or moving",
            "angle": "dutch/canted"
        },
        "dutch": {
            "movement": "Dutch angle",
            "speed": "static or moving",
            "angle": "canted"
        },
        "canted": {
            "movement": "canted angle",
            "speed": "static or moving",
            "angle": "tilted"
        },
        "pov": {
            "movement": "POV",
            "speed": "subjective",
            "angle": "first person"
        },
        "fly_on_wall": {
            "movement": "fly on wall",
            "speed": "subtle",
            "angle": "observational"
        },
        "over_shoulder": {
            "movement": "over the shoulder",
            "speed": "static",
            "angle": "behind subject"
        },
        "OTS": {
            "movement": "over the shoulder",
            "speed": "static",
            "angle": "behind subject"
        },
        "low_angle": {
            "movement": "static",
            "speed": "none",
            "angle": "low angle"
        },
        "high_angle": {
            "movement": "static",
            "speed": "none",
            "angle": "high angle"
        },
        "birds_eye": {
            "movement": "static",
            "speed": "none",
            "angle": "bird's eye view"
        },
        "worms_eye": {
            "movement": "static",
            "speed": "none",
            "angle": "worm's eye view"
        },
        "following": {
            "movement": "following",
            "speed": "match subject",
            "angle": "behind"
        },
        "leading": {
            "movement": "leading",
            "speed": "match subject",
            "angle": "in front"
        },
        "circling": {
            "movement": "circling",
            "speed": "moderate",
            "angle": "eye level"
        },
        "descending": {
            "movement": "descending",
            "speed": "slow",
            "angle": "high to low"
        },
        "ascending": {
            "movement": "ascending",
            "speed": "slow",
            "angle": "low to high"
        },
    }

    if term_lower in camera_data:
        return camera_data[term_lower]

    return {
        "movement": term_lower,
        "speed": "unknown",
        "angle": "unknown"
    }


def parse_mood(term: str) -> Dict[str, str]:
    """
    Parse a mood/atmosphere term into its components.

    Args:
        term: Mood term (e.g., 'noir', 'cyberpunk', 'romantic')

    Returns:
        Dictionary with atmosphere, color_palette, and contrast
    """
    term_lower = term.lower().strip().replace(" ", "_").replace("-", "_")

    mood_data = {
        "noir": {
            "atmosphere": "mysterious, dangerous",
            "color_palette": "black and white, high contrast",
            "contrast": "very high"
        },
        "film_noir": {
            "atmosphere": "mysterious, dangerous",
            "color_palette": "black and white, high contrast",
            "contrast": "very high"
        },
        "cyberpunk": {
            "atmosphere": "dystopian, high-tech",
            "color_palette": "neon blues, pinks, purples",
            "contrast": "high"
        },
        "romantic": {
            "atmosphere": "soft, emotional, intimate",
            "color_palette": "warm pastels, soft tones",
            "contrast": "low to medium"
        },
        "horror": {
            "atmosphere": "dark, unsettling, tense",
            "color_palette": "desaturated, dark greens and blues",
            "contrast": "high"
        },
        "thriller": {
            "atmosphere": "tense, suspenseful",
            "color_palette": "cool tones, muted",
            "contrast": "medium to high"
        },
        "epic": {
            "atmosphere": "grand, sweeping, heroic",
            "color_palette": "rich, saturated",
            "contrast": "medium to high"
        },
        "intimate": {
            "atmosphere": "close, personal, warm",
            "color_palette": "warm, soft",
            "contrast": "low"
        },
        "surreal": {
            "atmosphere": "dreamlike, uncanny",
            "color_palette": "iridescent, shifting",
            "contrast": "varies"
        },
        "vintage": {
            "atmosphere": "nostalgic, warm, aged",
            "color_palette": "faded, sepia tones",
            "contrast": "low to medium"
        },
        "futuristic": {
            "atmosphere": "advanced, sleek, clean",
            "color_palette": "cool metallics, whites, blues",
            "contrast": "medium"
        },
        "post_apocalyptic": {
            "atmosphere": "desolate, decayed, abandoned",
            "color_palette": "desaturated earth tones",
            "contrast": "high"
        },
        "fantasy": {
            "atmosphere": "magical, enchanted, mythical",
            "color_palette": "jewel tones, ethereal glows",
            "contrast": "medium"
        },
        "western": {
            "atmosphere": "rugged, frontier, dusty",
            "color_palette": "warm earth tones, amber",
            "contrast": "medium to high"
        },
        "steampunk": {
            "atmosphere": "Victorian, mechanical, industrial",
            "color_palette": "copper, brass, warm browns",
            "contrast": "medium"
        },
        "ethereal": {
            "atmosphere": "otherworldly, delicate, transcendent",
            "color_palette": "soft whites, pastels, iridescent",
            "contrast": "low"
        },
        "gritty": {
            "atmosphere": "raw, realistic, harsh",
            "color_palette": "desaturated, urban tones",
            "contrast": "high"
        },
        "dreamy": {
            "atmosphere": "soft, hazy, romantic",
            "color_palette": "pastels, soft focus",
            "contrast": "low"
        },
        "melancholic": {
            "atmosphere": "sad, reflective, somber",
            "color_palette": "cool blues, grays",
            "contrast": "medium"
        },
        "energetic": {
            "atmosphere": "dynamic, vibrant, alive",
            "color_palette": "saturated, bold",
            "contrast": "high"
        },
        "calm": {
            "atmosphere": "peaceful, serene, tranquil",
            "color_palette": "soft blues, greens",
            "contrast": "low"
        },
        "mysterious": {
            "atmosphere": "enigmatic, unknown, hidden",
            "color_palette": "dark, shadows, muted",
            "contrast": "medium to high"
        },
        "magical": {
            "atmosphere": "enchanting, whimsical",
            "color_palette": "sparkles, glows, soft colors",
            "contrast": "medium"
        },
        "dark": {
            "atmosphere": "foreboding, ominous",
            "color_palette": "deep blacks, dark tones",
            "contrast": "high"
        },
        "light": {
            "atmosphere": "airy, bright, positive",
            "color_palette": "whites, soft colors",
            "contrast": "low"
        },
        "moody": {
            "atmosphere": "atmospheric, emotional",
            "color_palette": "varies, often cool tones",
            "contrast": "medium to high"
        },
        "atmospheric": {
            "atmosphere": "environmental, immersive",
            "color_palette": "contextual",
            "contrast": "varies"
        },
        "cinematic": {
            "atmosphere": "filmic, dramatic",
            "color_palette": "color graded, intentional",
            "contrast": "medium to high"
        },
        "dramatic": {
            "atmosphere": "intense, emotional",
            "color_palette": "high contrast tones",
            "contrast": "high"
        },
        "peaceful": {
            "atmosphere": "serene, quiet",
            "color_palette": "soft, muted",
            "contrast": "low"
        },
        "tense": {
            "atmosphere": "suspenseful, anxious",
            "color_palette": "cool, desaturated",
            "contrast": "high"
        },
        "whimsical": {
            "atmosphere": "playful, fanciful",
            "color_palette": "bright, varied",
            "contrast": "medium"
        },
        "gloomy": {
            "atmosphere": "dark, depressing",
            "color_palette": "grays, dark blues",
            "contrast": "low to medium"
        },
        "romantic": {
            "atmosphere": "love, passion",
            "color_palette": "reds, pinks, warm tones",
            "contrast": "medium"
        },
        "haunting": {
            "atmosphere": "eerie, lingering",
            "color_palette": "muted, ghostly",
            "contrast": "medium"
        },
        "nostalgic": {
            "atmosphere": "wistful, longing",
            "color_palette": "warm, faded",
            "contrast": "low to medium"
        },
        "aggressive": {
            "atmosphere": "confrontational, raw",
            "color_palette": "high contrast, bold",
            "contrast": "very high"
        },
        "serene": {
            "atmosphere": "calm, peaceful",
            "color_palette": "soft, natural",
            "contrast": "low"
        },
        "ominous": {
            "atmosphere": "threatening, foreboding",
            "color_palette": "dark, desaturated",
            "contrast": "high"
        },
        "hopeful": {
            "atmosphere": "optimistic, bright",
            "color_palette": "warm, light",
            "contrast": "medium"
        },
        "decadent": {
            "atmosphere": "luxurious, excess",
            "color_palette": "rich, opulent",
            "contrast": "medium"
        },
    }

    if term_lower in mood_data:
        return mood_data[term_lower]

    return {
        "atmosphere": term_lower,
        "color_palette": "unknown",
        "contrast": "unknown"
    }


def parse_cinematic_term(term: str) -> Dict[str, str]:
    """
    Auto-detect and parse any cinematic term.

    Args:
        term: Any cinematic term

    Returns:
        Parsed dictionary with appropriate structure
    """
    term_lower = term.lower().strip().replace(" ", "_").replace("-", "_")

    # Check each category
    lens_terms = {"anamorphic", "35mm", "50mm", "85mm", "135mm", "24mm", "14mm",
                  "fisheye", "tilt-shift", "tilt_shift", "macro", "telephoto", "prime", "zoom"}
    lighting_terms = {"rim_light", "rim", "low_key", "high_key", "chiaroscuro",
                      "backlight", "back", "soft_light", "soft", "hard_light", "hard",
                      "golden_hour", "golden", "blue_hour", "blue", "neon", "practical",
                      "key_light", "fill_light", "top_light", "under_light", "motivated",
                      "natural", "studio", "volumetric", "god_rays", "moonlight",
                      "candlelight", "firelight", "fluorescent", "tungsten", "daylight", "mixed"}
    camera_terms = {"dolly_in", "dolly_out", "dolly", "steadicam", "handheld", "crane",
                    "tracking", "pan", "tilt", "whip_pan", "drone", "aerial", "orbit",
                    "push_in", "pull_out", "zoom_in", "zoom_out", "rack_focus", "static",
                    "locked_off", "jib", "slider", "float", "swedish", "dutch", "canted",
                    "pov", "fly_on_wall", "over_shoulder", "ots", "low_angle", "high_angle",
                    "birds_eye", "worms_eye", "following", "leading", "circling",
                    "descending", "ascending"}
    mood_terms = set(mood_data.keys()) if 'mood_data' in dir() else set()

    if term_lower in lens_terms or "mm" in term_lower:
        return {"category": "lens", **parse_lens(term)}
    elif term_lower in lighting_terms or "light" in term_lower:
        return {"category": "lighting", **parse_lighting(term)}
    elif term_lower in camera_terms or term_lower in {"dolly", "pan", "tilt", "zoom"}:
        return {"category": "camera", **parse_camera(term)}
    else:
        return {"category": "mood", **parse_mood(term)}