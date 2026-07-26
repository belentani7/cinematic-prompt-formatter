"""
Map cinematic terms to weighted prompt tags for AI image generation.
"""

from typing import Dict, List, Optional

# =============================================================================
# LENS MAPPINGS
# =============================================================================

LENS_MAP: Dict[str, str] = {
    # Anamorphic
    "anamorphic": "(anamorphic lens, cinematic, 2.39:1 aspect ratio:1.3)",
    "anamorphic_lens": "(anamorphic lens, oval bokeh, lens flares:1.3)",

    # Focal lengths
    "35mm": "(35mm lens, natural perspective:1.1)",
    "35mm_lens": "(35mm focal length, versatile wide:1.1)",
    "50mm": "(50mm lens, human eye perspective:1.1)",
    "50mm_lens": "(50mm focal length, standard lens:1.1)",
    "85mm": "(85mm lens, portrait compression, bokeh:1.2)",
    "85mm_lens": "(85mm focal length, flattering perspective:1.2)",
    "135mm": "(135mm lens, telephoto compression:1.2)",
    "135mm_lens": "(135mm focal length, extreme compression:1.2)",

    # Wide angle
    "24mm": "(24mm lens, wide angle, dramatic perspective:1.1)",
    "24mm_lens": "(24mm focal length, expansive view:1.1)",
    "14mm": "(14mm lens, ultra wide, extreme distortion:1.1)",
    "14mm_lens": "(14mm focal length, immersive wide:1.1)",
    "wide_angle": "(wide angle lens, expansive, environmental:1.1)",
    "wide-angle": "(wide angle lens, dramatic perspective:1.1)",

    # Specialty lenses
    "fisheye": "(fisheye lens, circular distortion, 180 degree view:1.2)",
    "fisheye_lens": "(fisheye, barrel distortion, surreal:1.2)",
    "tilt_shift": "(tilt-shift lens, miniature effect:1.2)",
    "tilt-shift": "(tilt-shift, selective focus, toy-like:1.2)",
    "tilt_shift_lens": "(tilt-shift, architectural photography:1.2)",
    "macro": "(macro lens, extreme close-up, 1:1 magnification:1.1)",
    "macro_lens": "(macro photography, detail, texture:1.1)",

    # Telephoto
    "telephoto": "(telephoto lens, compression, distant subject:1.1)",
    "super_telephoto": "(super telephoto, extreme compression:1.2)",
    "long_lens": "(long focal length, compressed perspective:1.1)",

    # Lens types
    "prime": "(prime lens, sharp, fast aperture:1.1)",
    "prime_lens": "(fixed focal length, maximum sharpness:1.1)",
    "zoom": "(zoom lens, versatile framing:1.0)",
    "zoom_lens": "(variable focal length, flexible composition:1.0)",

    # Lens effects
    "shallow_dof": "(shallow depth of field, bokeh, subject isolation:1.2)",
    "deep_focus": "(deep focus, everything sharp, f/16:1.1)",
    "bokeh": "(beautiful bokeh, out of focus background:1.1)",
    "lens_flare": "(cinematic lens flare, light streaks:1.1)",
    "soft_focus": "(soft focus lens, dreamy, diffused:1.1)",

    # Vintage lenses
    "vintage_lens": "(vintage lens, character, imperfections:1.1)",
    "helios": "(Helios 44-2, swirly bokeh, Soviet lens:1.2)",
    "cooke": "(Cooke lens, warm, cinematic rendering:1.1)",
}

# =============================================================================
# LIGHTING MAPPINGS
# =============================================================================

