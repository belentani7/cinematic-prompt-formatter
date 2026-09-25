# SDD / Design Doc -- cinematic-prompt-formatter
Fecha: 2026-09-25 | Estado: Draft

## Arquitectura general

Stack: Python. Estructura de primer nivel detectada:

```
  .github
  .gitignore
  LICENSE
  README.md
  SECURITY.md
  docs
  ecosistema.html
  formatter
  magic
  pyproject.toml
  tests
```

CI: deploy-pages.yml.

## Decisiones clave

Ver `docs/adr/`. Regla: una fuente de verdad por concern, contratos de frontera
claros y direccion de dependencias sin ciclos.

## Flujos criticos

1. Desarrollo local -> build -> test -> CI.
2. Cambio -> PR -> revision -> merge -> deploy (si aplica).

## Estrategia de verificacion

- Build y tests en CI en cada PR.
- Revision de seguridad (cero secretos, validacion).
- Comprobacion de deploy segun la matriz de plataforma.

## Limites y riesgos

- Deuda tecnica no documentada: registrar como ADR antes de refactor mayor.
- Dependencias externas: fijar versiones y lockfile.
