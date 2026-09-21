# Design webu Baumat Heroltice

Verze 5. Fotka v hero přes celý úvodní blok, pod ní se střídají vzdušné sekce na papíře a několik plných pásů v tmavé lesní a olivové.

## Barvy

| Token | Hex | Použití |
|---|---|---|
| `--les` | #222C1D | tmavé pásy (celý areál, správce, patička), hlavní tlačítko na světlé ploše, obsazené dny |
| `--les-2` | #2F3C28 | hover tmavých prvků |
| `--oliva` | #4B5E33 | olivový pás (recenze, zázemí, dokumenty), plná dlaždice, ikony na světlé |
| `--salvej` | #B8C29F | akcent na tmavé ploše (ikony), částečně obsazené dny |
| `--papir` | #F4F0E6 | podklad stránky |
| `--bila` | #FBF9F3 | vyvýšené plochy: formulář, dlaždice, kalendář |
| `--pisek` | #E8E2D2 | tlumená plocha, hover polí |
| `--text` | #1D2319 | text |
| `--sedy` | #5E6558 | vedlejší text |

Pravidla:
- Kontrast drží dvojice tmavý les a světlý papír. Olivová je střední tón, nikdy podklad pod dlouhý text.
- Na stránce se střídají sekce na papíře s nejvýš dvěma až třemi plnými pásy. Dva pásy nikdy nejsou hned pod sebou.
- Stín má jen formulář přes hero a přilepená lišta.

## Písmo

Hanken Grotesk, jedna rodina, variabilní řez uložený lokálně (latin a latin-ext, OFL).

- H1 řez 400, proklad -0.048em. H2 řez 380, proklad -0.038em. H3 řez 460.
- Text 16 px, perex 17 až 19 px, řádkování 1,6.
- Žádné verzálky, žádné štítky nad nadpisy sekcí.

## Rozvržení a rozestupy

- Obsah má šířku 1280 px a boční odsazení `--p` (20 až 64 px). Všechno lícuje na jednu levou hranu, i obsah uvnitř pásů a hero.
- Hero a pásy jsou odsazené od okraje okna o `--ram` (8 až 16 px) a mají rádius 28 px.
- Mezera mezi sekcemi `--sekce` (96 až 152 px), pod nadpisem sekce `--hlava` (40 až 72 px).
- Rádiusy: 28 px pásy a hero, 18 px fotky, dlaždice a karty, 12 px drobné náhledy, pilulka pro tlačítka a štítky.

## Hero

Fotka přes celý úvodní blok, navigace leží na fotce, nadpis vlevo dole, perex a tlačítka vpravo. Na úvodu a v kontaktu přečnívá přes spodní hranu hero poptávkový formulář (`--prekryv`). Bez fotky je vidět olivový přechod, takže hero nikdy není prázdné. Prvky na fotce (hodnocení, kontakty, kotvy, počet fotek) jsou matné sklo (`.sklo`).

## Komponenty

| Třída | Co to je |
|---|---|
| `.pas`, `.pas--les`, `.pas--oliva` | plný pás přes šířku stránky, uvnitř vždy `.wrap` |
| `.tmave` | přidat na tmavý pás, přepne linky a vedlejší text na světlé varianty |
| `.wrap` | obsah na šířku stránky |
| `.sklo` | matné sklo na fotce |
| `.hlava` | hlavička sekce: nadpis vlevo, krátký text a odkaz vpravo |
| `.lista`, `.menu`, `.drobky` | navigace na fotce v hero |
| `.hero`, `.hero--pod`, `.hero--s-formularem`, `.hodnoceni` | úvodní blok s fotkou |
| `.poptavka` | formulář, který sestaví e-mail s poptávkou (bez serveru) |
| `.uvodni`, `.fakta` | úvodní sekce s čísly |
| `.mozaika`, `.dlazdice`, `--plna`, `--foto` | mřížka dlaždic |
| `.karty`, `.karta` | karty ubytování s fotkou, na mobilu posuvné |
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
