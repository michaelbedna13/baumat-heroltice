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


## Kalendář obsazenosti z Google Kalendáře

Kalendář na stránce Kontakt čte `assets/data/obsazenost.json`. Ten jednou za hodinu přepisuje GitHub Actions (`.github/workflows/kalendar.yml` spouští `scripts/kalendar.py`) podle Google Kalendáře správce. Na web se ukládají jen data a stav dne, žádné názvy událostí ani jména hostů.

Nastavení (jednou):
1. V Google Kalendáři správce: Nastavení, vybrat kalendář s rezervacemi, sekce „Integrace kalendáře“, zkopírovat **Tajnou adresu ve formátu iCal**.
2. V repu na GitHubu: Settings, Secrets and variables, Actions, **New repository secret**. Název `KALENDAR_ICAL_URL`, hodnota zkopírovaná adresa. Víc kalendářů jde zadat oddělených čárkou.
3. Záložka **Actions**: povolit workflow, pokud se ptá, otevřít „Kalendář obsazenosti“ a dát **Run workflow**. Za minutu by měl být v repu nový `obsazenost.json`.

Jak zapisovat do kalendáře:
- Pronájem celého areálu: název události obsahuje „celý areál“ (nebo „obsazeno“). Dny se zobrazí červeně jako obsazené.
- Jakákoli jiná rezervace: dny se zobrazí žlutě jako částečně obsazené.
- Počítají se noci: pobyt od 3. do 5. obsadí 3. a 4., odjezdový den zůstane volný.
- Zrušené události se ignorují.

Pozor: pokud v repu delší dobu (60 dní) nic neproběhne, GitHub automatické spouštění vypne a pošle o tom e-mail. Znovu se zapne jedním kliknutím v záložce Actions. Workflow sám jednou denně zapíše datum aktualizace, takže by k tomu nemělo docházet.

## Recenze

Recenze na úvodní stránce jsou vybrané z Google Maps a vložené napevno v `_sablony/index.html` a v anglickém překladu v `_sablony/en/index.html`. Novou recenzi přidáš zkopírováním jednoho bloku `<figure class="recenze__karta">` a úpravou jména, iniciál, roku a textu. Dlouhé recenze (nad 260 znaků) mají tlačítko „Celá recenze“.

Tlačítko „Napsat recenzi“ a QR kód vedou na https://g.page/r/CQ6p7-MQkw-UEAE/review. QR je obrázek `assets/img/qr-recenze.svg`, verze pro tisk je `assets/img/qr-recenze-tisk.png` (1480 × 1480 px).
