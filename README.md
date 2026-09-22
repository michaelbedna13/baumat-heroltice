# baumatheroltice.cz

Statický web Rekreačního areálu Baumat Heroltice. Čisté HTML, CSS a JS bez buildu, hostované přes GitHub.

## Struktura

```
index.html              homepage (CZ)
ubytovani/ aktivity/ cenik/ kontakt/   podstránky (CZ)
en/                     anglická verze (připravujeme)
_sablony/               zdrojové šablony a sdílené části (hlava-meta, hlavicka, paticka)
build.py                sestaví HTML ze šablon
assets/css/style.css    celý stylopis (mobile-first, tokeny a komponenty)
DESIGN.md               pravidla designu a seznam komponent
assets/js/main.js       mobilní menu, přilepená lišta, prohlížeč fotek, kalendář
assets/data/obsazenost.json   termíny pro kalendář (zatím UKÁZKOVÁ data)
assets/img/             fotky a logo (viz FOTKY.md)
FOTKY.md                názvy a formáty fotek, návod na logo
styleguide.html         živé ukázky komponent (noindex)
assets/fonts/           Hanken Grotesk, variabilní (woff2, latin + latin-ext, licence OFL)
```

## Úpravy a sestavení

Obsah se edituje v `_sablony/`, pak stačí spustit:

```
python3 build.py
```

Hotové HTML se commituje, hosting nic nebuilduje. Náhled: `python3 -m http.server` a http://localhost:8000.

## Zbývá

- Potvrdit u Baumatu přesnou adresu areálu (katalogy uvádějí Heroltice 166 i Heroltice 1) a doplnit ji do kontaktu a JSON-LD.
- Stáhnout fotky a dokumenty z WordPressu do `assets/img/` a `assets/docs/` a přepsat cesty (teď se odkazují na starý web).
- Logo: značka je zatím můj návrh (kruh, štít chatky, vlna řeky). Pokud má Baumat vlastní logo, nahradit symbol `i-znacka` ve `_sablony/ikony.svg`.
- Anglická verze všech stránek (pozor: v současné EN verzi jsou staré ceny).
- Recenze přes Google Places API (klíč omezený na doménu). Zatím jsou na homepage tři statické citace bez hvězd.
- **Kalendář na /kontakt/ běží na ukázkových datech.** Před spuštěním přepsat `assets/data/obsazenost.json` skutečnou obsazeností, nebo napojit export z Google kalendáře (stavy: `obsazeno`, `castecne`).

Ikony: Tabler Icons (MIT).


## Anglická verze

Anglické stránky jsou v `en/` (`/en/`, `/en/accommodation/`, `/en/activities/`, `/en/pricing/`, `/en/contact/`). Jejich šablony jsou v `_sablony/en/`, včetně vlastní hlavičky a patičky. Sdílí se `hlava-meta.html`, CSS, JS, ikony a fotky.

- Přepínač CZ / EN vede vždy na protějšek aktuální stránky. Páry jsou definované v `STRANKY` v `build.py`.
- Když změníš text v české šabloně, uprav ho i v anglické. Build to nehlídá.
- JavaScript (kalendář, prohlížeč fotek) bere jazyk z `<html lang>` a texty má v objektu `T` v `main.js`.
- Ceník a řády ke stažení jsou jen česky, v EN verzi jsou odkazy označené „in Czech".
- Názvy ubytování odpovídají původnímu anglickému webu: Apartment, Cottages (buňky Slušovice), Cabins (chatky klasické), Cabins by the Main Gate, Kitchen & Dining Hall, Kitchenettes, Main Sanitary Facilities. Areál se jmenuje Baumat Heroltice Recreation Area.
- Recenze jsou v EN verzi přeložené a označené „translated from Czech".
- Měna je CZK s anglickým oddělovačem tisíců (40,000 CZK), hodnocení 4.5.
