# Asistencia Digital — 1ª Compañía de Bomberos de Coquimbo

<p align="center"><img src="docs/branding/app-icon.svg" width="150" alt="Icono minimalista de Asistencia Digital Bomberos"></p>


**Autor:** [Patricio Varela C.](https://github.com/2674321) · **ORCID:** [0009-0002-1087-9445](https://orcid.org/0009-0002-1087-9445) · **Licencia:** [MIT](LICENSE) · **Citación:** [CITATION.cff](CITATION.cff)

PWA histórica para registrar asistencia de voluntarios, diseñada con funcionamiento
offline y sincronización posterior. El proyecto está **descontinuado** porque su
adopción requiere replicar el formato institucional oficial con exactitud.

> ▶️ **[Demo online](https://2674321.github.io/asistencia-digital-bomberos/)** · datos de prueba


[![Licencia MIT](https://img.shields.io/badge/licencia-MIT-blue)](LICENSE) ![Versión](https://img.shields.io/badge/versi%C3%B3n-v1.0-green) ![Estado](https://img.shields.io/badge/estado-deprecated-red) [![CI](https://github.com/2674321/asistencia-digital-bomberos/actions/workflows/ci.yml/badge.svg)](https://github.com/2674321/asistencia-digital-bomberos/actions/workflows/ci.yml)


## Características

- **Registro de asistencia** de voluntarios en tiempo real
- **Funcionamiento offline** mediante Service Worker
- **Instalable** como aplicación en dispositivos móviles y de escritorio
- **Sincronización automática** cuando se restaura la conexión
- **Interfaz responsive** optimizada para todos los dispositivos

## Capturas

> Datos de prueba · capturas: agosto 2026 · v1 · [demo online](https://2674321.github.io/asistencia-digital-bomberos/)

![Vista principal](docs/screenshots/asistencia-principal.png)
*Vista principal — escritorio · ago 2026 · v1*

![Vista móvil](docs/screenshots/asistencia-movil.png)
*Vista móvil (PWA instalable) · ago 2026 · v1*

## Tecnologías

- HTML5 / CSS3 / JavaScript vanilla
- Service Worker (PWA)
- JSON para almacenamiento local
- Manifest para instalación

## Archivos Principales

| Archivo | Descripción |
|---------|-------------|
| `asistencia_primera_compania_v3.html` | Aplicación principal (punto de entrada) |
| `sw.js` | Service Worker para funcionalidad offline |
| `manifest.json` | Manifest de la PWA |
| `voluntarios.json` | Base de datos local de voluntarios |

## Instalación

### Como PWA (Recomendado)
1. Abrir `asistencia_primera_compania_v3.html` en un navegador moderno
2. Hacer clic en "Instalar" o "Agregar a pantalla de inicio"
3. La app aparecerá como una aplicación nativa

### Como página web
1. Copiar todos los archivos a un servidor web estático
2. Acceder a `asistencia_primera_compania_v3.html` desde el navegador

## Uso

1. **Registrar asistencia:** Seleccionar voluntario y marcar presente/ausente
2. **Ver reportes:** Consultar historial de asistencia
3. **Exportar datos:** Descargar información en formato CSV

## Desarrollo

### Requisitos
- Navegador web moderno (Chrome, Firefox, Safari, Edge)
- Habilitar JavaScript
- Para desarrollo local: servidor HTTP local (por ejemplo, Live Server de VS Code)

### Estructura del Código
- **Frontend:** HTML5 + CSS3 + JavaScript vanilla
- **Almacenamiento:** JSON local + Service Worker Cache
- **Sin dependencias externas**

## Licencia

Uso interno - 1ra Compañía de Bomberos


## Versiones

- **Actual (v3+):** `asistencia_primera_compania_v3.html` — PWA offline de un solo archivo.
- **v1 (primer formato):** `versiones-anteriores/v1-primer-formato/` — versión inicial,
  fusionada desde el antiguo repositorio `asistencia-1cia-coquimbo`.

> ℹ️ `voluntarios.json` contiene **datos de prueba** (nombres ficticios); el listado real se gestiona localmente.
