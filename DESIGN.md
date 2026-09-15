# Design systém webu Baumat Heroltice

Tenhle soubor je závazný pro všechny stránky. Živé ukázky všech komponent jsou na `styleguide.html`. Nová stránka se skládá jen z věcí popsaných tady. Když je potřeba něco nového, přidá se to nejdřív sem a do styleguidu, teprve potom na stránku.

## Principy

1. **Fotky prodávají místo.** Typografie a barvy jim dělají rámec, nekonkurují jim.
2. **Klid, ale ne šablona.** Většina sekcí je jednoduchá, jedno nebo dvě místa na stránce smí být výrazně asymetrická nebo editorial.
3. **Jeden hlavní akcent na sekci.** Maximálně jedno tlačítko a jeden proklik v hlavičce sekce.
4. **Jen ověřená fakta.** Žádné domyšlené kapacity, vzdálenosti ani ceny. Co není potvrzené od Baumatu, na web nejde.

## Značka

Značka je kruh se štítem chatky nad vlnou řeky (`#i-znacka` ve spritu). Odkazuje na chatky u Svratky.

- V hlavičce a patičce vždy se jménem: značka, „Baumat“ tučně, „Heroltice“ lehce.
- Značka se nikdy nedeformuje ani nebarví jinak, dědí barvu textu.
- V patičce je navíc jako velký jemný motiv (7 % krytí), jinde se opakovat nemá.
- Minimální velikost 24 px, pod ni je vlnka nečitelná.

## Fotky: barevné sjednocení

Fotky areálu vznikaly v různých ročních obdobích a na různé přístroje, takže vedle sebe skáčou z podzimní žluté do letní modré. Všechny obrázkové obaly proto mají třídu `foto`, která drží jednotnou korekci: mírná desaturace, vyšší kontrast a zelený soft-light nádech.

Prakticky: každý obal fotky (`hero__foto`, `karta__foto`, `detail__hlavni`, `areal__foto` a další) musí mít i třídu `foto`. Bez ní fotka vypadne z palety a je to hned vidět.

Až vznikne nové focení z jednoho dne, korekci je možné zeslabit nebo vypnout úpravou pravidla `.foto` v CSS.

## Barvy

| Token | Hex | Kde |
|---|---|---|
| `--les` | #2C4219 | tmavé panely, tlačítka, ikony, odkazy |
| `--krem` | #F5F0E3 | pozadí stránky, text na tmavém |
| `--uhel` | #16181A | hlavní text, nadpisy, ceny |
| `--uhel-jemny` | #5C6058 | perex, popisy, drobný text |
| `--pisek` | #E8E0C8 | podklad pod fotkou nebo mapou, než se načte |
| `--pisek-tmavy` | #D6CCAE | linky a rámečky na světlém |
| `--len-tlumeny` | #F1ECD6 | jemná zvýraznění: čísla u typů ubytování, částečně obsazené dny |
| `--oliva` | #A8B774 | drobné akcenty na tmavém: hvězdy u recenzí, ikona v hero |
| `--cihla` | #A9503C | obsazené termíny v kalendáři, nikdy jako dekorace |

Pravidla:
- Základ nese les, krém a uhel. Písek je na linky a podklady.
- Web nemá barevný akcent. Důraz nese velikost, váha písma a tmavá plocha, ne barva. Velká cena je krémová, ne barevná.
- Cihlová je vyhrazená pro obsazené termíny. Barva nese informaci, takže se nesmí použít jinde.
- Kontrast: malý text vždy uhel nebo uhel-jemny na krému, krém na lese.

## Světlo, stín a zrno

Web má jednu vlastní texturu: tmavě zelenou plochu prosvícenou olivovým světlem shora a ztmavenou zespodu, s jemným zrnem.

- Třída `svetlo` dává zelený světelný gradient, třída `zrno` přidá šum (16 % krytí, režim overlay).
- Používá se na uzavírací sekci (výzva) a nikde jinde. Tmavé panely uvnitř stránky zůstávají plnou barvou, jinak by web zošedivěl.
- Výzva jde přes celou šířku a navazuje přímo na tmavou patičku, takže stránka končí jedním tmavým blokem, ne dvěma.
- Nejsvětlejší místo gradientu má s krémovým textem kontrast 5 : 1, takže text zůstává čitelný. Při zesvětlení gradientu je nutné kontrast přepočítat.
- Hero má vlastní variantu: zrno přes fotku (12 %) a boční ztmavení, aby nadpis držel i na světlé fotce.

