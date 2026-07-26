"""
Tests for the parser module.
"""

import pytest
from formatter.parser import (
    parse_lens,
    parse_lighting,
    parse_camera,
    parse_mood,
    parse_cinematic_term,
)


class TestParseLens:
    """Tests for parse_lens function."""

    def test_parse_anamorphic(self):
        result = parse_lens("anamorphic")
        assert result["type"] == "anamorphic"
        assert "2.39:1" in result["characteristics"]

    def test_parse_35mm(self):
        result = parse_lens("35mm")
        assert result["focal_length"] == "35mm"
        assert result["type"] == "wide-normal"

    def test_parse_50mm(self):
        result = parse_lens("50mm")
        assert result["focal_length"] == "50mm"
        assert result["type"] == "standard"

    def test_parse_85mm(self):
        result = parse_lens("85mm")
        assert result["focal_length"] == "85mm"
        assert result["type"] == "portrait"

    def test_parse_135mm(self):
        result = parse_lens("135mm")
        assert result["focal_length"] == "135mm"
        assert result["type"] == "telephoto"

    def test_parse_24mm(self):
        result = parse_lens("24mm")
        assert result["focal_length"] == "24mm"
        assert result["type"] == "wide"

    def test_parse_14mm(self):
        result = parse_lens("14mm")
        assert result["focal_length"] == "14mm"
        assert result["type"] == "ultra-wide"

    def test_parse_fisheye(self):
        result = parse_lens("fisheye")
        assert result["type"] == "fisheye"
        assert "180" in result["characteristics"]

    def test_parse_tilt_shift(self):
        result = parse_lens("tilt-shift")
        assert result["type"] == "tilt-shift"
        assert "miniature" in result["characteristics"]

    def test_parse_unknown_lens(self):
        result = parse_lens("unknown_lens")
        assert result["focal_length"] == "unknown"
        assert result["type"] == "unknown"

    def test_parse_case_insensitive(self):
        result = parse_lens("ANAMORPHIC")
        assert result["type"] == "anamorphic"

    def test_parse_with_whitespace(self):
        result = parse_lens("  35mm  ")
        assert result["focal_length"] == "35mm"


class TestParseLighting:
    """Tests for parse_lighting function."""

    def test_parse_rim_light(self):
        result = parse_lighting("rim_light")
        assert result["type"] == "rim"
        assert result["direction"] == "behind"

    def test_parse_low_key(self):
        result = parse_lighting("low_key")
        assert result["type"] == "low-key"
        assert result["intensity"] == "low"

    def test_parse_high_key(self):
        result = parse_lighting("high_key")
        assert result["type"] == "high-key"
        assert result["intensity"] == "high"

    def test_parse_chiaroscuro(self):
        result = parse_lighting("chiaroscuro")
        assert result["type"] == "chiaroscuro"
        assert "high contrast" in result["intensity"]

    def test_parse_backlight(self):
        result = parse_lighting("backlight")
        assert result["type"] == "back"
        assert result["direction"] == "behind"

    def test_parse_soft_light(self):
        result = parse_lighting("soft_light")
        assert result["type"] == "soft"
        assert result["direction"] == "diffused"

    def test_parse_hard_light(self):
        result = parse_lighting("hard_light")
        assert result["type"] == "hard"
        assert result["intensity"] == "high"

    def test_parse_golden_hour(self):
        result = parse_lighting("golden_hour")
        assert result["type"] == "golden hour"
        assert "golden" in result["color"]

    def test_parse_neon(self):
        result = parse_lighting("neon")
        assert result["type"] == "neon"
        assert "saturated" in result["color"]

    def test_parse_unknown_lighting(self):
        result = parse_lighting("unknown_light")
        assert result["type"] == "unknown_light"

    def test_parse_case_insensitive(self):
        result = parse_lighting("RIM_LIGHT")
        assert result["type"] == "rim"

    def test_parse_with_hyphens(self):
        result = parse_lighting("low-key")
        assert result["type"] == "low-key"


