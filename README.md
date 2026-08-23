# Cinematic Prompt Formatter

Translate cinematic language into optimized prompts for Stable Diffusion, Flux, and SDXL models.

## Features

- Parse cinematic terms (lens, lighting, camera movement, mood)
- Map to weighted prompt tags for AI image generation
- 50+ cinematic terms with precise mappings
- Preset styles for common cinematic looks
- Batch processing via CLI
- Model-specific optimization

## Installation

```bash
pip install cinematic-prompt-formatter
```

Or from source:

```bash
git clone https://github.com/belentani7/cinematic-prompt-formatter.git
cd cinematic-prompt-formatter
pip install -e .
```

## Quick Start

```python
from formatter import format_prompt

# Single prompt
result = format_prompt("dolly in, rim light, cyberpunk mood")
# Output: (dolly zoom, vertigo effect:1.1), (rim lighting, edge light:1.2), (cyberpunk, neon glow, rain:1.3)

# With specific model
result = format_prompt("anamorphic lens, noir lighting", model="flux")

# Batch processing
results = format_batch([
    "dolly in, rim light, cyberpunk mood",
    "steadicam, low key, thriller"
], style="hollywood_cinematic")
```

## CLI Usage

```bash
# Format a single prompt
cpf format "dolly in, rim light, cyberpunk mood" --model sdxl

# Batch process from CSV
cpf batch input.csv --output formatted.csv

# List available presets
cpf presets
```

## Cinematic Terms

### Lens Types
- `anamorphic` - Anamorphic lens, cinematic 2.39:1 aspect ratio
- `35mm` - Natural perspective lens
- `50mm` - Standard lens, human eye perspective
- `85mm` - Portrait lens, flattering compression
- `135mm` - Telephoto, extreme compression
- `24mm` - Wide angle, dramatic distortion
- `14mm` - Ultra wide, extreme perspective
- `fisheye` - Fisheye lens, circular distortion
- `tilt-shift` - Tilt-shift lens, miniature effect

### Lighting
- `rim_light` - Edge lighting, separation from background
- `low_key` - Low-key lighting, dramatic shadows
- `high_key` - High-key lighting, bright and even
- `chiaroscuro` - Strong contrast between light and dark
- `backlight` - Backlighting, silhouette effect
- `soft_light` - Soft, diffused lighting
- `hard_light` - Hard, directional lighting
- `golden_hour` - Warm, golden hour light
- `blue_hour` - Cool, blue hour light
- `neon` - Neon lighting, colorful glow
- `practical` - Practical lighting, in-scene sources

### Camera Movement
- `dolly_in` - Dolly zoom, vertigo effect
- `dolly_out` - Reverse dolly, reveal
- `steadicam` - Steadicam, smooth motion
- `handheld` - Handheld camera, raw energy
- `crane` - Crane shot, sweeping movement
- `tracking` - Tracking shot, following subject
- `pan` - Pan, horizontal movement
- `tilt` - Tilt, vertical movement
- `whip_pan` - Whip pan, fast transition
- `drone` - Aerial drone shot
- `orbit` - Orbiting camera movement
- `push_in` - Push in, increasing intensity
- `pull_out` - Pull out, revealing context

### Mood/Atmosphere
- `noir` - Film noir, high contrast
- `cyberpunk` - Cyberpunk aesthetic
- `romantic` - Romantic, soft atmosphere
- `horror` - Horror, unsettling
- `thriller` - Thriller, tension
- `epic` - Epic, grand scale
- `intimate` - Intimate, close feeling
- `surreal` - Surreal, dreamlike
- `vintage` - Vintage, nostalgic
- `futuristic` - Futuristic, advanced
- `post_apocalyptic` - Post-apocalyptic decay
- `fantasy` - Fantasy, magical
- `western` - Western, frontier
- `steampunk` - Steampunk, Victorian tech
- `ethereal` - Ethereal, otherworldly

### Color Grading
- `teal_orange` - Teal and orange color grade
- `desaturated` - Desaturated, muted colors
- `high_saturation` - High saturation, vibrant
- `monochrome` - Black and white
- `sepia` - Sepia tone
- `cross_process` - Cross-processing effect
- `bleach_bypass` - Bleach bypass, high contrast

## Presets

| Preset | Description |
|--------|-------------|
| `hollywood_cinematic` | Big budget Hollywood look |
| `indie_film` | Independent film aesthetic |
| `music_video` | Music video style |
| `commercial` | Commercial/advertising look |
| `anime` | Anime-inspired style |
| `realistic` | Photorealistic style |

## Model Support

- **SDXL**: Optimized for Stable Diffusion XL
- **Flux**: Optimized for Flux models
- **SD15**: Optimized for Stable Diffusion 1.5

## License

MIT License
