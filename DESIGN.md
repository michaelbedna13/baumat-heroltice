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
- Zelená je jediná akcentová barva. Výjimkou jsou zlaté hvězdičky u hodnocení a barvy stavů v kalendáři.
- Karty: bílé, tenký rámeček, rádius 16 px. Stín se objeví až po najetí myší.

## Mobil

- Hero nemá na mobilu pevnou výšku, je jen tak vysoké, kolik zabere obsah. Na desktopu nejvýš 74 % výšky okna (podstránky 48 %).
- Skupiny tlačítek (`.akce`) jsou pod 560 px přes celou šířku a pod sebou.
- Karty ubytování se na mobilu posouvají do strany.
- Karta ubytování je na mobilu zkrácená: jen hlavní fotka (ostatní jsou v prohlížeči), menší štítky, vybavení schované pod tlačítkem „Zobrazit vybavení" (`details`, na desktopu vždy rozbalené) a v boxu s cenou je částka s jednotkou na jednom řádku a pod nimi tlačítko přes celou šířku.

## Hodnocení

Hodnocení z Google je nejsilnější důkaz, proto má vlastní podobu: zlaté hvězdičky #F2A922 (poslední napůl, `.hvezdy`), v sekci recenzí bílá pilulka s velkým číslem 4,5 (`.souhrn`), v úvodním bloku řádek s hvězdičkami (`.hodnoceni-radek`) a v proužku s fakty plná zlatá hvězda. U jednotlivých recenzí hvězdičky nejsou, dokud neznáme jejich skutečné hodnocení. Po napojení Google API se doplní.

## Kalendář obsazenosti

Klasické barvy stavů, aby se daly přečíst na první pohled: volno světle zelená #E2F0DA, částečně obsazeno žluté šrafování (#FCE7B6 a #F7D993), obsazeno červená #D8453A. Minulé dny jsou šedé a zeslabené, dnešek má tmavý rámeček. Šrafování odliší částečnou obsazenost i bez barvy.

## Přepínač jazyka

Pilulka CZ / EN (`.jazyky`). Na fotce je sklo s bílou aktivní volbou, v přilepené liště šedá s bílou aktivní volbou (ne zelenou, aby se nebila se zeleným tlačítkem), na mobilu je v menu vedle tlačítka Volné termíny.

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
| `.logo`, `.logo__znak`, `.logo__misto` | logo Baumat (symbol `i-logo` ve spritu, jednobarevné, bez „spol. s r.o."); barvu bere z okolí, na fotce bílé, v přilepené liště tmavé |
| `.hero`, `.hero--pod`, `.hero--s-formularem`, `.hodnoceni` | úvodní blok s fotkou |
| `.fakta-pruh`, `.predstaveni` | proužek s fakty pod hero, úvodní blok fotka a text |
| `.vyhody` | čtyři body s ikonou v kruhu |
| `.mozaika`, `.dlazdice` | mřížka odkazových karet |
| `.karty`, `.karta` | bílé karty ubytování s fotkou nahoře |
| `.celek`, `.celek__cena` | pás s cenou celého areálu |
| `.ikony`, `.ikony--svetle` | seznam s linkovými ikonami |
| `.prehled` | tabulka typů ubytování s odkazy na kotvy |
| `.detail`, `.detail__galerie`, `.cipy`, `.detail__cena` | karta typu ubytování: galerie nahoře, vlevo název, štítky s hlavními údaji, popis a vybavení ve dvou sloupcích, vpravo box s cenou a tlačítkem |
| `.galerie`, `.parametry`, `.parametry--2` | galerie fotek, seznam vybavení s ikonami |
| `.polozky--karty` | bílé karty zázemí (kuchyně, kuchyňky, sociální zařízení) |
| `.aktivity`, `.aktivita`, `.aktivita--hlavni` | aktivity: bazén jako široká hlavní karta, ostatní v jednotné mřížce 3 sloupců |
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
