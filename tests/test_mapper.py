"""
Tests for the mapper module.
"""

import pytest
from formatter.mapper import (
    LENS_MAP,
    LIGHTING_MAP,
    CAMERA_MAP,
    MOOD_MAP,
    COLOR_MAP,
    map_single_term,
    map_terms_list,
    map_to_prompt,
    get_all_terms,
    search_terms,
)


class TestLensMap:
    """Tests for LENS_MAP."""

    def test_anamorphic_mapping(self):
        assert "anamorphic" in LENS_MAP
        assert "2.39:1" in LENS_MAP["anamorphic"]

    def test_35mm_mapping(self):
        assert "35mm" in LENS_MAP
        assert "35mm lens" in LENS_MAP["35mm"]

    def test_50mm_mapping(self):
        assert "50mm" in LENS_MAP
        assert "human eye" in LENS_MAP["50mm"]

    def test_85mm_mapping(self):
        assert "85mm" in LENS_MAP
        assert "portrait" in LENS_MAP["85mm"]

    def test_fisheye_mapping(self):
        assert "fisheye" in LENS_MAP
        assert "fisheye lens" in LENS_MAP["fisheye"]

    def test_all_lens_have_weights(self):
        for key, value in LENS_MAP.items():
            assert ":1." in value or ":1)" in value, f"Lens '{key}' missing weight"


class TestLightingMap:
    """Tests for LIGHTING_MAP."""

    def test_rim_light_mapping(self):
        assert "rim_light" in LIGHTING_MAP
        assert "rim lighting" in LIGHTING_MAP["rim_light"]

    def test_low_key_mapping(self):
        assert "low_key" in LIGHTING_MAP
        assert "low-key lighting" in LIGHTING_MAP["low_key"]

    def test_high_key_mapping(self):
        assert "high_key" in LIGHTING_MAP
        assert "high-key lighting" in LIGHTING_MAP["high_key"]

    def test_chiaroscuro_mapping(self):
        assert "chiaroscuro" in LIGHTING_MAP
        assert "chiaroscuro" in LIGHTING_MAP["chiaroscuro"]

    def test_neon_mapping(self):
        assert "neon" in LIGHTING_MAP
        assert "neon lighting" in LIGHTING_MAP["neon"]

    def test_golden_hour_mapping(self):
        assert "golden_hour" in LIGHTING_MAP
        assert "golden hour" in LIGHTING_MAP["golden_hour"]

    def test_all_lighting_have_weights(self):
        for key, value in LIGHTING_MAP.items():
            assert ":1." in value or ":1)" in value, f"Lighting '{key}' missing weight"


class TestCameraMap:
    """Tests for CAMERA_MAP."""

    def test_dolly_in_mapping(self):
        assert "dolly_in" in CAMERA_MAP
        assert "dolly zoom" in CAMERA_MAP["dolly_in"]

    def test_steadicam_mapping(self):
        assert "steadicam" in CAMERA_MAP
        assert "steadicam" in CAMERA_MAP["steadicam"]

    def test_handheld_mapping(self):
        assert "handheld" in CAMERA_MAP
        assert "handheld camera" in CAMERA_MAP["handheld"]

    def test_crane_mapping(self):
        assert "crane" in CAMERA_MAP
        assert "crane shot" in CAMERA_MAP["crane"]

    def test_whip_pan_mapping(self):
        assert "whip_pan" in CAMERA_MAP
        assert "whip pan" in CAMERA_MAP["whip_pan"]

    def test_drone_mapping(self):
        assert "drone" in CAMERA_MAP
        assert "aerial drone" in CAMERA_MAP["drone"]

    def test_all_camera_have_weights(self):
        for key, value in CAMERA_MAP.items():
            assert ":1." in value or ":1)" in value, f"Camera '{key}' missing weight"


class TestMoodMap:
    """Tests for MOOD_MAP."""

    def test_noir_mapping(self):
        assert "noir" in MOOD_MAP
        assert "film noir" in MOOD_MAP["noir"]

    def test_cyberpunk_mapping(self):
        assert "cyberpunk" in MOOD_MAP
        assert "cyberpunk" in MOOD_MAP["cyberpunk"]

    def test_horror_mapping(self):
        assert "horror" in MOOD_MAP
        assert "horror" in MOOD_MAP["horror"]

    def test_romantic_mapping(self):
        assert "romantic" in MOOD_MAP
        assert "romantic" in MOOD_MAP["romantic"]

    def test_fantasy_mapping(self):
        assert "fantasy" in MOOD_MAP
        assert "fantasy" in MOOD_MAP["fantasy"]

    def test_ethereal_mapping(self):
        assert "ethereal" in MOOD_MAP
        assert "ethereal" in MOOD_MAP["ethereal"]

    def test_all_mood_have_weights(self):
        for key, value in MOOD_MAP.items():
            assert ":1." in value or ":1)" in value, f"Mood '{key}' missing weight"


