"""
Pytest configuration and shared fixtures.
"""

import pytest


@pytest.fixture
def sample_lens_terms():
    """Sample lens terms for testing."""
    return ["anamorphic", "35mm", "50mm", "85mm", "135mm", "24mm", "14mm", "fisheye", "tilt-shift"]


@pytest.fixture
def sample_lighting_terms():
    """Sample lighting terms for testing."""
    return ["rim_light", "low_key", "high_key", "chiaroscuro", "backlight", "soft_light", "hard_light", "golden_hour", "neon"]


@pytest.fixture
def sample_camera_terms():
    """Sample camera movement terms for testing."""
    return ["dolly_in", "dolly_out", "steadicam", "handheld", "crane", "tracking", "pan", "tilt", "whip_pan"]


@pytest.fixture
def sample_mood_terms():
    """Sample mood terms for testing."""
    return ["noir", "cyberpunk", "romantic", "horror", "thriller", "epic", "intimate", "surreal", "vintage"]


@pytest.fixture
def sample_descriptions():
    """Sample cinematic descriptions for testing."""
    return [
        "dolly in, rim light, cyberpunk mood",
        "anamorphic lens, noir lighting, tense atmosphere",
        "steadicam, soft light, romantic",
        "handheld, low key, horror",
        "crane shot, golden hour, epic",
    ]