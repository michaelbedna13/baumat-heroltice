# Design systém webu Baumat Heroltice

Závazné pro všechny stránky. Živé ukázky komponent jsou na `styleguide.html`.

Stylopis `assets/css/style.css` je psaný **mobile-first**: základní pravidla platí pro telefon, `@media (min-width: …)` přidává větší obrazovky. Nikdy se nepíše opačně, jinak se pravidla začnou přebíjet.

## Principy

1. **Fotky prodávají místo.** Typografie a barvy jim dělají rámec.
2. **Jedna škála rozestupů.** Všechno jsou násobky osmi, nic se netrefuje „od oka".
3. **Jeden důraz na sekci.** Max jedno plné tlačítko a jeden proklik.
4. **Jen ověřená fakta.** Co není potvrzené od Baumatu, na web nejde.

## Písmo

| Font | Kde | Řezy |
|---|---|---|
| **Playfair Display** | H1 až H3, ceny, čísla ve faktech, logo | 400 až 700, kurzíva pro první řádek hero |
| **Poppins** | text, perex, tlačítka, navigace, popisky | 400, 500, 600 |

Nikdy naopak. Oba jsou v repu (`assets/fonts/`), nic se netahá z Googlu.

### Velikosti

| Token | Rozsah | Kde |
|---|---|---|
| `--fs-hero` | 38 až 104 px | H1 v hero |
| `--fs-h2-velky` | 32 až 68 px | závěrečná výzva, hlavní argument |
| `--fs-h2` | 27 až 44 px | nadpisy sekcí |
| `--fs-h3` | 19 až 25 px | karty, řádky, dlaždice |
| `--fs-cena` | 23 až 29 px | ceny v kartách |
| `--fs-perex` | 16 až 18 px | úvodní odstavec |
| `--fs-text` | 16 px | běžný text |
| `--fs-maly` | 14 px | popisky v kartách |
| `--fs-drobny` | 13 px | metadata, jednotky |

## Barvy

| Token | Hex | Kde |
|---|---|---|
| `--tma` | #022E21 | hero, tmavé panely, plná tlačítka |
| `--tma-hluboka` | #011C15 | konec závěru, pozadí za stránkou |
| `--les` | #0C4433 | hover plných tlačítek |
| `--krem` | #F3EFE6 | pozadí stránky, text na tmavém |
| `--papir` | #EBE5D8 | podklad střídaných sekcí (`pruh`), kalendář |
| `--pisek` | #E2DCCB | podklad pod fotkou, než se načte |
| `--uhel` | #12211B | hlavní text |
| `--uhel-jemny` | #5A6660 | perex a popisky |
| `--mata` | #9FCBB4 | akcent jen na tmavém (hvězdy, ikony) |
| `--cihla` | #A9503C | obsazené termíny v kalendáři, nikde jinde |

Web nemá barevný akcent na světlém pozadí. Důraz nese velikost, váha a tmavá plocha.

## Rozestupy

Jediná škála, násobky osmi: `--s-1` (8) až `--s-8` (64).

Rytmus stránky řídí čtyři tokeny:

| Token | Rozsah | Kdy |
|---|---|---|
| `--sekce-y` | 64 až 120 px | mezi sekcemi, třída `sekce` |
| `--sekce-y-velka` | 96 až 176 px | před hlavním argumentem a před závěrem, třída `sekce--xl` |
| `--hlava-mezera` | 32 až 56 px | mezi nadpisem sekce a jejím obsahem |
| `--mrizka-mezera` | 16 až 28 px | mezi kartami v mřížce |

Nic jiného se pro odsazení sekcí nepoužívá. Když někde chybí vzduch, upraví se token, ne jednotlivé místo.

## Rádiusy

| Token | Velikost | Kde |
|---|---|---|
| `--r-panel` | 24 až 32 px | velké panely |
| `--r-karta` | 16 px | karty a fotky |
| `--r-radek` | 12 px | vnitřní prvky karet, poznámky |
| `--r-drobny` | 8 px | nejmenší prvky, dny v kalendáři |

Vnitřní prvek má vždy menší rádius než obal, jinak roh vypadá nevyvážený.

## Mřížka a body zlomu

- Obsah max 1360 px, odsazení od kraje `--pad` (20 px na mobilu, 32 na tabletu, 48 na desktopu).
- Body zlomu: **620** (dva sloupce karet), **700** (větší odsazení), **900** (dvousloupcové sekce), **1080** (desktopová navigace, čtyři sloupce).

