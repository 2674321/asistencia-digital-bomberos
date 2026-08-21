# Instalación — Asistencia Digital (PWA)

Aplicación web progresiva **100% estática**: sin backend ni base de datos.

## Demo online

<https://2674321.github.io/asistencia-digital-bomberos/>

## Instalar en un celular

1. Abrir la demo en Chrome (Android) o Safari (iOS).
2. Menú → *Añadir a pantalla de inicio* / *Instalar aplicación*.
3. Funciona sin conexión gracias al service worker.

## Servir localmente

Los navegadores exigen HTTPS o localhost para registrar service workers:

```bash
cd demo
python3 -m http.server 8080
# → http://localhost:8080/asistencia_primera_compania_v3.html
```

> **Estructura:** la app vive en `demo/` y espera sus logos **un nivel arriba**
> (`../img-logo-1cia-sin-fondo.png`, `../LOGO CBC.webp`). Si mueves la carpeta,
> respeta esa relación.

## Datos

`demo/voluntarios.json` contiene **datos de prueba** (nombres ficticios).
Para uso real, reemplázalo localmente con el listado verdadero y **no lo publiques**.
