#!/usr/bin/env python3
"""Stáhne Google Kalendář správce (tajná adresa ve formátu iCal) a vytvoří
assets/data/obsazenost.json pro kalendář na webu.

Na web se dostanou jen data a stav (obsazeno / castecne). Názvy událostí,
jména hostů ani poznámky se nikam neukládají.

Pravidla (dají se upravit níže):
- Událost, jejíž název obsahuje některé slovo z CELY_AREAL, označí dny jako "obsazeno".
- Jakákoli jiná událost označí dny jako "castecne" (část ubytování je obsazená).
- Den se počítá jako noc: pobyt od 3. do 5. obsadí 3. a 4. (odjezdový den zůstane volný).

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

CELY_AREAL = ["cely areal", "obsazeno", "cely objekt"]
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
            den = max(zacatek, od)
            while den < min(konec, do):
                klic = den.isoformat()
                if terminy.get(klic) != "obsazeno":
                    terminy[klic] = stav
                den += dt.timedelta(days=1)

    data = {"aktualizovano": dnes.isoformat(), "terminy": dict(sorted(terminy.items()))}
    VYSTUP.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Uloženo {len(terminy)} dní do {VYSTUP}")


if __name__ == "__main__":
    main()
