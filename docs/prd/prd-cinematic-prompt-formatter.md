# PRD -- cinematic-prompt-formatter
Fecha: 2026-09-25 | Estado: Draft (auditoria automatica, requiere revision humana) | Autor: auditoria belentani7 (NOIACORE)

## 1. Problema

﻿# Cinematic Prompt Formatter

## 2. Usuarios objetivo

- **Primario**: usuario final que necesita resolver el caso de uso de cinematic-prompt-formatter.
- **Secundario**: equipo/persona que mantiene y despliega el proyecto.
- **Terciario**: agentes CLI que operan sobre el repositorio.

## 3. Features (MoSCoW)

| ID | Feature | MoSCoW |
|---|---|---|
| F1 | Parse cinematic terms (lens, lighting, camera movement, mood) | Must |
| F2 | Map to weighted prompt tags for AI image generation | Must |
| F3 | 50+ cinematic terms with precise mappings | Must |
| F4 | Preset styles for common cinematic looks | Must |
| F5 | Batch processing via CLI | Must |
| F6 | Model-specific optimization | Must |
| F7 | anamorphic - Anamorphic lens, cinematic 2.39:1 aspect ratio | Must |
| F8 | 35mm - Natural perspective lens | Must |
| F90 | Checklist de produccion (build, tests, deploy, seguridad) | Should |
| F91 | Documentacion viva (esta cadena) | Must |

## 4. Criterios de aceptacion (GWT)

### F1 -- Parse cinematic terms (lens, lighting, camera movement, mood
- Given el usuario en el contexto de cinematic-prompt-formatter / When usa Parse cinematic terms (lens, lighting, camera move / Then obtiene el resultado esperado sin error.
- Given entrada invalida / When la envia / Then recibe un error generico y el detalle queda en logs.

### F2 -- Map to weighted prompt tags for AI image generation
- Given el usuario en el contexto de cinematic-prompt-formatter / When usa Map to weighted prompt tags for AI image generatio / Then obtiene el resultado esperado sin error.
- Given entrada invalida / When la envia / Then recibe un error generico y el detalle queda en logs.

### F3 -- 50+ cinematic terms with precise mappings
- Given el usuario en el contexto de cinematic-prompt-formatter / When usa 50+ cinematic terms with precise mappings / Then obtiene el resultado esperado sin error.
- Given entrada invalida / When la envia / Then recibe un error generico y el detalle queda en logs.

### F4 -- Preset styles for common cinematic looks
- Given el usuario en el contexto de cinematic-prompt-formatter / When usa Preset styles for common cinematic looks / Then obtiene el resultado esperado sin error.
- Given entrada invalida / When la envia / Then recibe un error generico y el detalle queda en logs.


## 5. Metricas de exito

- Build reproducible en un comando.
- CI verde en cada PR.
- Cero secretos en el repositorio.
- Documentacion actualizada en el mismo PR que el codigo.

## 6. Out of scope

- Funcionalidad no descrita en el README vigente.
- Cambios que rompan compatibilidad sin ADR que lo justifique.