LIGHTING_MAP: Dict[str, str] = {
    # Classic lighting setups
    "rim_light": "(rim lighting, edge light, separation:1.2)",
    "rim": "(rim light, backlit edges, halo:1.2)",
    "rim_lighting": "(rim lighting, subject separation:1.2)",
    "low_key": "(low-key lighting, dramatic shadows:1.3)",
    "low-key": "(low-key, high contrast, moody:1.3)",
    "low_key_lighting": "(low-key, chiaroscuro style:1.3)",
    "high_key": "(high-key lighting, bright and even:1.1)",
    "high-key": "(high-key, minimal shadows, bright:1.1)",
    "high_key_lighting": "(high-key, commercial lighting:1.1)",
    "chiaroscuro": "(chiaroscuro, strong light-dark contrast:1.3)",
    "rembrandt": "(Rembrandt lighting, triangle of light:1.2)",

    # Directional lighting
    "backlight": "(backlighting, silhouette, rim light:1.2)",
    "back": "(backlit, halo effect, separation:1.2)",
    "backlighting": "(backlight, dramatic outline:1.2)",
    "sidelight": "(side lighting, dimension, texture:1.2)",
    "side_light": "(side light, dramatic shadows:1.2)",
    "front_light": "(front lighting, even, flat:1.0)",
    "top_light": "(overhead lighting, dramatic:1.1)",
    "under_light": "(under lighting, horror, eerie:1.2)",
    "bottom_light": "(underlighting, unnatural, spooky:1.2)",

    # Quality of light
    "soft_light": "(soft lighting, diffused, gentle shadows:1.1)",
    "soft": "(soft light, wrapping, flattering:1.1)",
    "soft_lighting": "(soft diffused light, minimal shadows:1.1)",
    "hard_light": "(hard lighting, sharp shadows:1.2)",
    "hard": "(hard light, defined shadows, contrast:1.2)",
    "hard_lighting": "(hard directional light, dramatic:1.2)",
    "diffused": "(diffused light, soft shadows:1.1)",
    "harsh": "(harsh lighting, unflattering, stark:1.1)",

    # Time-based lighting
    "golden_hour": "(golden hour lighting, warm sun, magic hour:1.3)",
    "golden": "(golden hour, warm golden tones:1.3)",
    "magic_hour": "(magic hour, sunset colors:1.3)",
    "blue_hour": "(blue hour, twilight, cool ambient:1.2)",
    "blue": "(blue hour lighting, cool dusk:1.2)",
    "twilight": "(twilight lighting, fading light:1.1)",
    "noon": "(harsh midday sun, overhead, contrast:1.1)",
    "midday": "(midday sun, bright overhead:1.1)",

    # Color temperatures
    "warm_light": "(warm lighting, tungsten, orange:1.1)",
    "cool_light": "(cool lighting, blue, fluorescent:1.1)",
    "tungsten": "(tungsten lighting, 3200K, warm:1.1)",
    "daylight_balanced": "(daylight balanced, 5600K:1.0)",
    "mixed_color_temp": "(mixed color temperature, contrast:1.1)",

    # Special lighting
    "neon": "(neon lighting, colorful glow, cyberpunk:1.3)",
    "neon_light": "(neon lights, vibrant, electric:1.3)",
    "neon_glow": "(neon glow, atmospheric, colorful:1.2)",
    "practical": "(practical lighting, in-scene sources:1.1)",
    "practical_light": "(practical lights, motivated lighting:1.1)",
    "volumetric": "(volumetric lighting, light shafts, atmosphere:1.2)",
    "god_rays": "(god rays, crepuscular rays, through windows:1.2)",
    "crepuscular": "(crepuscular rays, light beams:1.2)",
    "light_shafts": "(light shafts, atmospheric, dust particles:1.2)",

    # Mood lighting
    "moonlight": "(moonlight, cool blue, night:1.2)",
    "moon": "(lunar light, blue night:1.2)",
    "candlelight": "(candlelight, warm flickering:1.2)",
    "candle": "(candle glow, intimate, warm:1.2)",
    "firelight": "(firelight, warm orange, dancing shadows:1.2)",
    "fire": "(fire glow, warm, flickering:1.2)",
    "fireplace": "(fireplace light, cozy, warm:1.1)",
    "sunset": "(sunset lighting, warm colors:1.1)",
    "sunrise": "(sunrise lighting, soft warm:1.1)",

    # Studio lighting
    "studio": "(studio lighting, controlled, professional:1.1)",
    "studio_lighting": "(studio setup, three-point lighting:1.1)",
    "three_point": "(three-point lighting, key, fill, rim:1.1)",
    "beauty_dish": "(beauty dish, soft but defined:1.1)",
    "softbox": "(softbox lighting, even, professional:1.1)",
    "ring_light": "(ring light, even facial lighting:1.0)",

    # Color gels/effects
    "colored_gels": "(colored gels, dramatic color:1.2)",
    "gel_light": "(gel lighting, saturated color:1.2)",
    "duotone": "(duotone lighting, two colors:1.2)",
    "split_lighting": "(split lighting, half face:1.2)",

    # Natural lighting
    "natural_light": "(natural lighting, ambient:1.1)",
    "window_light": "(window light, soft directional:1.1)",
    "skylight": "(skylight, ambient overhead:1.0)",
    "dappled": "(dappled light, through leaves:1.1)",
    "filtered": "(filtered light, through curtains:1.1)",

    # Motivated lighting
    "motivated": "(motivated lighting, source-justified:1.1)",
    "motivated_light": "(motivated light, natural source:1.1)",

    # Hard/dramatic
    "stark": "(stark lighting, minimal, harsh:1.1)",
    "dramatic": "(dramatic lighting, high contrast:1.2)",
    "moody": "(moody lighting, atmospheric:1.2)",
    "atmospheric": "(atmospheric lighting, environmental:1.1)",
}

