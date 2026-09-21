# Design webu Baumat Heroltice

Koncept v2 „olivové panely". Obsah leží v zaoblených panelech na kamenném podkladu, mezi panely je vždy stejná mezera. Fotky jsou vidět, ale vždy v rámu vedle textu, nikdy přes celou šířku okna.

## Barvy

| Token | Hex | Použití |
|---|---|---|
| `--oliva` | #55613F | úvodní panel s navigací, pás aktivit, plná dlaždice, hlavní tlačítko na světlé ploše |
| `--oliva-tmava` | #434D31 | hover olivových prvků |
| `--mech` | #2B3222 | text, patička |
| `--hlina` | #3F3225 | jediný hnědý panel na stránce (celý areál, správce), obsazené dny v kalendáři |
| `--krem` | #F6F2E7 | světlé panely, tlačítka na tmavé |
| `--kamen` | #E3E2D7 | podklad stránky, mezery mezi panely |
| `--sedy` | #676C5B | vedlejší text na světlé ploše |
| `--foto` | #C8CBB8 | plocha pod fotkou, než se načte |

Pravidla:
- Na jedné stránce nejvýš jeden hnědý panel.
- Žádná další akcentová barva. Důraz nese velikost písma a tmavá plocha.
- Stíny se nepoužívají, jedinou výjimkou je přilepená lišta při scrollování.

## Písmo

Hanken Grotesk, jedna rodina, variabilní řez uložený lokálně v `assets/fonts/` (latin a latin-ext, licence OFL).

- Nadpisy H1 a H2: řez 300, těsný proklad (-0.035em), velké velikosti. Tohle je hlavní výrazový prvek webu.
- H3: řez 400.
- Text 16 px, řez 400, řádkování 1,6. Důraz 500, tučně 600.
- Žádné verzálky, žádné štítky nad nadpisy sekcí.

## Tvar a rozestupy

- Panely: rádius 26 px. Fotky: 16 px. Pole formuláře: 14 px. Tlačítka, štítky a kotvy: pilulka.
- Vnitřní odsazení panelu `--vnitrek` (20 až 64 px), mezera mezi panely `--okraj` (8 až 14 px).
- Maximální šířka stránky 1360 px.

## Rytmus stránky

1. Úvodní olivový panel: lišta, pravítko (vlevo místo nebo drobečková navigace, vpravo vzdálenost), nadpis, fotka, případně poptávkový formulář.
2. Pod ním se střídají krémové panely, holé sekce na kamenném podkladu (mozaika dlaždic), jeden olivový a jeden hnědý panel.
3. Stránka vždy končí tmavou patičkou s výzvou „Je váš termín volný?".

## Komponenty

| Třída | Co to je |
|---|---|
| `.panel` + `--krem`, `--oliva`, `--mech`, `--hlina`, `--holy` | základní blok obsahu |
| `.svetly` | přidat na tmavý panel, přepne linky a vedlejší text na světlé varianty |
| `.hlava` | hlavička sekce: nadpis vlevo, krátký text a odkaz vpravo |
| `.split`, `.split--pul`, `.split--obracene` | dva bloky vedle sebe |
| `.lista`, `.menu`, `.pravitko`, `.drobky` | navigace v úvodním panelu |
| `.hero`, `.hero--pod`, `.hodnoceni`, `.uvod-karta` | obsah úvodního panelu |
| `.poptavka` | formulář, který sestaví e-mail s poptávkou (bez serveru) |
| `.vodici`, `.ctvrtiny`, `.fakta` | panel se svislými vodicími linkami a čísly |
| `.mozaika`, `.dlazdice`, `--plna`, `--foto` | mřížka dlaždic |
| `.karty`, `.karta` | karty ubytování s fotkou, na mobilu posuvné |
| `.celek`, `.celek__cena` | blok s cenou celého areálu |
| `.ikony` | seznam s linkovými ikonami na olivové |
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
