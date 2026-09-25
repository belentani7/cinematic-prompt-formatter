# ADR-001 -- Auditoria documental y stack de cinematic-prompt-formatter
Fecha: 2026-09-25 | Estado: aceptado

## Contexto

El repositorio carecia de cadena documental formal (PRD/SRS/SDD/ADR/plan) y de
reglas explicitas para agentes. Stack detectado: Python.

## Decision

1. Anadir documentacion viva en `docs/` (aditiva, sin tocar codigo existente).
2. Anadir `AGENTS.md` y `.cursorrules` con reglas de trabajo.
3. Mantener el stack actual; cualquier cambio de arquitectura requiere un ADR nuevo.

## Consecuencias

- Positivas: trazabilidad, onboarding mas rapido, agentes con reglas claras.
- Negativas (asumidas): documentacion que puede quedar desactualizada si no se
  mantiene en el mismo PR que el codigo.
- Reversible: los documentos son aditivos y pueden revisarse por PR.
