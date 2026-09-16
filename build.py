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

# Fotky: přepni na True, jakmile nahraješ obrázky do assets/img/ podle FOTKY.md.
# Do té doby se použijí fotky ze starého webu.
VLASTNI_FOTKY = False
IMG_LOKALNI = "assets/img"

# logický název -> cesta na starém webu (názvy souborů v assets/img/ jsou stejné jako klíč)
FOTKY = {
    "hero-areal": "2024/11/areal-1.jpg",
    "hero-ubytovani": "2024/11/Chatky_hl-foto-1-1536x1024.jpg",
    "hero-aktivity": "2024/11/Bazen_2-1536x1024.jpg",
    "hero-cenik": "2024/11/areal-2.jpg",
    "hero-kontakt": "2024/11/areal-1.jpg",
    "pro-koho": "2024/11/Ohniste_1-1536x1024.jpg",
    "cely-areal": "2024/11/Bazen_mainpage.jpg",
    "recenze-pozadi": "2024/11/areal-2.jpg",
    "apartman-1": "2024/11/Apartman_hl-foto-1536x1024.jpg",
    "apartman-2": "2024/11/Apartman_4-1536x1024.jpg",
    "apartman-3": "2024/11/Apartman_3-1536x1024.jpg",
    "apartman-karta": "2024/11/apartman_na-vysku.jpg",
    "slusovice-1": "2024/11/Bunky-slusovice_hl-foto-1-1536x1024.jpg",
    "slusovice-2": "2024/11/Bunky-slusovice_2-1536x1024.jpg",
    "slusovice-3": "2024/11/Slusovice_socialn-1536x1024.jpg",
    "slusovice-karta": "2024/11/slusovice_na-vysku.jpg",
    "chatky-1": "2024/11/Chatky_hl-foto-1-1536x1024.jpg",
    "chatky-2": "2024/11/Chatky_2-1536x1024.jpg",
    "chatky-3": "2024/11/Chatky_3-1536x1024.jpg",
    "chatky-karta": "2024/11/chatky_na-vysku.jpg",
    "brana-1": "2024/11/chatky-u-hl-brany-_hl-foto-1-1536x1024.jpg",
    "brana-2": "2024/11/chatky-u-hl-brany-_2-1-1536x1024.jpg",
    "brana-3": "2024/11/chatky-u-hl-brany-_3-1-1536x1024.jpg",
    "kuchyne-1": "2024/11/Kuchyne-a-jidelna_1-1536x1024.jpg",
    "kuchyne-2": "2024/11/Kuchyne-a-jidelna_2-1536x1024.jpg",
    "kuchyne-3": "2024/11/Kuchyne-a-jidelna_3-1536x1024.jpg",
    "kuchynka-1": "2024/11/kuchynka_hl.photo_-1536x1024.jpg",
    "kuchynka-2": "2024/11/kuchynka_2-1536x1024.jpg",
    "kuchynka-3": "2024/11/kuchynka_3-1536x1024.jpg",
    "socialky-1": "2024/11/Hl.socialky_1-1536x1024.jpg",
    "socialky-2": "2024/11/Hl.socialky_2-1-1536x1024.jpg",
    "socialky-3": "2024/11/Hl.socialky_3-1-1536x1024.jpg",
    "bazen-1": "2024/11/Bazen_2-1536x1024.jpg",
    "bazen-2": "2024/11/Bazen_3-1536x1024.jpg",
    "bazen-3": "2024/11/Bazen_mainpage.jpg",
    "tenis-1": "2024/11/tenis_hl.photo_-1536x1024.jpg",
    "tenis-2": "2024/12/tenis-2-1536x1024.jpg",
    "beach-1": "2024/11/beach_hl.photo_-1536x1024.jpg",
    "beach-2": "2024/11/Beach-1536x1024.jpg",
    "stolni-tenis": "2024/11/ping-pong-1536x1024.jpg",
    "ohniste-1": "2024/11/Ohniste_1-1536x1024.jpg",
    "ohniste-2": "2024/11/Ohniste_2-1-1536x1024.jpg",
    "ohniste-3": "2024/11/Ohniste_3-1-1536x1024.jpg",
    "hriste-1": "2024/11/Detske-hriste-1536x1024.jpg",
    "hriste-2": "2024/11/Detske-hriste_2-1536x1024.jpg",
    "klubovna-1": "2024/11/klubovna_hl.photo_-1536x1024.jpg",
    "klubovna-2": "2024/11/klubovna_2-1536x1024.jpg",
    "spravce": "2024/11/Josef-Kavalec_spravce.jpg"
}

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


def foto(nazev, root=""):
    """Vrátí cestu k fotce. Dokud nejsou vlastní fotky, bere je ze starého webu."""
    if nazev not in FOTKY:
        raise SystemExit(f"Neznámá fotka: {nazev}. Doplň ji do FOTKY v build.py a do FOTKY.md.")
    if VLASTNI_FOTKY:
        return f"{root}{IMG_LOKALNI}/{nazev}.jpg"
    return f"{IMG}/{FOTKY[nazev]}"


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
    text = re.sub(r"\{\{foto:([a-z0-9-]+)\}\}", lambda m: foto(m.group(1), root), text)
    return text


def sestavit(nazev):
    vystup, root, aktivni = STRANKY[nazev]
    zdroj = (SABLONY / f"{nazev}.html").read_text(encoding="utf-8")
    for cast in ("hlavicka", "paticka", "vyzva", "zaver"):
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
