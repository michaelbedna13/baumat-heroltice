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

# Soubory ze starého webu (fotky, dokumenty, favicona).
# Přepni na True, jakmile je nahraješ do repa podle SOUBORY.md:
#   obrázky (.jpg, .png)   -> assets/img/
#   dokumenty (.pdf, .docx) -> assets/docs/
# Názvy souborů zůstávají stejné jako na starém webu. Do té doby se berou ze starého webu.
MISTNI_SOUBORY = False
SLOZKA_OBRAZKY = "assets/img"
SLOZKA_DOKUMENTY = "assets/docs"

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
    """Vrátí odkaz na soubor ze starého webu: buď tam, nebo na jeho kopii v repu."""
    if not MISTNI_SOUBORY:
        return f"{IMG}/{cesta_na_starem_webu}"
    nazev = cesta_na_starem_webu.split("/")[-1]
    slozka = SLOZKA_DOKUMENTY if nazev.lower().endswith((".pdf", ".docx", ".doc")) else SLOZKA_OBRAZKY
    # Obrázek může být v repu i jako WebP se stejným názvem (Apartman_3.webp místo Apartman_3.jpg).
    if slozka == SLOZKA_OBRAZKY:
        webp = nazev.rsplit(".", 1)[0] + ".webp"
        if (KOREN / slozka / webp).exists():
            return f"{root}{slozka}/{webp}"
    if not (KOREN / slozka / nazev).exists():
        CHYBI.add(f"{slozka}/{nazev}" + (" (nebo .webp)" if slozka == SLOZKA_OBRAZKY else ""))
    return f"{root}{slozka}/{nazev}"


def foto(nazev, root=""):
    if nazev not in FOTKY:
        raise SystemExit(f"Neznámá fotka: {nazev}. Doplň ji do FOTKY v build.py.")
    return soubor(FOTKY[nazev], root)


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
    if CHYBI:
        print("\nPOZOR, v repu chybí tyto soubory (web by na nich měl rozbité obrázky nebo odkazy):")
        for c in sorted(CHYBI):
            print("  " + c)
        raise SystemExit(1)