class TestParseCamera:
    """Tests for parse_camera function."""

    def test_parse_dolly_in(self):
        result = parse_camera("dolly_in")
        assert result["movement"] == "dolly in"
        assert "slow" in result["speed"] or "moderate" in result["speed"]

    def test_parse_dolly_out(self):
        result = parse_camera("dolly_out")
        assert result["movement"] == "dolly out"

    def test_parse_steadicam(self):
        result = parse_camera("steadicam")
        assert result["movement"] == "steadicam"
        assert "smooth" in result["speed"]

    def test_parse_handheld(self):
        result = parse_camera("handheld")
        assert result["movement"] == "handheld"
        assert result["speed"] == "erratic"

    def test_parse_crane(self):
        result = parse_camera("crane")
        assert result["movement"] == "crane"
        assert result["angle"] == "elevated"

    def test_parse_tracking(self):
        result = parse_camera("tracking")
        assert result["movement"] == "tracking"

    def test_parse_pan(self):
        result = parse_camera("pan")
        assert result["movement"] == "pan"

    def test_parse_tilt(self):
        result = parse_camera("tilt")
        assert result["movement"] == "tilt"

    def test_parse_whip_pan(self):
        result = parse_camera("whip_pan")
        assert result["movement"] == "whip pan"
        assert result["speed"] == "very fast"

    def test_parse_drone(self):
        result = parse_camera("drone")
        assert result["movement"] == "aerial drone"
        assert "bird" in result["angle"]

    def test_parse_orbit(self):
        result = parse_camera("orbit")
        assert result["movement"] == "orbit"

    def test_parse_static(self):
        result = parse_camera("static")
        assert result["movement"] == "static"
        assert result["speed"] == "none"

    def test_parse_unknown_camera(self):
        result = parse_camera("unknown_move")
        assert result["movement"] == "unknown_move"

    def test_parse_case_insensitive(self):
        result = parse_camera("DOLLY_IN")
        assert result["movement"] == "dolly in"


class TestParseMood:
    """Tests for parse_mood function."""

    def test_parse_noir(self):
        result = parse_mood("noir")
        assert "mysterious" in result["atmosphere"]
        assert result["contrast"] == "very high"

    def test_parse_cyberpunk(self):
        result = parse_mood("cyberpunk")
        assert "dystopian" in result["atmosphere"]
        assert "neon" in result["color_palette"]

    def test_parse_romantic(self):
        result = parse_mood("romantic")
        assert "soft" in result["atmosphere"]
        assert result["contrast"] == "low to medium"

    def test_parse_horror(self):
        result = parse_mood("horror")
        assert "dark" in result["atmosphere"]
        assert result["contrast"] == "high"

    def test_parse_thriller(self):
        result = parse_mood("thriller")
        assert "tense" in result["atmosphere"]

    def test_parse_epic(self):
        result = parse_mood("epic")
        assert "grand" in result["atmosphere"]
        assert "rich" in result["color_palette"]

    def test_parse_intimate(self):
        result = parse_mood("intimate")
        assert "close" in result["atmosphere"]
        assert result["contrast"] == "low"

    def test_parse_surreal(self):
        result = parse_mood("surreal")
        assert "dreamlike" in result["atmosphere"]

    def test_parse_vintage(self):
        result = parse_mood("vintage")
        assert "nostalgic" in result["atmosphere"]
        assert "faded" in result["color_palette"]

    def test_parse_unknown_mood(self):
        result = parse_mood("unknown_mood")
        assert result["atmosphere"] == "unknown_mood"

    def test_parse_case_insensitive(self):
        result = parse_mood("NOIR")
        assert "mysterious" in result["atmosphere"]


class TestParseCinematicTerm:
    """Tests for parse_cinematic_term function."""

    def test_auto_detect_lens(self):
        result = parse_cinematic_term("35mm")
        assert result["category"] == "lens"
        assert result["focal_length"] == "35mm"

    def test_auto_detect_lighting(self):
        result = parse_cinematic_term("rim_light")
        assert result["category"] == "lighting"
        assert result["type"] == "rim"

    def test_auto_detect_camera(self):
        result = parse_cinematic_term("dolly_in")
        assert result["category"] == "camera"
        assert result["movement"] == "dolly in"

    def test_auto_detect_mood(self):
        result = parse_cinematic_term("noir")
        assert result["category"] == "mood"
        assert "mysterious" in result["atmosphere"]