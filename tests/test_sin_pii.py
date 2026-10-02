"""Verifica que el fixture histórico de voluntarios sea 100 % sintético.

No reproduce ningún valor sensible: comprueba el *patrón* de los datos, de modo
que el propio test no pueda convertirse en una copia de la información real.

Ejecutar:  python3 tests/test_sin_pii.py   (o `pytest tests/`)
"""
from __future__ import annotations

import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
FIXTURE = RAIZ / "versiones-anteriores" / "v1-primer-formato" / "voluntarios.json"

PATRON_NOMBRE = re.compile(r"^Voluntario Demo \d{2}$")
CLAVES = {"nombre", "cargo", "seccion", "activo", "subseccion"}


def cargar():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def test_fixture_es_lista():
    datos = cargar()
    assert isinstance(datos, list) and datos, "el fixture debe ser una lista no vacía"


def test_esquema_preservado():
    for registro in cargar():
        assert set(registro) == CLAVES, f"esquema inesperado: {sorted(registro)}"
        assert isinstance(registro["nombre"], str)
        assert isinstance(registro["activo"], bool)


def test_nombres_son_sinteticos():
    for registro in cargar():
        assert PATRON_NOMBRE.match(registro["nombre"]), (
            "todos los nombres deben seguir el patrón 'Voluntario Demo NN'"
        )


if __name__ == "__main__":
    test_fixture_es_lista()
    test_esquema_preservado()
    test_nombres_son_sinteticos()
    print("OK: fixture sintético, esquema preservado")