class TestColorMap:
    """Tests for COLOR_MAP."""

    def test_teal_orange_mapping(self):
        assert "teal_orange" in COLOR_MAP
        assert "teal and orange" in COLOR_MAP["teal_orange"]

    def test_monochrome_mapping(self):
        assert "monochrome" in COLOR_MAP
        assert "black and white" in COLOR_MAP["monochrome"]

    def test_sepia_mapping(self):
        assert "sepia" in COLOR_MAP
        assert "sepia" in COLOR_MAP["sepia"]

    def test_film_grain_mapping(self):
        assert "film_grain" in COLOR_MAP
        assert "film grain" in COLOR_MAP["film_grain"]

    def test_all_color_have_weights(self):
        for key, value in COLOR_MAP.items():
            assert ":1." in value or ":1)" in value, f"Color '{key}' missing weight"


class TestMapSingleTerm:
    """Tests for map_single_term function."""

    def test_map_known_term(self):
        result = map_single_term("anamorphic")
        assert result is not None
        assert "anamorphic" in result

    def test_map_unknown_term(self):
        result = map_single_term("nonexistent_term")
        assert result is None

    def test_map_with_category(self):
        result = map_single_term("35mm", category="lens")
        assert result is not None
        assert "35mm" in result

    def test_map_case_insensitive(self):
        result = map_single_term("ANAMORPHIC")
        assert result is not None

    def test_map_with_whitespace(self):
        result = map_single_term("  anamorphic  ")
        assert result is not None

    def test_map_with_hyphens(self):
        result = map_single_term("low-key")
        assert result is not None
        assert "low-key" in result


class TestMapTermsList:
    """Tests for map_terms_list function."""

    def test_map_multiple_terms(self):
        terms = ["anamorphic", "rim_light", "noir"]
        result = map_terms_list(terms)
        assert len(result) == 3
        assert all(":1." in r or ":1)" in r for r in result)

    def test_map_with_unknown_terms(self):
        terms = ["anamorphic", "nonexistent", "noir"]
        result = map_terms_list(terms)
        assert len(result) == 2  # Only known terms mapped

    def test_map_empty_list(self):
        result = map_terms_list([])
        assert result == []


class TestMapToPrompt:
    """Tests for map_to_prompt function."""

    def test_basic_mapping(self):
        terms = {
            "lens": ["anamorphic"],
            "lighting": ["rim_light"],
            "mood": ["cyberpunk"],
        }
        result = map_to_prompt(terms)
        assert "anamorphic" in result
        assert "rim lighting" in result
        assert "cyberpunk" in result

    def test_single_category(self):
        terms = {"lens": ["35mm", "50mm"]}
        result = map_to_prompt(terms)
        assert "35mm" in result
        assert "50mm" in result

    def test_empty_terms(self):
        result = map_to_prompt({})
        assert result == ""

    def test_string_value(self):
        terms = {"lens": "anamorphic"}
        result = map_to_prompt(terms)
        assert "anamorphic" in result


class TestGetAllTerms:
    """Tests for get_all_terms function."""

    def test_returns_all_categories(self):
        result = get_all_terms()
        assert "lens" in result
        assert "lighting" in result
        assert "camera" in result
        assert "mood" in result
        assert "color" in result

    def test_categories_have_terms(self):
        result = get_all_terms()
        for category, terms in result.items():
            assert len(terms) > 0, f"Category '{category}' is empty"

    def test_terms_are_sorted(self):
        result = get_all_terms()
        for category, terms in result.items():
            assert terms == sorted(terms), f"Category '{category}' terms not sorted"


class TestSearchTerms:
    """Tests for search_terms function."""

    def test_search_by_keyword(self):
        result = search_terms("rim")
        assert "lighting" in result
        assert "rim_light" in result["lighting"]

    def test_search_no_results(self):
        result = search_terms("xyznonexistent")
        assert result == {}

    def test_search_multiple_categories(self):
        result = search_terms("light")
        assert "lighting" in result
        # Should find multiple lighting terms
        assert len(result["lighting"]) > 1

    def test_search_case_insensitive(self):
        result = search_terms("RIM")
        assert "lighting" in result


class TestMapWeights:
    """Tests for weight formatting in mappings."""

    def test_weights_are_floats(self):
        """Verify all weights can be parsed as floats."""
        import re
        all_maps = [LENS_MAP, LIGHTING_MAP, CAMERA_MAP, MOOD_MAP, COLOR_MAP]
        for mapping in all_maps:
            for key, value in mapping.items():
                matches = re.findall(r':(\d+\.?\d*)\)', value)
                assert len(matches) >= 1, f"Weight not found in '{key}': {value}"
                for match in matches:
                    float(match)  # Should not raise

    def test_weights_in_valid_range(self):
        """Verify weights are in reasonable range (1.0-2.0)."""
        import re
        all_maps = [LENS_MAP, LIGHTING_MAP, CAMERA_MAP, MOOD_MAP, COLOR_MAP]
        for mapping in all_maps:
            for key, value in mapping.items():
                matches = re.findall(r':(\d+\.?\d*)\)', value)
                for match in matches:
                    weight = float(match)
                    assert 1.0 <= weight <= 2.0, f"Weight {weight} out of range for '{key}'"