# =============================================================================
# CAMERA MOVEMENT MAPPINGS
# =============================================================================

CAMERA_MAP: Dict[str, str] = {
    # Dolly movements
    "dolly_in": "(dolly zoom, vertigo effect:1.1)",
    "dolly_out": "(dolly out, revealing context:1.1)",
    "dolly": "(dolly movement, smooth tracking:1.1)",
    "dolly_zoom": "(dolly zoom, vertigo effect, Hitchcock:1.2)",
    "vertigo": "(vertigo effect, dolly zoom:1.2)",
    "hitchcock": "(Hitchcock zoom, vertigo effect:1.2)",

    # Stabilized movement
    "steadicam": "(steadicam, smooth motion:1.0)",
    "steady": "(steadicam, fluid movement:1.0)",
    "gimbal": "(gimbal movement, stabilized, smooth:1.0)",
    "stabilized": "(stabilized camera, smooth:1.0)",

    # Handheld/raw
    "handheld": "(handheld camera, raw, documentary:1.1)",
    "shaky_cam": "(shaky cam, chaos, urgency:1.2)",
    "shaky": "(shaky camera, handheld energy:1.1)",

    # Aerial/elevated
    "crane": "(crane shot, sweeping, elevated:1.1)",
    "jib": "(jib movement, smooth elevation:1.0)",
    "drone": "(aerial drone shot, bird's eye:1.2)",
    "aerial": "(aerial shot, elevated perspective:1.2)",
    "birds_eye": "(bird's eye view, top down:1.1)",

    # Tracking
    "tracking": "(tracking shot, following subject:1.1)",
    "following": "(following shot, behind subject:1.0)",
    "leading": "(leading shot, in front of subject:1.0)",
    "parallel": "(parallel tracking, side by side:1.0)",

    # Pan/Tilt
    "pan": "(pan shot, horizontal movement:1.0)",
    "tilt": "(tilt shot, vertical movement:1.0)",
    "whip_pan": "(whip pan, fast transition:1.2)",
    "swish_pan": "(swish pan, blur transition:1.1)",
    "snap_zoom": "(snap zoom, sudden close:1.1)",

    # Push/Pull
    "push_in": "(push in, increasing intensity:1.1)",
    "push": "(push in, getting closer:1.1)",
    "pull_out": "(pull out, revealing context:1.1)",
    "pull": "(pull out, stepping back:1.1)",
    "reveal": "(reveal shot, showing new information:1.1)",

    # Zoom
    "zoom_in": "(zoom in, increasing emphasis:1.0)",
    "zoom_out": "(zoom out, showing context:1.0)",
    "slow_zoom": "(slow zoom, subtle approach:1.0)",
    "crash_zoom": "(crash zoom, sudden emphasis:1.2)",
    "snap_back": "(snap back, sudden reveal:1.1)",

    # Focus
    "rack_focus": "(rack focus, shifting attention:1.1)",
    "focus_pull": "(focus pull, selective focus:1.1)",
    "deep_focus": "(deep focus, everything sharp:1.1)",
    "shallow_focus": "(shallow focus, bokeh background:1.1)",

    # Static
    "static": "(static camera, locked frame:1.0)",
    "locked_off": "(locked off, no movement:1.0)",
    "locked": "(locked camera, still:1.0)",
    "tripod": "(tripod shot, stable, static:1.0)",

    # Slider
    "slider": "(slider movement, smooth horizontal:1.0)",
    "lateral": "(lateral movement, side to side:1.0)",

    # Floating
    "float": "(floating camera, ethereal movement:1.1)",
    "floating": "(floating shot, dreamlike:1.1)",

    # Dutch/canted
    "dutch": "(Dutch angle, canted frame:1.1)",
    "swedish": "(Swedish angle, tilted:1.1)",
    "canted": "(canted angle, unease:1.1)",
    "tilted": "(tilted angle, off-balance:1.1)",

    # POV
    "pov": "(point of view, first person:1.1)",
    "first_person": "(first person perspective, POV:1.1)",
    "subjective": "(subjective camera, character POV:1.1)",

    # Fly on wall
    "fly_on_wall": "(fly on the wall, observational:1.0)",
    "observational": "(observational camera, documentary:1.0)",

    # Over shoulder
    "over_shoulder": "(over the shoulder, conversation:1.0)",
    "ots": "(over the shoulder, dialogue:1.0)",
    "shoulder": "(over shoulder, two-shot:1.0)",

    # Angle-specific
    "low_angle": "(low angle, powerful, dominant:1.1)",
    "low": "(low angle shot, looking up:1.1)",
    "high_angle": "(high angle, diminished, vulnerable:1.1)",
    "high": "(high angle shot, looking down:1.1)",
    "worms_eye": "(worm's eye view, extreme low:1.1)",
    "eye_level": "(eye level, neutral:1.0)",

    # Circling/orbiting
    "orbit": "(orbiting camera, circling subject:1.1)",
    "circling": "(circling shot, 360 movement:1.1)",
    "360": "(360 degree orbit, full circle:1.1)",

    # Vertical movement
    "ascending": "(ascending shot, rising up:1.0)",
    "descending": "(descending shot, going down:1.0)",
    "rising": "(rising shot, going up:1.0)",
    "falling": "(falling shot, going down:1.0)",

    # Special movements
    "wipe": "(wipe transition, scene change:1.0)",
    "match_cut": "(match cut, visual transition:1.0)",
    "invisible_cut": "(invisible cut, seamless:1.0)",
}

