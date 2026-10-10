#!/usr/bin/env python3
"""Stáhne Google Kalendář správce (tajná adresa ve formátu iCal) a vytvoří
assets/data/obsazenost.json pro kalendář na webu.

Na web se dostanou data, stav dne (obsazeno / castecne) a názvy událostí,
aby u termínů bylo vidět, o jakou akci jde. POZOR: název události je veřejný.
Co má zůstat jen v kalendáři (jména hostů, telefon, poznámka), napiš v názvu
za dvě lomítka: "Svatba // Novákovi, 777 123 456" zveřejní jen "Svatba".
Popis události (DESCRIPTION) se nezveřejňuje nikdy.

Pravidla (dají se upravit níže):
- Událost, jejíž název obsahuje "plná kapacita" (nebo "celý areál", "obsazeno"), označí dny jako "obsazeno".
- Jakákoli jiná událost, třeba "poloviční kapacita", označí dny jako "castecne".
- Celodenní událost obsadí přesně ty dny, přes které je v kalendáři natažená.
- U události s časem se počítají noci: od 3. 14:00 do 5. 10:00 obsadí 3. a 4.
- Diakritika a velikost písmen nevadí.
- Název události se vypíše pod kalendářem u příslušného měsíce, bez údaje o kapacitě na konci.

Spouští se automaticky přes GitHub Actions (.github/workflows/kalendar.yml).
Adresa kalendáře je v tajném nastavení repa: KALENDAR_ICAL_URL.
Víc kalendářů jde zadat oddělených čárkou.
"""
import datetime as dt
import json
import os
import pathlib
import sys
import unicodedata
import urllib.request

CELY_AREAL = ["plna kapacita", "cely areal", "obsazeno", "cely objekt"]
SOUKROME = "//"   # co je v názvu za tímto, se nezveřejní
MAX_NAZEV = 90    # delší název se zkrátí
DNY_ZPET = 7
DNY_DOPREDU = 550
VYSTUP = pathlib.Path(__file__).resolve().parent.parent / "assets" / "data" / "obsazenost.json"


def bez_diakritiky(text):
    return "".join(c for c in unicodedata.normalize("NFD", text.lower()) if unicodedata.category(c) != "Mn")


def stahnout(url):
    req = urllib.request.Request(url, headers={"User-Agent": "baumatheroltice-kalendar"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")


def radky(ics):
    """Rozbalí zalomené řádky podle RFC 5545."""
    vysledek = []
    for radek in ics.splitlines():
        if radek.startswith((" ", "\t")) and vysledek:
            vysledek[-1] += radek[1:]
        else:
            vysledek.append(radek)
    return vysledek


def rozbal_text(hodnota):
    """Odstraní escapování podle RFC 5545: \\n, \\, , \\; , \\\\."""
    vysledek = []
    i = 0
    while i < len(hodnota):
        if hodnota[i] == "\\" and i + 1 < len(hodnota):
            dalsi = hodnota[i + 1]
            vysledek.append("\n" if dalsi in "nN" else dalsi)
            i += 2
        else:
            vysledek.append(hodnota[i])
            i += 1
    return "".join(vysledek)


def nazev_pro_web(summary):
    """Veřejný popisek akce. Co je v názvu za //, zůstane jen v kalendáři.

    Z konce názvu se odřízne údaj o kapacitě ("Svatba - plná kapacita"), protože
    totéž už na webu říká barva dne a legenda pod kalendářem.
    """
    text = " ".join(rozbal_text(summary).split(SOUKROME)[0].split())
    for oddelovac in (" - ", " – ", " — ", " | ", ", "):
        cast = text.rsplit(oddelovac, 1)
        if len(cast) == 2 and cast[0].strip():
            konec = bez_diakritiky(cast[1])
            if "kapacit" in konec or any(slovo in konec for slovo in CELY_AREAL):
                text = cast[0].strip()
                break
    if len(text) > MAX_NAZEV:
        text = text[: MAX_NAZEV - 1].rstrip(" ,;-") + "…"
    return text


def datum(hodnota):
    hodnota = hodnota.strip()
    if len(hodnota) >= 8 and hodnota[:8].isdigit():
        return dt.date(int(hodnota[:4]), int(hodnota[4:6]), int(hodnota[6:8]))
    return None


def udalosti(ics):
    udalost = None
    for radek in radky(ics):
        if radek == "BEGIN:VEVENT":
            udalost = {}
        elif radek == "END:VEVENT" and udalost is not None:
            yield udalost
            udalost = None
        elif udalost is not None and ":" in radek:
            klic, hodnota = radek.split(":", 1)
            udalost[klic.split(";")[0].upper()] = hodnota


def main():
    adresy = [a.strip() for a in os.environ.get("KALENDAR_ICAL_URL", "").split(",") if a.strip()]
    if not adresy:
        sys.exit("Chybí KALENDAR_ICAL_URL (tajná adresa kalendáře ve formátu iCal).")

    dnes = dt.date.today()
    od, do = dnes - dt.timedelta(days=DNY_ZPET), dnes + dt.timedelta(days=DNY_DOPREDU)
    terminy = {}
    akce = {}

    for adresa in adresy:
        for u in udalosti(stahnout(adresa)):
            if u.get("STATUS", "").upper() == "CANCELLED":
                continue
            zacatek = datum(u.get("DTSTART", ""))
            konec = datum(u.get("DTEND", "")) or zacatek
            if not zacatek:
                continue
            if konec <= zacatek:
                konec = zacatek + dt.timedelta(days=1)
            nazev = bez_diakritiky(u.get("SUMMARY", ""))
            stav = "obsazeno" if any(slovo in nazev for slovo in CELY_AREAL) else "castecne"
            prvni, posledni = max(zacatek, od), min(konec, do) - dt.timedelta(days=1)
            if prvni > posledni:
                continue
            den = prvni
            while den <= posledni:
                klic = den.isoformat()
                if terminy.get(klic) != "obsazeno":
                    terminy[klic] = stav
                den += dt.timedelta(days=1)
            popisek = nazev_pro_web(u.get("SUMMARY", ""))
            if popisek:
                # Stejná akce ve dvou kalendářích se vypíše jen jednou.
                akce[(prvni.isoformat(), posledni.isoformat(), popisek)] = stav

    seznam = [
        {"od": o, "do": d, "nazev": n, "stav": akce[(o, d, n)]}
        for o, d, n in sorted(akce)
    ]
    data = {
        "aktualizovano": dnes.isoformat(),
        "terminy": dict(sorted(terminy.items())),
        "akce": seznam,
    }
    VYSTUP.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Uloženo {len(terminy)} dní a {len(seznam)} akcí do {VYSTUP}")


if __name__ == "__main__":
    main()
