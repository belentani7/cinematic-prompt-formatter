"""
Tests for the formatter module.
"""

import pytest
from formatter.formatter import (
    format_prompt,
    format_batch,
    optimize_for_model,
    optimize_sdxl,
    optimize_flux,
    optimize_sd15,
    apply_preset,
    parse_description,
)
from formatter.presets import PRESETS, get_preset


class TestFormatPrompt:
    """Tests for format_prompt function."""

    def test_basic_format(self):
        result = format_prompt("dolly in, rim light, cyberpunk mood")
        assert "dolly zoom" in result
        assert "rim lighting" in result
        assert "cyberpunk" in result

    def test_with_model(self):
        result = format_prompt("anamorphic lens", model="flux")
        assert "anamorphic" in result
        assert "professional" in result  # Flux optimizer adds this

    def test_with_style(self):
        result = format_prompt("noir lighting", style="hollywood_cinematic")
        assert "cinematic" in result.lower()
        assert "noir" in result

    def test_multiple_terms(self):
        result = format_prompt("35mm, soft light, romantic")
        assert "35mm" in result
        assert "soft" in result
        assert "romantic" in result

    def test_unknown_term(self):
        result = format_prompt("unknown_cinematic_term")
        assert "unknown_cinematic_term" in result

    def test_empty_description(self):
        result = format_prompt("")
        # Should handle gracefully
        assert isinstance(result, str)

    def test_case_insensitive(self):
        result = format_prompt("DOLLY IN, RIM LIGHT")
        assert "dolly zoom" in result
        assert "rim lighting" in result


class TestFormatBatch:
    """Tests for format_batch function."""

    def test_batch_format(self):
        descriptions = [
            "dolly in, rim light",
            "anamorphic lens, noir mood",
        ]
        results = format_batch(descriptions)
        assert len(results) == 2
        assert "dolly zoom" in results[0]
        assert "anamorphic" in results[1]

    def test_batch_with_style(self):
        descriptions = ["soft light", "hard light"]
        results = format_batch(descriptions, style="realistic")
        assert len(results) == 2
        for result in results:
            assert "realistic" in result.lower() or "photorealistic" in result.lower()

    def test_batch_with_model(self):
        descriptions = ["rim light"]
        results = format_batch(descriptions, model="flux")
        assert len(results) == 1
        assert "professional" in results[0]

    def test_empty_batch(self):
        results = format_batch([])
        assert results == []


class TestOptimizeForModel:
    """Tests for optimize_for_model function."""

    def test_optimize_sdxl(self):
        result = optimize_for_model("(test:1.1)", "sdxl")
        assert "masterpiece" in result
        assert "highly detailed" in result

    def test_optimize_flux(self):
        result = optimize_for_model("(test:1.1)", "flux")
        assert "professional" in result
        # Flux should strip weights
        assert ":1.1)" not in result

    def test_optimize_sd15(self):
        result = optimize_for_model("(test:1.1)", "sd15")
        assert "masterpiece" in result
        assert "highly detailed" in result

    def test_optimize_unknown_model(self):
        result = optimize_for_model("(test:1.1)", "unknown_model")
        assert result == "(test:1.1)"


class TestOptimizeSdxl:
    """Tests for optimize_sdxl function."""

    def test_adds_quality_boosters(self):
        result = optimize_sdxl("(test:1.1)")
        assert "masterpiece" in result
        assert "best quality" in result
        assert "highly detailed" in result

    def test_preserves_original(self):
        result = optimize_sdxl("(anamorphic:1.3)")
        assert "anamorphic" in result


class TestOptimizeFlux:
    """Tests for optimize_flux function."""

    def test_strips_weights(self):
        result = optimize_flux("(test:1.3)")
        assert ":1.3)" not in result
        assert "test" in result

    def test_adds_professional(self):
        result = optimize_flux("(test:1.1)")
        assert "professional" in result

    def test_cleans_double_commas(self):
        result = optimize_flux("(test:1.1), , (other:1.2)")
        assert ", ," not in result


class TestOptimizeSd15:
    """Tests for optimize_sd15 function."""

    def test_adds_quality_boosters(self):
        result = optimize_sd15("(test:1.1)")
        assert "masterpiece" in result
        assert "highly detailed" in result

    def test_caps_weights(self):
        # SD1.5 can be sensitive to high weights
        result = optimize_sd15("(test:2.0)")
        assert ":1.5)" in result  # Should be capped

    def test_preserves_valid_weights(self):
        result = optimize_sd15("(test:1.2)")
        assert ":1.2)" in result


class TestApplyPreset:
    """Tests for apply_preset function."""

    def test_apply_hollywood_preset(self):
        preset = get_preset("hollywood_cinematic")
        result = apply_preset("(test:1.1)", preset)
        assert "cinematic" in result.lower()

    def test_apply_with_prefix(self):
        preset = {"prefix": "PREFIX", "suffix": "SUFFIX"}
        result = apply_preset("(test:1.1)", preset)
        assert result.startswith("PREFIX")
        assert result.endswith("SUFFIX")

    def test_apply_with_modifiers(self):
        preset = {"modifiers": ["(extra:1.1)", "(boost:1.2)"]}
        result = apply_preset("(test:1.1)", preset)
        assert "extra" in result
        assert "boost" in result


class TestParseDescription:
    """Tests for parse_description function."""

    def test_parse_comma_separated(self):
        result = parse_description("dolly in, rim light, cyberpunk")
        assert "dolly_in" in result
        assert "rim_light" in result
        assert "cyberpunk" in result

    def test_parse_with_and(self):
        result = parse_description("dolly in and rim light")
        assert "dolly_in" in result
        assert "rim_light" in result

    def test_parse_with_with(self):
        result = parse_description("anamorphic with neon lighting")
        assert "anamorphic" in result
        assert "neon" in result

    def test_parse_single_term(self):
        result = parse_description("noir")
        assert "noir" in result

    def test_parse_empty(self):
        result = parse_description("")
        assert result == []

    def test_parse_whitespace(self):
        result = parse_description("  dolly in  ,  rim light  ")
        assert "dolly_in" in result
        assert "rim_light" in result

    def test_parse_preserves_multiword(self):
        result = parse_description("golden hour")
        assert "golden_hour" in result

    def test_parse_hyphenated(self):
        result = parse_description("low-key lighting")
        assert "low_key" in result


class TestIntegration:
    """Integration tests for the full formatting pipeline."""

    def test_full_pipeline_sdxl(self):
        result = format_prompt(
            "dolly in, rim light, cyberpunk mood",
            style="hollywood_cinematic",
            model="sdxl"
        )
        assert "masterpiece" in result
        assert "dolly zoom" in result
        assert "rim lighting" in result
        assert "cyberpunk" in result
        assert "cinematic" in result.lower()

    def test_full_pipeline_flux(self):
        result = format_prompt(
            "anamorphic lens, noir lighting",
            model="flux"
        )
        assert "professional" in result
        assert "anamorphic" in result
        assert "noir" in result
        # Flux should strip weights
        assert ":1." not in result

    def test_full_pipeline_sd15(self):
        result = format_prompt(
            "35mm, soft light, romantic",
            model="sd15"
        )
        assert "masterpiece" in result
        assert "35mm" in result
        assert "soft" in result

    def test_batch_full_pipeline(self):
        descriptions = [
            "dolly in, rim light, cyberpunk",
            "anamorphic, noir, tense",
            "steadicam, golden hour, epic",
        ]
        results = format_batch(
            descriptions,
            style="music_video",
            model="sdxl"
        )
        assert len(results) == 3
        for result in results:
            assert len(result) > 0