## Sklo (glass)

Jen na dvou místech:
- **fakta v hero** (boxy na fotce),
- **citace v panelu s fotkou** (recenze).

Nikde jinde. Sklo potřebuje fotku za sebou, na čisté ploše nemá smysl. Jemné rozostření pod fakty v hero není sklo, ale přechod bez hran a rámečku.

## Typografie

Jeden font: **Bricolage Grotesque** v normální šířce (soubor `assets/fonts/bricolage.woff2`, latin + latin-ext, OFL). Nezužovat přes `font-stretch`, působí to sportovně.

| Úroveň | Token | Velikost | Váha | Použití |
|---|---|---|---|---|
| H1 | `--fs-hero` | 38 až 108 px | 650 | jen v hero, jednou na stránce |
| H2 velký | `--fs-h2-velky` | 44 až 96 px | 650 | třída `h2-velky`, max jednou na stránce, hlavní prodejní argument |
| H2 | `--fs-h2` | 32 až 52 px | 650 | běžné nadpisy sekcí |
| H3 | `--fs-h3` | 22 až 28 px | 600 | názvy karet, dlaždic, řádků |
| Cena | `--fs-cena` | 26 až 32 px | 650 | ceny v kartách |
| Perex | `--fs-perex` | 17 až 19 px | 400 | úvod pod nadpisem, třída `perex` |
| Text | `--fs-text` | 17 px | 400 | běžný text |
| Malý | `--fs-maly` | 15 px | 400 | popisy v kartách a řádcích |
| Drobný | `--fs-drobny` | 14 px | 400 | metadata, jednotky u cen |

Pravidla:
- Nadpisy větou, žádné verzálky.
- H1 na dva řádky přes `<span>` bloky, nerozdělovat na malý štítek a velký název.
- Tlačítka a odkazy váha 600.

## Mezery

| Token | Velikost | Kdy |
|---|---|---|
| `--mezera-s` | 16 až 24 px | související prvky: mezery mezi kartami, dlaždicemi, fakty |
| `--mezera-m` | 32 až 52 px | nadpis sekce a její obsah |
| `--mezera-l` | 88 až 144 px | mezi sekcemi (třída `sekce`) |
| `--mezera-xl` | 120 až 224 px | jen před hlavním prodejním argumentem (třída `sekce sekce--xl`), max jednou na stránce |

## Patička

