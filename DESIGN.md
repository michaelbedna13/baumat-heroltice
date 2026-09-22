# Design webu Baumat Heroltice

Verze 6, čistá. Inspirace: cambriavacationrentals.com. Bílá stránka, jedna zelená, bílé karty a fotka přes celou šířku v hero.

## Barvy

| Token | Hex | Použití |
|---|---|---|
| `--papir` | #FFFFFF | podklad stránky |
| `--seda` | #F5F4EF | střídavé sekce (`.pas`), pole formuláře |
| `--pisek` | #EFEDE6 | plocha pod fotkou, hover polí |
| `--oliva` | #3E5A2F | jediná barva značky: tlačítka, odkazy, ikony, ceny |
| `--oliva-2` | #324A25 | hover |
| `--oliva-sv` | #E6ECDD | kruh pod ikonou, avatar u recenze |
| `--les` | #1E2A1C | jen patička |
| `--text` | #1F2420 | text |
| `--sedy` | #676C63 | vedlejší text |
| `--linka` | #E6E3DA | rámečky karet a oddělovače |

Pravidla:
- Bílá stránka, sekce se střídají bílá a světle šedá. Tmavá je jen patička.
- Zelená je jediná akcentová barva.
- Karty: bílé, tenký rámeček, rádius 16 px. Stín se objeví až po najetí myší.

## Kalendář obsazenosti

Klasické barvy stavů, aby se daly přečíst na první pohled: volno světle zelená #E2F0DA, částečně obsazeno žluté šrafování (#FCE7B6 a #F7D993), obsazeno červená #D8453A. Minulé dny jsou šedé a zeslabené, dnešek má tmavý rámeček. Šrafování odliší částečnou obsazenost i bez barvy.

## Přepínač jazyka

Pilulka CZ / EN (`.jazyky`). Na fotce je sklo s bílou aktivní volbou, v přilepené liště šedá s olivovou aktivní volbou, na mobilu je v menu vedle tlačítka Volné termíny.

## Písmo

Hanken Grotesk, jedna rodina, variabilní řez uložený lokálně (latin a latin-ext, OFL). Nadpisy řez 560, text 400, důraz 600. Žádné verzálky a žádné štítky nad nadpisy sekcí.

## Rozvržení

- Obsah 1200 px, boční odsazení 20 až 56 px. Mezera mezi sekcemi 80 až 128 px.
- Nadpisy sekcí jsou na středu s krátkým perexem pod sebou.
- Hero: fotka přes celou šířku okna, navigace na fotce, nadpis, perex a dvě tlačítka na středu (volné termíny a telefon). Pod hero proužek se čtyřmi fakty. Po odscrollování se objeví bílá lišta s navigací.

## Komponenty

| Třída | Co to je |
|---|---|
| `.pas` | světle šedá sekce přes celou šířku, uvnitř vždy `.wrap`; `.pas--les` je patička |
| `.tmave` | přidat na tmavý pás, přepne linky a vedlejší text na světlé varianty |
| `.wrap` | obsah na šířku stránky |
| `.sklo` | matné sklo na fotce |
| `.hlava` | hlavička sekce: nadpis vlevo, krátký text a odkaz vpravo |
| `.lista`, `.menu`, `.drobky` | navigace na fotce v hero |
| `.hero`, `.hero--pod`, `.hero--s-formularem`, `.hodnoceni` | úvodní blok s fotkou |
| `.fakta-pruh`, `.predstaveni` | proužek s fakty pod hero, úvodní blok fotka a text |
| `.vyhody` | čtyři body s ikonou v kruhu |
| `.mozaika`, `.dlazdice` | mřížka odkazových karet |
| `.karty`, `.karta` | bílé karty ubytování s fotkou nahoře |
| `.celek`, `.celek__cena` | pás s cenou celého areálu |
| `.ikony`, `.ikony--svetle` | seznam s linkovými ikonami |
| `.prehled` | tabulka typů ubytování s odkazy na kotvy |
| `.typ`, `.galerie`, `.parametry` | detail typu ubytování |
| `.polozky`, `.polozka`, `.aktivity`, `.aktivita--velka` | karty zázemí a aktivit |
| `.cenik-skupina`, `.cenik`, `.kotvy` | ceník |
| `.kontakty`, `.poloha`, `.mapa`, `.osoba` | kontakty |
| `.odkazy` | odkazové řádky (dokumenty, rozcestník) |
| `.kalendar-blok`, `.legenda` | kalendář obsazenosti |
| `.lightbox` | prohlížeč fotek (vytváří ho main.js) |

Živé ukázky jsou ve `styleguide.html`.

## Texty

- Žádné dlouhé pomlčky. `build.py` stránku s dlouhou pomlčkou nesestaví.
- Mezi číslem a jednotkou nezlomitelná mezera: `290&nbsp;Kč`, `25&nbsp;km`.
- Na web patří jen údaje, které Baumat potvrdil. Nic nedomýšlet (počty objektů, časy dojezdu, lhůty odpovědí).
