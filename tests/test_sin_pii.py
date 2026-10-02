"""Verifica que los fixtures de voluntarios (histórico y demo) sean 100 % sintéticos.

No reproduce ningún valor sensible: comprueba el *patrón* de los datos, de modo
que el propio test no pueda convertirse en una copia de la información real.

Ejecutar:  python3 tests/test_sin_pii.py   (o `pytest tests/`)
"""
from __future__ import annotations

import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
FIXTURES = [
    RAIZ / "versiones-anteriores" / "v1-primer-formato" / "voluntarios.json",
    RAIZ / "demo" / "voluntarios.json",
]

PATRON_NOMBRE = re.compile(r"^Voluntario Demo \d{2}$")
CLAVES = {"nombre", "cargo", "seccion", "activo", "subseccion"}


def cargar(fixture):
    return json.loads(fixture.read_text(encoding="utf-8"))


def test_fixtures_son_listas():
    for fixture in FIXTURES:
        datos = cargar(fixture)
        assert isinstance(datos, list) and datos, f"{fixture} debe ser una lista no vacía"


def test_esquema_preservado():
    for fixture in FIXTURES:
        for registro in cargar(fixture):
            assert set(registro) == CLAVES, f"esquema inesperado en {fixture}: {sorted(registro)}"
            assert isinstance(registro["nombre"], str)
            assert isinstance(registro["activo"], bool)


def test_nombres_son_sinteticos():
    for fixture in FIXTURES:
        for registro in cargar(fixture):
            assert PATRON_NOMBRE.match(registro["nombre"]), (
                f"nombre no sintético en {fixture}: todos deben ser 'Voluntario Demo NN'"
            )


if __name__ == "__main__":
    test_fixtures_son_listas()
    test_esquema_preservado()
    test_nombres_son_sinteticos()
    print("OK: fixtures sintéticos, esquema preservado")
