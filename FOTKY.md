# Fotky a logo

Všechny obrázky patří do složky `assets/img/` a **název souboru musí přesně sedět** na první sloupec tabulky, včetně malých písmen a pomlček. Bez diakritiky, bez mezer.

## Formát a velikost

- **Formát:** JPG (fotky) nebo WEBP, pokud ho umíš vyexportovat. WEBP je zhruba o třetinu menší při stejné kvalitě. Pokud použiješ WEBP, přepiš příponu v `build.py` (funkce `foto`).
- **Šířka:** 1920 px u fotek na šířku, 1400 px u fotek na výšku. Větší nemá smysl, jen zpomalují web.
- **Kvalita:** JPG kolem 80 %. Cílová velikost souboru do 400 kB, ideálně do 250 kB.
- **Barevný profil:** sRGB. Fotky z iPhonu bývají v Display P3 a v prohlížeči pak vypadají přesycené.
- **Bez vodoznaků a bez rámečků.**

## Jak je nasadit

1. Nahraj fotky do `assets/img/`.
2. V `build.py` nastav `VLASTNI_FOTKY = True`.
3. Spusť `python3 build.py`.

Do té doby se berou fotky ze starého WordPressu, takže web funguje, ale po jeho vypnutí by fotky zmizely.

## Seznam fotek

Poměr stran je doporučení, ne povinnost. Fotka se vždy ořízne na střed, takže hlavní motiv patří doprostřed.

