# SRS -- cinematic-prompt-formatter
Fecha: 2026-09-25 | Estado: Draft | Traza a: PRD prd-cinematic-prompt-formatter.md

## Requisitos funcionales

| ID | Requisito | Traza PRD | Prioridad |
|---|---|---|---|
| FR-001 | El sistema implementa: Parse cinematic terms (lens, lighting, camera movement, mood) | F1 | Must |
| FR-002 | El sistema implementa: Map to weighted prompt tags for AI image generation | F2 | Must |
| FR-003 | El sistema implementa: 50+ cinematic terms with precise mappings | F3 | Must |
| FR-004 | El sistema implementa: Preset styles for common cinematic looks | F4 | Must |
| FR-005 | El sistema implementa: Batch processing via CLI | F5 | Must |
| FR-006 | El sistema implementa: Model-specific optimization | F6 | Must |
| FR-007 | El sistema implementa: anamorphic - Anamorphic lens, cinematic 2.39:1 aspect ratio | F7 | Must |
| FR-008 | El sistema implementa: 35mm - Natural perspective lens | F8 | Must |

## Requisitos no funcionales

| ID | Requisito | Metrica | Traza |
|---|---|---|---|
| NFR-001 | Build reproducible | `build` pasa en CI | todos |
| NFR-002 | Calidad estatica | lint + typecheck sin errores | todos |
| NFR-003 | Seguridad | 0 secretos; validacion de entrada | FR-001 |
| NFR-004 | Observabilidad | logs estructurados y errores claros | todos |
| NFR-005 | Accesibilidad (si hay UI) | WCAG 2.1 AA | FR-001 |
| NFR-006 | CI verde | workflow en cada PR | todos |

## Trazabilidad

`PRD -> FR/NFR -> tests -> verificacion`. Todo cambio actualiza la documentacion
en el mismo PR y debe pasar la suite antes de fusionar.