# =============================================================================
# MOOD/ATMOSPHERE MAPPINGS
# =============================================================================

MOOD_MAP: Dict[str, str] = {
    # Film genres/styles
    "noir": "(film noir, high contrast, chiaroscuro:1.4)",
    "film_noir": "(film noir, shadows, mystery:1.4)",
    "neo_noir": "(neo-noir, modern noir, neon:1.3)",
    "cyberpunk": "(cyberpunk, neon glow, rain:1.3)",
    "cyber": "(cyberpunk aesthetic, futuristic:1.3)",
    "steampunk": "(steampunk, Victorian technology, brass:1.3)",
    "solarpunk": "(solarpunk, green tech, optimistic:1.2)",
    "western": "(Western, frontier, dusty:1.2)",
    "space_western": "(space Western, sci-fi frontier:1.2)",
    "fantasy": "(fantasy, magical, enchanted:1.3)",
    "sci_fi": "(science fiction, futuristic:1.2)",
    "horror": "(horror, unsettling, dark:1.3)",
    "thriller": "(thriller, suspense, tension:1.2)",
    "romance": "(romantic, soft, emotional:1.2)",
    "action": "(action, dynamic, intense:1.1)",
    "comedy": "(comedic, bright, playful:1.0)",
    "drama": "(dramatic, emotional, serious:1.1)",
    "documentary": "(documentary, realistic, observational:1.0)",
    "music_video": "(music video, stylized, energetic:1.2)",

    # Emotional states
    "romantic": "(romantic, intimate, warm:1.2)",
    "love": "(romantic, passionate, warm:1.2)",
    "melancholic": "(melancholic, somber, reflective:1.2)",
    "sad": "(melancholic, sad, emotional:1.2)",
    "happy": "(joyful, bright, uplifting:1.0)",
    "joyful": "(joyful, vibrant, energetic:1.0)",
    "peaceful": "(peaceful, serene, calm:1.1)",
    "serene": "(serene, tranquil, zen:1.1)",
    "calm": "(calm, peaceful, quiet:1.0)",
    "tense": "(tense, suspenseful, anxious:1.2)",
    "anxious": "(anxious, uneasy, nervous:1.1)",
    "scary": "(frightening, horror, dark:1.3)",
    "fearful": "(fearful, horror, unsettling:1.2)",
    "angry": "(angry, aggressive, intense:1.1)",
    "aggressive": "(aggressive, raw, confrontational:1.1)",
    "energetic": "(energetic, dynamic, alive:1.1)",
    "mysterious": "(mysterious, enigmatic, unknown:1.2)",
    "enigmatic": "(enigmatic, puzzling, hidden:1.2)",
    "hopeful": "(hopeful, optimistic, bright:1.1)",
    "optimistic": "(optimistic, bright, positive:1.1)",
    "gloomy": "(gloomy, dark, depressing:1.2)",
    "depressing": "(depressing, somber, bleak:1.1)",
    "whimsical": "(whimsical, playful, fanciful:1.1)",
    "playful": "(playful, fun, lighthearted:1.0)",
    "dreamy": "(dreamy, soft, hazy:1.2)",
    "ethereal": "(ethereal, otherworldly, transcendent:1.3)",
    "haunting": "(haunting, eerie, lingering:1.2)",
    "eerie": "(eerie, unsettling, strange:1.2)",
    "ominous": "(ominous, foreboding, threatening:1.2)",
    "threatening": "(threatening, dark, dangerous:1.1)",
    "nostalgic": "(nostalgic, warm, wistful:1.1)",
    "wistful": "(wistful, longing, reflective:1.1)",
    "decadent": "(decadent, luxurious, excess:1.1)",
    "luxurious": "(luxurious, opulent, rich:1.1)",
    "gritty": "(gritty, raw, realistic:1.1)",
    "raw": "(raw, unpolished, authentic:1.1)",
    "moody": "(moody, atmospheric, emotional:1.2)",
    "atmospheric": "(atmospheric, environmental, immersive:1.1)",
    "cinematic": "(cinematic, filmic, dramatic:1.1)",
    "dramatic": "(dramatic, intense, emotional:1.2)",
    "intimate": "(intimate, close, personal:1.1)",
    "epic": "(epic, grand, sweeping:1.3)",
    "grand": "(grand, majestic, sweeping:1.2)",
    "surreal": "(surreal, dreamlike, uncanny:1.3)",
    "abstract": "(abstract, non-representational:1.1)",
    "minimalist": "(minimalist, clean, simple:1.0)",
    "baroque": "(baroque, ornate, detailed:1.1)",
    "ornate": "(ornate, detailed, decorative:1.1)",
    "futuristic": "(futuristic, advanced, sleek:1.2)",
    "vintage": "(vintage, nostalgic, aged:1.1)",
    "retro": "(retro, nostalgic, throwback:1.1)",
    "antique": "(antique, aged, historical:1.0)",
    "modern": "(modern, contemporary, clean:1.0)",
    "contemporary": "(contemporary, current, modern:1.0)",
    "ancient": "(ancient, historical, aged:1.1)",
    "medieval": "(medieval, dark ages, historical:1.1)",
    "post_apocalyptic": "(post-apocalyptic, decayed, desolate:1.3)",
    "dystopian": "(dystopian, dark future, oppressive:1.2)",
    "utopian": "(utopian, perfect, idealized:1.0)",
    "alien": "(alien, otherworldly, strange:1.2)",
    "cosmic": "(cosmic, space, vast:1.2)",
    "organic": "(organic, natural, flowing:1.0)",
    "industrial": "(industrial, mechanical, harsh:1.1)",
    "urban": "(urban, city, metropolitan:1.0)",
    "rural": "(rural, countryside, pastoral:1.0)",
    "wilderness": "(wilderness, nature, untamed:1.0)",
    "military": "(military, tactical, disciplined:1.0)",
    "mystical": "(mystical, magical, spiritual:1.2)",
    "spiritual": "(spiritual, sacred, transcendent:1.1)",
    "religious": "(religious, sacred, devotional:1.0)",
    "tribal": "(tribal, cultural, traditional:1.0)",
    "futuristic_city": "(futuristic cityscape, neon, advanced:1.2)",
    "underwater": "(underwater, submerged, aquatic:1.1)",
    "space": "(space, cosmic, stars:1.2)",
    "forest": "(forest, woodland, natural:1.0)",
    "desert": "(desert, arid, vast:1.0)",
    "arctic": "(arctic, frozen, ice:1.1)",
    "tropical": "(tropical, lush, vibrant:1.0)",
    "apocalyptic": "(apocalyptic, end of world, destruction:1.3)",
    "biblical": "(biblical, epic, historical:1.1)",
    "mythological": "(mythological, legendary, epic:1.2)",
    "fairytale": "(fairytale, magical, storybook:1.2)",
    "nightmare": "(nightmare, nightmarish, horror:1.3)",
    "paradise": "(paradise, utopian, perfect:1.1)",
    "heaven": "(heavenly, divine, ethereal:1.2)",
    "hell": "(hellish, infernal, dark:1.2)",
}

