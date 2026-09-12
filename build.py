#!/usr/bin/env python3
"""Sestaví HTML stránky ze šablon v _sablony/.

Spuštění: python3 build.py
Vygenerované soubory (index.html, ubytovani/index.html, ...) se commitují do repa,
takže GitHub Pages funguje bez jakéhokoli buildu. Skript je jen pomůcka, aby se
hlavička a patička nemusely upravovat na každé stránce zvlášť.
"""

import re
import pathlib

KOREN = pathlib.Path(__file__).parent
SABLONY = KOREN / "_sablony"
IMG = "https://baumatheroltice.cz/wp-content/uploads"

IKONY = SABLONY / "ikony.svg"

# stránka -> (výstupní soubor, hloubka vůči kořeni, aktivní položka menu)
STRANKY = {
    "index": ("index.html", "", ""),
    "ubytovani": ("ubytovani/index.html", "../", "ubytovani"),
    "aktivity": ("aktivity/index.html", "../", "aktivity"),
    "cenik": ("cenik/index.html", "../", "cenik"),
    "kontakt": ("kontakt/index.html", "../", "kontakt"),
    "styleguide": ("styleguide.html", "", ""),
}

HVEZDY = '<svg class="i" aria-hidden="true"><use href="#i-star"/></svg>' * 5


def ikona(nazev):
    return f'<svg class="i" aria-hidden="true"><use href="#i-{nazev}"/></svg>'


def doplnit(text, root, aktivni):
    text = text.replace("{{SPRITE}}", IKONY.read_text(encoding="utf-8").strip())
    text = text.replace("{{ROOT}}", root)
    text = text.replace("{{IMG}}", IMG)
    text = text.replace("{{stars}}", HVEZDY)
    # aktivní položka v menu
    text = re.sub(
        r"\{\{A:([a-z]+)\}\}",
        lambda m: ' aria-current="page"' if m.group(1) == aktivni else "",
        text,
    )
    text = re.sub(r"\{\{i:([a-z0-9-]+)\}\}", lambda m: ikona(m.group(1)), text)
    return text


def sestavit(nazev):
    vystup, root, aktivni = STRANKY[nazev]
    zdroj = (SABLONY / f"{nazev}.html").read_text(encoding="utf-8")
    for cast in ("hlavicka", "paticka", "vyzva"):
        zdroj = zdroj.replace(
            "{{" + cast + "}}", (SABLONY / f"{cast}.html").read_text(encoding="utf-8")
        )
    hotovo = doplnit(zdroj, root, aktivni)

    zbytky = re.findall(r"\{\{[^}]+\}\}", hotovo)
    if zbytky:
        raise SystemExit(f"{nazev}: nevyplněné značky {zbytky}")
    if "—" in hotovo:
        raise SystemExit(f"{nazev}: obsahuje dlouhou pomlčku, viz DESIGN.md")

    cil = KOREN / vystup
    cil.parent.mkdir(parents=True, exist_ok=True)
    cil.write_text(hotovo, encoding="utf-8")
    print(f"{vystup} ({len(hotovo) // 1024} kB)")


if __name__ == "__main__":
    for nazev in STRANKY:
        sestavit(nazev)
