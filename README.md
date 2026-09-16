# baumatheroltice.cz

Statický web Rekreačního areálu Baumat Heroltice. Čisté HTML, CSS a JS bez buildu, hostované přes GitHub.

## Struktura

```
index.html              homepage (CZ)
ubytovani/ aktivity/ cenik/ kontakt/   podstránky (CZ)
en/                     anglická verze (připravujeme)
_sablony/               zdrojové šablony a sdílené části
build.py                sestaví HTML ze šablon
assets/css/style.css    paleta, typografie, layout
assets/js/main.js       mobilní menu, hlavička, prohlížeč fotek, kalendář
assets/data/obsazenost.json   termíny pro kalendář (zatím UKÁZKOVÁ data)
assets/img/             fotky a logo (viz FOTKY.md)
FOTKY.md                názvy a formáty fotek, návod na logo
DESIGN.md               pravidla designu, komponenty, typy sekcí
styleguide.html         živé ukázky komponent (noindex)
assets/fonts/           Bricolage Grotesque (woff2, latin + latin-ext, licence OFL)
```

## Úpravy a sestavení

Obsah se edituje v `_sablony/`, pak stačí spustit:

```
python3 build.py
```

Hotové HTML se commituje, hosting nic nebuilduje. Náhled: `python3 -m http.server` a http://localhost:8000.

## Paleta

| Název   | Hex     | Použití            |
|---------|---------|--------------------|
| Les     | #2F4A2B | hlavní, tmavé bloky |
| Mech    | #6B8A4E | v záloze |
| Krém    | #F5F0E3 | pozadí             |
| Písek   | #E8DFC9 | linky, podklad mapy |
| Uhel    | #12211B | text |
| Ohniště | #9A4F1E | v záloze |

## Zbývá

- Potvrdit u Baumatu přesnou adresu areálu (katalogy uvádějí Heroltice 166 i Heroltice 1) a doplnit ji do kontaktu a JSON-LD.
- Stáhnout fotky a dokumenty z WordPressu do `assets/img/` a `assets/docs/` a přepsat cesty (teď se odkazují na starý web).
- Logo: značka je zatím můj návrh (kruh, štít chatky, vlna řeky). Pokud má Baumat vlastní logo, nahradit symbol `i-znacka` ve `_sablony/ikony.svg`.
- Fotky mají jednotnou barevnou korekci přes CSS (`.foto`). Po novém focení ji lze zeslabit.
- Anglická verze všech stránek (pozor: v současné EN verzi jsou staré ceny).
- Recenze přes Google Places API (klíč omezený na doménu). Do té doby odstranit zástupné hvězdy u citací.
- **Kalendář na /kontakt/ běží na ukázkových datech.** Před spuštěním přepsat `assets/data/obsazenost.json` skutečnou obsazeností, nebo napojit export z Google kalendáře (stavy: `obsazeno`, `castecne`).

Ikony: Tabler Icons (MIT).