| Soubor | Co má být na fotce | Kde se zobrazí | Doporučený poměr |
|---|---|---|---|
| `hero-areal.jpg` | Hlavní fotka úvodní stránky, celkový pohled na areál | homepage hero | 16:9 na šířku |
| `hero-ubytovani.jpg` | Úvodní fotka stránky Ubytování | ubytovani hero | 16:9 na šířku |
| `hero-aktivity.jpg` | Úvodní fotka stránky Aktivity | aktivity hero | 16:9 na šířku |
| `hero-cenik.jpg` | Úvodní fotka stránky Ceník | cenik hero | 16:9 na šířku |
| `hero-kontakt.jpg` | Úvodní fotka stránky Kontakt | kontakt hero | 16:9 na šířku |
| `pro-koho.jpg` | Fotka u sekce Pro oslavy, svatby, tábory i firmy | homepage | 3:4 na výšku |
| `cely-areal.jpg` | Pozadí sekce Celý areál jen pro vaši skupinu | homepage | 16:9 na šířku |
| `recenze-pozadi.jpg` | Pozadí sekce Co píší hosté | homepage | 16:9 na šířku |
| `apartman-1.jpg` | Apartmán zvenku, hlavní fotka | ubytovani, homepage | 3:2 na šířku |
| `apartman-2.jpg` | Pokoj v apartmánu | ubytovani | 3:2 na šířku |
| `apartman-3.jpg` | Kuchyně v apartmánu | ubytovani | 3:2 na šířku |
| `apartman-karta.jpg` | Apartmán na výšku do karty na homepage | homepage | 4:5 na výšku |
| `slusovice-1.jpg` | Buňky Slušovice zvenku | ubytovani, homepage | 3:2 na šířku |
| `slusovice-2.jpg` | Interiér buňky | ubytovani | 3:2 na šířku |
| `slusovice-3.jpg` | Sociální zařízení u buněk | ubytovani | 3:2 na šířku |
| `slusovice-karta.jpg` | Buňky na výšku do karty na homepage | homepage | 4:5 na výšku |
| `chatky-1.jpg` | Řada chatek na louce | ubytovani | 3:2 na šířku |
| `chatky-2.jpg` | Chatka zvenku | ubytovani | 3:2 na šířku |
| `chatky-3.jpg` | Interiér chatky | ubytovani | 3:2 na šířku |
| `chatky-karta.jpg` | Chatky na výšku do karty na homepage | homepage | 4:5 na výšku |
| `brana-1.jpg` | Chatky u hlavní brány zvenku | ubytovani, homepage | 3:2 na šířku |
| `brana-2.jpg` | Pokoj v chatce u hlavní brány | ubytovani | 3:2 na šířku |
| `brana-3.jpg` | Vybavení pokoje | ubytovani | 3:2 na šířku |
| `kuchyne-1.jpg` | Profesionální kuchyně | ubytovani | 3:2 na šířku |
| `kuchyne-2.jpg` | Jídelna se stoly | ubytovani | 3:2 na šířku |
| `kuchyne-3.jpg` | Vybavení kuchyně | ubytovani | 3:2 na šířku |
| `kuchynka-1.jpg` | Kuchyňka pro menší skupiny | ubytovani | 3:2 na šířku |
| `kuchynka-2.jpg` | Posezení v kuchyňce | ubytovani | 3:2 na šířku |
| `kuchynka-3.jpg` | Vybavení kuchyňky | ubytovani | 3:2 na šířku |
| `socialky-1.jpg` | Hlavní sociální zařízení zvenku | ubytovani | 3:2 na šířku |
| `socialky-2.jpg` | Sprchy | ubytovani | 3:2 na šířku |
| `socialky-3.jpg` | Umyvadla | ubytovani | 3:2 na šířku |
| `bazen-1.jpg` | Bazén, hlavní fotka | aktivity, homepage | 3:2 na šířku |
| `bazen-2.jpg` | Posezení u bazénu | aktivity | 3:2 na šířku |
| `bazen-3.jpg` | Bazén s okolní přírodou | aktivity | 3:2 na šířku |
| `tenis-1.jpg` | Tenisový kurt | aktivity, homepage | 3:2 na šířku |
| `tenis-2.jpg` | Tenisový kurt z druhé strany | aktivity | 3:2 na šířku |
| `beach-1.jpg` | Hřiště na beach volejbal | aktivity, homepage | 3:2 na šířku |
| `beach-2.jpg` | Písečné hřiště | aktivity | 3:2 na šířku |
| `stolni-tenis.jpg` | Pingpongový stůl | aktivity | 3:2 na šířku |
| `ohniste-1.jpg` | Ohniště s posezením | aktivity, homepage | 3:2 na šířku |
| `ohniste-2.jpg` | Ohniště zblízka | aktivity | 3:2 na šířku |
| `ohniste-3.jpg` | Večerní posezení u ohně | aktivity | 3:2 na šířku |
| `hriste-1.jpg` | Dětské hřiště | aktivity, homepage | 3:2 na šířku |
| `hriste-2.jpg` | Prolézačka | aktivity | 3:2 na šířku |
| `klubovna-1.jpg` | Klubovna s kulečníkem a krbem | aktivity, homepage | 3:2 na šířku |
| `klubovna-2.jpg` | Posezení v klubovně | aktivity | 3:2 na šířku |
| `spravce.jpg` | Portrét správce areálu Josefa Kavalce | kontakt | 1:1 čtverec |

## Logo

- **Nejlepší formát: SVG.** Je ostré v každé velikosti a dá se obarvit přes CSS, takže v tmavé patičce bude krémové a v hlavičce tmavé automaticky.
- Ulož jako `assets/img/logo.svg` (samotná značka, čtvercová, na mřížce 48 × 48) a případně `assets/img/logo-plne.svg` (značka se jménem).
- Značka nesmí mít pevně zapsanou barvu, ideálně `fill="currentColor"` nebo `stroke="currentColor"`.
- **Když SVG nemáš:** PNG s průhledným pozadím, značka 512 × 512 px, logo se jménem výška aspoň 240 px. JPG ne, nemá průhlednost.
- Po nahrání stačí vyměnit symbol `i-znacka` v `_sablony/ikony.svg` nebo v šabloně použít `<img>` místo SVG.

## Favicon

- `favicon.svg` (32 × 32) a `apple-touch-icon.png` (180 × 180, může mít plné pozadí).