Patička je tmavá (`--uhel-zeleny` #17200F) a navazuje na uzavírací výzvu bez mezery. Stránka tak končí jedním tmavým blokem místo série světlých a tmavých pruhů.

## Rádiusy

Velikost rádiusu nese hierarchii, proto se nesmí sjednotit:

| Token | Velikost | Kde |
|---|---|---|
| `--r-panel` | 24 až 36 px | hero, tmavé panely, velké fotky |
| `--r-karta` | 14 px | karty, fotky v kartách |
| `--r-radek` | 16 px | řádky, poznámky |

## Mřížka

- Stránka max 1440 px, na širších monitorech se centruje.
- Obsah lícuje s textem uvnitř panelů (`--gutter` = `--inset` + `--pad`).
- `wrap` pro obsah, `panel` pro zaoblené bloky přes šířku (hero, tmavé panely).
- Breakpointy: 420, 640, 760, 900, 960 (menu), 1080 px.

## Komponenty

| Komponenta | Třídy | Použití | Pravidla |
|---|---|---|---|
| Tlačítko | `btn btn--les` / `btn--krem` / `btn--obrys` | hlavní akce (rezervace, termín) | les na světlém, krém na tmavém, obrys jako vedlejší na tmavém. Max jedno hlavní tlačítko v sekci |
| Proklik | `proklik` / `proklik--svetly` | odkaz na podstránku v hlavičce sekce | vždy s šipkou, při najetí se vyplní |
| Odkazový řádek | `odkazy` + `odkaz-radek` | rozcestník na existující stránky | řádky oddělené linkami. Při najetí se řádek jemně odsadí a vybarví se jen kolečko se šipkou, nikdy celý blok |
| Položka | `polozky` + `polozka` | výčet bez odkazů (pro koho je areál) | ikona, H3, jedna věta, řádky oddělené linkami |
| Karta vybavení | `vybaveni-mrizka` + `vybaveni-karta` | aktivity a vybavení | fotka, pod ní název a věta. Text nikdy přes fotku, aby byl čitelný i na mobilu |
| Kontaktní řádek | `kontakty` + `kontakt-radek` | telefony, e-maily | řádky oddělené linkami, šipka se objeví při najetí |
| Karta | `karty` + `karta` | ubytování | fotka 4:5, H3, jedna krátká věta, cena. Celá karta je odkaz. Žádné štítky na fotkách, žádné ikony u textu. Na mobilu vodorovný posun |
| Dlaždice | `dlazdice` / `dlazdice--velka` | fotka s popiskem přes spodní část | jen tam, kde je fotka dost tmavá. Na mobilu raději karta s textem pod fotkou |
| Fakta | `fakta` | krátká čísla (cena, kapacita, vzdálenost, hodnocení) | max 4 položky, jen na tmavém, každá ve vlastním skleněném boxu. Všechny stejné, žádný se nezvýrazňuje |
| Citace | `citace` | recenze | jen v panelu s fotkou, hvězdy jen se skutečným hodnocením |
| Přepínač jazyka | `jazyky` | hlavička | aktivní jazyk `aria-current="true"` |

## Typy sekcí

| Typ | Třídy | Příklad na homepage | Poznámka |
|---|---|---|---|
| Hero | `hero panel na-tmave` | úvod | fotka, H1, perex s dvěma tlačítky, fakta |
| Text s fotkou a rozcestníkem | `pro-koho` | pro oslavy, svatby... | text asi 42 %, fotka asi 58 % |
| Karty | `sekce__hlava` + `karty` | kde budete spát | hlavička s proklikem vpravo |
| Karty vybavení | `vybaveni-mrizka` | co v areálu najdete | 6 karet, fotka a text pod ní |
| Rozdělený panel | `sekce sekce--xl` + `areal` | celý areál | tmavá polovina s `h2-velky` a velkou cenou, fotka na plnou výšku vedle |
| Panel s fotkou a citacemi | `recenze panel panel--tmavy panel--sekce` | co píší hosté | fotka ztmavená přechodem |
| Kontakt a poloha | `kontakt` + `poloha` | naplánujte si pobyt | kontaktní řádky, fakta o poloze, mapa |

Rytmus stránky: střídat světlé sekce a tmavé plochy. Dvě tmavé plochy smí jít po sobě, jen když se vizuálně liší (plná barva a fotka) a odděluje je velká mezera. Na stránce max jeden `h2-velky`.

Podstránky nemají všechny stejnou stavbu. Ubytování je rozhodovací stránka, proto má přehled a číslované bloky s cenou. Aktivity jsou k prohlížení, proto je to mřížka karet, kde velké karty dostanou hlavní lákadla. Stejný blok se nikdy neopakuje víc než čtyřikrát za sebou.

Sekce nemají štítky ani nálepky nad nadpisem, nadpis stojí sám.

Hlavička je běžný pruh nad hero, ne plovoucí pilulka přes obsah. Jakmile ji scroll odsune z obrazovky, přilepí se zpátky nahoru ve skleněné variantě (`hlavicka--lepi`) a od obsahu ji odděluje měkký stín, ne linka. Aby stránka při přilepení neposkočila, JS pod ni vloží prvek stejné výšky.

Hero jde přes celou šířku okna, bez rádiusu a bez okrajů. Obsah uvnitř zůstává v mřížce stránky, takže lícuje se zbytkem webu. Na homepage zabírá celou první obrazovku, ale výška je omezená rozsahem 560 až 840 px, aby nebylo obří na velkém monitoru ani useknuté na nízkém. Na podstránkách je rozsah 420 až 600 px. Obě mají dvojitý gradient: svislý zespodu a vodorovný zleva. Bez toho se světlý nadpis ztrácí ve světlé fotce.

Na podstránkách se nepoužívá kotvová navigace pod hero. Kotvy v URL (`#apartman`) zůstávají, aby na ně šlo odkazovat z jiných stránek.

Nedělat odkazy na stránky, které neexistují. Samostatné stránky pro svatby, oslavy, tábory a firemní akce nebudou, tyhle okruhy jsou jen výčtem na homepage.

## Texty

- Nikdy dlouhou pomlčku. Místo ní čárka, dvojtečka nebo nová věta.
- Mezi číslem a jednotkou nezlomitelná mezera: `290&nbsp;Kč`, `25&nbsp;km`.
- Uvozovky české „takto“.
- Popis v kartě jedna krátká věta, bez tečky na konci, pokud nejde o celou větu.
- Ceny jsou na více stránkách (homepage, ubytování, ceník, EN). Při změně ceny projít všechny výskyty: `grep -rn "Kč" .`
- EN verze má stejná čísla jako CZ, nikdy starší.

## Fotky

- Hlavní fotky na šířku 1536 px, na výšku podle karty. Alt text popisuje místo, u dekorativních dlaždic prázdný `alt=""` (název je v nadpisu).
- Jedna fotka jen jednou na stránce.
- Dočasně se odkazují na starý WordPress, před vypnutím stáhnout do `assets/img/`.

## Přístupnost

- Každá sekce má `aria-labelledby` na svůj nadpis.
- Viditelný focus (`:focus-visible`), na tmavém krémový.
- Ikony `aria-hidden="true"`, smysl nese text.
- Pohyb respektuje `prefers-reduced-motion`.

## Komponenty podstránek

| Komponenta | Třídy | Použití |
|---|---|---|
| Hero podstránky | `hero hero--podstranka` | nižší hero bez faktů, jedno tlačítko |
| Kotvy | `kotvy` | odkazy na sekce v rámci stránky, hned pod hero |

| Parametry | `parametry` | seznam vlastností s ikonami, jen v detailu |
| Přehled | `prehled` | rychlé srovnání typů pod hero: náhled, název, kapacita a cena |
| Blok typu | `typ` / `typ--obraceny` | ubytování: číslo, název, cena, široká galerie, text s parametry |
| Karta aktivity | `aktivity` + `aktivita` / `aktivita--velka` | aktivity a zázemí: fotka, název, text, volitelná meta s cenou |
| Ceníkový řádek | `cenik-skupina` + `cenik` + `cenik-radek` | položka, popis a cena vpravo |
| Poznámka | `poznamka` | vysvětlivka pod obsahem, na pískovém podkladu |
| Osoba | `osoba` | správce areálu: fotka, role, jméno, kontakt |
| Karusel | `karusel` + `karusel__stopa` | sady karet, které se nevejdou vedle sebe | aktivní karta je plná a povystoupí, ostatní ustoupí do 58 % krytí. Ovládá se šipkami, tažením myší, prstem i kolečkem. Šipky a ukazatel se skryjí, když není co posouvat |
| Kalendář | `kalendar-blok` + `kalendar` | vlastní kalendář obsazenosti, data z `assets/data/obsazenost.json`. Mřížka vlevo, legenda a poznámka vpravo |
| Galerie s prohlížečem | `detail__galerie` + `data-galerie` | fotky v detailu | hlavní fotka, náhledy, klik otevře prohlížeč (šipky, Esc) |
| Výzva | `vyzva` | závěrečná sekce na konci každé podstránky |

Na tmavém panelu (`na-tmave`) mají kontakty, parametry, poznámka i kotvy automaticky světlou variantu.

## Sestavení stránek

Hlavička, patička, závěrečná výzva a sprite ikon jsou v `_sablony/`. Stránky se generují skriptem:

```
python3 build.py
```

Výstupní HTML se commituje do repa, takže GitHub Pages funguje bez buildu. Skript hlídá, že v HTML nezůstaly nevyplněné značky ani dlouhá pomlčka.

Značky v šablonách: `{{ROOT}}` cesta ke kořeni, `{{IMG}}` základ cesty k fotkám, `{{i:nazev}}` ikona, `{{stars}}` pět hvězd, `{{hlavicka}}`, `{{paticka}}`, `{{vyzva}}` vložené části. Novou stránku stačí přidat do `STRANKY` v `build.py`.

## Nová stránka: postup

1. Vytvořit `_sablony/<nazev>.html`, začít `{{hlavicka}}` a skončit `{{vyzva}}` a `{{paticka}}`.
2. Přidat stránku do `STRANKY` v `build.py` (výstup, hloubka, aktivní položka menu).
3. Hero a pod ním sekce jen z typů výše.
4. Zkontrolovat: jeden H1, max jeden `h2-velky`, max jedna `sekce--xl`, sklo jen v hlavičce a recenzích.
5. Přidat EN verzi se stejnými čísly a `hreflang`.
6. Spustit `python3 build.py` a otestovat na 390, 820, 1440 a 2560 px.