## Komponenty

| Komponenta | Třídy | Pravidla |
|---|---|---|
| Tlačítko | `btn` + `btn--les` / `btn--obrys-tmavy` / `btn--krem` / `btn--obrys` | na světlém plné tmavé a obrysové tmavé, na tmavém plné krémové a obrysové světlé |
| Tlačítko se šipkou | `btn--sipka` + `btn__kolecko` | jen pro hlavní akci v hero a ve skleněné kartě |
| Proklik | `proklik` / `proklik--svetly` | textový odkaz se šipkou, nikdy nevypadá jako tlačítko |
| Výčet | `polozky` + `polozka` | ikona, název, věta. Bez odkazu |
| Odkazový řádek | `odkazy` + `odkaz-radek` | při najetí se řádek odsadí a vybarví jen kolečko se šipkou |
| Kontaktní řádek | `kontakty` + `kontakt-radek` | šipka se objeví při najetí, na dotykových zařízeních je vidět vždy |
| Karta ubytování | `karty` + `karta` | fotka, název, věta, cena. Celá je odkaz |
| Karta vybavení | `vybaveni-mrizka` + `vybaveni-karta` | text vždy pod fotkou, ne přes ni |
| Karta aktivity | `aktivity` + `aktivita` / `aktivita--velka` | meta s cenou sedí na spodní hraně karty |
| Karusel | `karusel` + `karusel__stopa` | aktivní karta plná, ostatní na 55 % (jen od 1080 px). Ovládá se šipkami, tažením, prstem i klávesnicí |
| Citace | `citace` | skleněná karta, jen na panelu s fotkou |
| Fakta | `fakta` | max 4 položky, jen v hero |
| Kalendář | `kalendar-blok` | pískový panel, mřížka vlevo, legenda a poznámka vpravo |

## Typy sekcí

| Typ | Třídy | Kde |
|---|---|---|
| Hero | `hero` (+ `hero--podstranka`) | přes celou šířku okna, překryv je samostatná vrstva `hero__prekryv` |
| Běžná sekce | `sekce` + `wrap` | většina obsahu |
| Pruh | `pruh` | sekce na pískovém podkladu s měkkým náběhem, max jedna na stránku |
| Tmavý panel | `panel panel--tmavy panel--sekce` | recenze |
| Skleněná karta přes fotku | `areal` + `areal__karta` | hlavní prodejní argument |
| Závěr | `zaver` | výzva a patička v jednom tmavém bloku |

Rytmus: hero (tmavé) → krémová → pruh → krémová → tmavý panel → krémová → závěr.

## Sklo

Čtyři vrstvy: přechod bílé 6 až 18 %, obrys 1 px, vnitřní světlo nahoře, rozostření 18 až 22 px. Používá se na skleněnou kartu v sekci „Celý areál", citace recenzí a hlavičku po odscrollování. Nikdy na čistém krémovém pozadí.

## Světlo a zrno

Závěr stránky a panel správce mají zelený světelný gradient a zrno (`svetlo`, `zrno`, 20 % krytí). Jinde ne, jinak by web zošedivěl.

## Texty

- Nikdy dlouhou pomlčku.
- Nezlomitelná mezera mezi číslem a jednotkou: `290&nbsp;Kč`, `25&nbsp;km`.
- České uvozovky „takto".
- Ceny jsou na více stránkách. Při změně projít všechny výskyty: `grep -rn "Kč" _sablony/`.

## Fotky

Pojmenování, formáty a seznam jsou ve `FOTKY.md`. Každý obrázkový obal má třídu `foto`, která drží jednotnou barevnou korekci.

## Přístupnost

- Každá sekce má `aria-labelledby` na svůj nadpis.
- Viditelný focus, na tmavém krémový.
- Ikony `aria-hidden="true"`, smysl nese text.
- Pohyb respektuje `prefers-reduced-motion`.

## Nová stránka

1. Vytvořit `_sablony/<nazev>.html`, začít `{{hlavicka}}`, skončit `{{vyzva}}` a `{{paticka}}`.
2. Přidat do `STRANKY` v `build.py`.
3. Skládat jen z typů sekcí výše.
4. Zkontrolovat: jeden H1, max jeden `h2-velky`, max jedna `sekce--xl`, max jeden `pruh`.
5. Spustit `python3 build.py` a otestovat na 390, 768, 1440 a 2560 px.
