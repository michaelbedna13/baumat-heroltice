# baumatheroltice.cz

Statický web Rekreačního areálu Baumat Heroltice. Čisté HTML, CSS a JS bez buildu, hostované přes GitHub.

## Struktura

```
index.html              homepage (CZ)
ubytovani/ aktivity/ cenik/ kontakt/   podstránky (připravujeme)
en/                     anglická verze (připravujeme)
assets/css/style.css    paleta, typografie, layout
assets/js/main.js       mobilní menu, stav hlavičky
assets/fonts/           Bricolage Grotesque (woff2, latin + latin-ext, licence OFL)
```

## Lokální náhled

Stačí otevřít `index.html` v prohlížeči, nebo spustit `python3 -m http.server` a jít na http://localhost:8000.

## Paleta

| Název   | Hex     | Použití            |
|---------|---------|--------------------|
| Les     | #2F4A2B | hlavní, tmavé bloky |
| Mech    | #6B8A4E | v záloze |
| Krém    | #F5F0E3 | pozadí             |
| Písek   | #E8DFC9 | linky, podklad mapy |
| Uhel    | #1F2A1D | text               |
| Ohniště | #9A4F1E | v záloze |

## Zbývá

- Stáhnout fotky a dokumenty z WordPressu do `assets/img/` a `assets/docs/` a přepsat cesty (teď se odkazují na starý web).
- Logo jako SVG místo textového loga.
- Podstránky a EN verze.
- Recenze přes Google Places API (klíč omezený na doménu).
- Kalendář obsazenosti na /kontakt/.

Ikony: Tabler Icons (MIT).