# =============================================================================
# COLOR GRADING MAPPINGS
# =============================================================================

COLOR_MAP: Dict[str, str] = {
    "teal_orange": "(teal and orange color grade, blockbuster:1.2)",
    "orange_teal": "(orange and teal, cinematic color:1.2)",
    "desaturated": "(desaturated, muted colors:1.1)",
    "muted": "(muted colors, low saturation:1.0)",
    "high_saturation": "(high saturation, vibrant colors:1.1)",
    "saturated": "(saturated, vivid colors:1.1)",
    "vibrant": "(vibrant, rich colors:1.1)",
    "monochrome": "(monochrome, black and white:1.1)",
    "black_and_white": "(black and white, grayscale:1.1)",
    "bw": "(black and white, monochrome:1.1)",
    "sepia": "(sepia tone, aged, warm:1.1)",
    "sepia_tone": "(sepia, vintage color:1.1)",
    "cross_process": "(cross-processing, shifted colors:1.2)",
    "cross_process": "(cross-processed, unusual colors:1.2)",
    "bleach_bypass": "(bleach bypass, high contrast, desaturated:1.2)",
    "bleach": "(bleach bypass, silver retention:1.2)",
    "technicolor": "(Technicolor, vivid, saturated:1.3)",
    "pastel": "(pastel colors, soft, light:1.0)",
    "earth_tones": "(earth tones, natural colors:1.0)",
    "cool_tones": "(cool color palette, blues:1.0)",
    "warm_tones": "(warm color palette, oranges:1.0)",
    "neon_colors": "(neon colors, vibrant, electric:1.2)",
    "jewel_tones": "(jewel tones, rich, deep:1.1)",
    "muted_tones": "(muted tones, subtle colors:1.0)",
    "high_contrast": "(high contrast, punchy:1.1)",
    "low_contrast": "(low contrast, flat, soft:1.0)",
    "lifted_blacks": "(lifted blacks, faded film:1.1)",
    "crushed_blacks": "(crushed blacks, deep shadows:1.1)",
    "film_grain": "(film grain, analog texture:1.0)",
    "grain": "(film grain, textured:1.0)",
    "clean": "(clean, digital, sharp:1.0)",
    "raw": "(raw, unprocessed:1.0)",
    "color_shifted": "(color shifted, unusual tones:1.1)",
    "duotone": "(duotone, two-color:1.1)",
    "split_tone": "(split toning, color contrast:1.1)",
    "lomography": "(lomography, light leaks, saturated:1.1)",
    "polaroid": "(Polaroid, instant film, vintage:1.1)",
    "film_stock": "(film stock emulation:1.1)",
    "kodak": "(Kodak film stock, warm:1.1)",
    "fuji": "(Fujifilm stock, green tones:1.1)",
    "cinestill": "(CineStill, halation, tungsten:1.2)",
    "portra": "(Portra, skin tones, warm:1.1)",
    "velvia": "(Velvia, ultra saturated:1.1)",
    "trichrome": "(trichrome, three-color:1.1)",
    "infrared": "(infrared photography, false color:1.2)",
    "uv": "(UV photography, fluorescent:1.1)",
}

