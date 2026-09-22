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
WEB = "https://baumatheroltice.cz/"

# Dokumenty (ceník, řády) zatím odkazují na starý web.
# Přepni na True, jakmile je nahraješ do assets/docs/ se stejnými názvy (viz FOTKY.md).
MISTNI_DOKUMENTY = True
SLOZKA_OBRAZKY = "assets/img"
SLOZKA_DOKUMENTY = "assets/docs"

# python3 build.py --bez-kontroly sestaví stránky i bez nahraných fotek (jen pro náhled).
import sys
KONTROLA = "--bez-kontroly" not in sys.argv

# Fotky jsou v assets/img/ jako <klíč>.webp (například apartman-1.webp).
# Seznam, která fotka patří kam, je v FOTKY.md.
FOTKY = [
    "hero-uvod", "hero-ubytovani", "hero-aktivity", "hero-cenik", "hero-kontakt",
    "uvod-predstaveni", "uvod-cely-areal", "spravce",
    "apartman-1", "apartman-2", "apartman-3", "apartman-4", "apartman-5", "apartman-6",
    "slusovice-1", "slusovice-2", "slusovice-3", "slusovice-4", "slusovice-5",
    "chatky-1", "chatky-2", "chatky-3", "chatky-4",
    "brana-1", "brana-2", "brana-3", "brana-4",
    "kuchyne-1", "kuchyne-2", "kuchyne-3",
    "kuchynka-1", "kuchynka-2", "kuchynka-3",
    "socialky-1", "socialky-2", "socialky-3", "socialky-4", "socialky-5",
    "bazen-1", "bazen-2", "bazen-3", "bazen-4",
    "tenis-1", "tenis-2", "tenis-3",
    "beach-1", "beach-2", "stolni-tenis",
    "ohniste-1", "ohniste-2", "ohniste-3",
    "hriste-1", "hriste-2", "hriste-3",
    "klubovna-1", "klubovna-2", "klubovna-3",
]

IKONY = SABLONY / "ikony.svg"

# stránka -> (výstupní soubor, hloubka vůči kořeni, aktivní položka menu, jazyk, protějšek v druhém jazyce)
# Šablony anglické verze jsou v _sablony/en/, stejně jako její hlavička a patička.
STRANKY = {
    "index": ("index.html", "", "", "cs", "en/index"),
    "ubytovani": ("ubytovani/index.html", "../", "ubytovani", "cs", "en/ubytovani"),
    "aktivity": ("aktivity/index.html", "../", "aktivity", "cs", "en/aktivity"),
    "cenik": ("cenik/index.html", "../", "cenik", "cs", "en/cenik"),
    "kontakt": ("kontakt/index.html", "../", "kontakt", "cs", "en/kontakt"),
    "styleguide": ("styleguide.html", "", "", "cs", None),
    "en/index": ("en/index.html", "../", "", "en", "index"),
    "en/ubytovani": ("en/accommodation/index.html", "../../", "ubytovani", "en", "ubytovani"),
    "en/aktivity": ("en/activities/index.html", "../../", "aktivity", "en", "aktivity"),
    "en/cenik": ("en/pricing/index.html", "../../", "cenik", "en", "cenik"),
    "en/kontakt": ("en/contact/index.html", "../../", "kontakt", "en", "kontakt"),
}


def url_stranky(nazev, root):
    """Relativní odkaz na stránku z pohledu stránky s daným rootem."""
    vystup = STRANKY[nazev][0]
    return root + (vystup[: -len("index.html")] if vystup.endswith("index.html") else vystup)

def ikona(nazev):
    return f'<svg class="i" aria-hidden="true"><use href="#i-{nazev}"/></svg>'


CHYBI = set()


def soubor(cesta_na_starem_webu, root=""):
    """Dokument ze starého webu: odkaz tam, nebo na kopii v assets/docs/."""
    if not MISTNI_DOKUMENTY:
        return f"{IMG}/{cesta_na_starem_webu}"
    nazev = cesta_na_starem_webu.split("/")[-1]
    if not (KOREN / SLOZKA_DOKUMENTY / nazev).exists():
        CHYBI.add(f"{SLOZKA_DOKUMENTY}/{nazev}")
    return f"{root}{SLOZKA_DOKUMENTY}/{nazev}"


def foto(nazev, root=""):
    if nazev not in FOTKY:
        raise SystemExit(f"Neznámá fotka: {nazev}. Doplň ji do FOTKY v build.py a do FOTKY.md.")
    cesta = f"{SLOZKA_OBRAZKY}/{nazev}.webp"
    if not (KOREN / cesta).exists():
        CHYBI.add(cesta)
    return f"{root}{cesta}"


def doplnit(text, root, aktivni):
    text = text.replace("{{SPRITE}}", IKONY.read_text(encoding="utf-8").strip())
    text = text.replace("{{ROOT}}", root)
    text = re.sub(r"\{\{IMG\}\}/([^\"\s<]+)", lambda m: soubor(m.group(1), root), text)
    # aktivní položka v menu
    text = re.sub(
        r"\{\{A:([a-z]+)\}\}",
        lambda m: ' aria-current="page"' if m.group(1) == aktivni else "",
        text,
    )
    text = re.sub(r"\{\{i:([a-z0-9-]+)\}\}", lambda m: ikona(m.group(1)), text)
    # absolutní adresa pro og:image a strukturovaná data
    text = re.sub(r"\{\{foto-abs:([a-z0-9-]+)\}\}", lambda m: WEB + foto(m.group(1), ""), text)
    text = re.sub(r"\{\{foto:([a-z0-9-]+)\}\}", lambda m: foto(m.group(1), root), text)
    return text


def sestavit(nazev):
    vystup, root, aktivni, jazyk, protejsek = STRANKY[nazev]
    zdroj = (SABLONY / f"{nazev}.html").read_text(encoding="utf-8")
    slozka = SABLONY / "en" if jazyk == "en" else SABLONY
    for cast in ("hlava-meta", "hlavicka", "paticka"):
        soubor = slozka / f"{cast}.html"
        if not soubor.exists():
            soubor = SABLONY / f"{cast}.html"
        zdroj = zdroj.replace("{{" + cast + "}}", soubor.read_text(encoding="utf-8"))
    tady = url_stranky(nazev, root)
    tam = url_stranky(protejsek, root) if protejsek else url_stranky("en/index" if jazyk == "cs" else "index", root)
    zdroj = zdroj.replace("{{URL_CZ}}", tady if jazyk == "cs" else tam)
    zdroj = zdroj.replace("{{URL_EN}}", tady if jazyk == "en" else tam)
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
    if CHYBI and KONTROLA:
        print("\nPOZOR, v repu chybí tyto soubory (web by na nich měl rozbité obrázky nebo odkazy):")
        for c in sorted(CHYBI):
            print("  " + c)
        raise SystemExit(1)