# =============================================================================
# COMBINED MAP
# =============================================================================

ALL_MAPS: Dict[str, Dict[str, str]] = {
    "lens": LENS_MAP,
    "lighting": LIGHTING_MAP,
    "camera": CAMERA_MAP,
    "mood": MOOD_MAP,
    "color": COLOR_MAP,
}


def map_to_prompt(cinematic_terms: dict) -> str:
    """
    Map a dictionary of cinematic terms to a formatted prompt string.

    Args:
        cinematic_terms: Dictionary with categories as keys and lists of terms

    Returns:
        Formatted prompt string with weighted tags

    Example:
        >>> map_to_prompt({
        ...     "lens": ["anamorphic"],
        ...     "lighting": ["rim_light"],
        ...     "mood": ["cyberpunk"]
        ... })
        '(anamorphic lens, cinematic, 2.39:1 aspect ratio:1.3), (rim lighting, edge light:1.2), (cyberpunk, neon glow, rain:1.3)'
    """
    prompt_parts = []

    for category, terms in cinematic_terms.items():
        if not isinstance(terms, list):
            terms = [terms]

        for term in terms:
            mapped = map_single_term(term, category)
            if mapped:
                prompt_parts.append(mapped)

    return ", ".join(prompt_parts)


def map_single_term(term: str, category: Optional[str] = None) -> Optional[str]:
    """
    Map a single cinematic term to its prompt tag.

    Args:
        term: The cinematic term to map
        category: Optional category hint (lens, lighting, camera, mood, color)

    Returns:
        Mapped prompt tag or None if not found
    """
    term_lower = term.lower().strip().replace(" ", "_").replace("-", "_")

    if category and category in ALL_MAPS:
        if term_lower in ALL_MAPS[category]:
            return ALL_MAPS[category][term_lower]

    # Search all maps
    for map_name, mapping in ALL_MAPS.items():
        if term_lower in mapping:
            return mapping[term_lower]

    return None


def map_terms_list(terms: List[str]) -> List[str]:
    """
    Map a list of cinematic terms to prompt tags.

    Args:
        terms: List of cinematic terms

    Returns:
        List of mapped prompt tags
    """
    return [tag for term in terms if (tag := map_single_term(term))]


def get_all_terms() -> Dict[str, List[str]]:
    """
    Get all available cinematic terms organized by category.

    Returns:
        Dictionary with categories as keys and lists of available terms
    """
    return {
        category: sorted(mapping.keys())
        for category, mapping in ALL_MAPS.items()
    }


def search_terms(query: str) -> Dict[str, List[str]]:
    """
    Search for terms matching a query across all categories.

    Args:
        query: Search query

    Returns:
        Dictionary with matching terms organized by category
    """
    query_lower = query.lower()
    results = {}

    for category, mapping in ALL_MAPS.items():
        matches = [term for term in mapping.keys() if query_lower in term]
        if matches:
            results[category] = sorted(matches)

    return results