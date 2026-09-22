# Soubory ze starého webu

Fotky, dokumenty a favicona se zatím načítají ze starého webu (baumatheroltice.cz/wp-content/uploads/). Než starý web vypneš, je potřeba je přesunout sem do repa. Jinak na novém webu zmizí.

## Postup

1. Stáhni soubory ze seznamu níže. Nejrychlejší je stáhnout přes FTP nebo správce souborů na hostingu celé složky `wp-content/uploads/2024/11`, `2024/12`, `2025/04` a `2026/01` a vybrat z nich tyto soubory. Jde to i po jednom přes odkazy v tabulkách.
2. **Názvy nech přesně tak, jak jsou**, včetně velkých a malých písmen. GitHub Pages je rozlišuje, takže `Bazen_3.jpg` a `bazen_3.jpg` jsou dva různé soubory.
3. Obrázky nahraj do `assets/img/`, dokumenty do `assets/docs/`.
4. V `build.py` přepni `MISTNI_SOUBORY = True` a spusť `python3 build.py`. Když nějaký soubor chybí, build to vypíše a stránky neuloží.

## Obrázky do assets/img/ (42 souborů)

| Soubor | Kde je na starém webu |
|---|---|
| `Apartman_3-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Apartman_3-1536x1024.jpg |
| `Apartman_4-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Apartman_4-1536x1024.jpg |
| `Apartman_hl-foto-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Apartman_hl-foto-1536x1024.jpg |
| `Bazen_2-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Bazen_2-1536x1024.jpg |
| `Bazen_3-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Bazen_3-1536x1024.jpg |
| `Bazen_mainpage.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Bazen_mainpage.jpg |
| `Beach-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Beach-1536x1024.jpg |
| `Bunky-slusovice_2-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Bunky-slusovice_2-1536x1024.jpg |
| `Bunky-slusovice_hl-foto-1-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Bunky-slusovice_hl-foto-1-1536x1024.jpg |
| `Chatky_2-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Chatky_2-1536x1024.jpg |
| `Chatky_3-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Chatky_3-1536x1024.jpg |
| `Chatky_hl-foto-1-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Chatky_hl-foto-1-1536x1024.jpg |
| `Detske-hriste-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Detske-hriste-1536x1024.jpg |
| `Detske-hriste_2-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Detske-hriste_2-1536x1024.jpg |
| `Hl.socialky_1-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Hl.socialky_1-1536x1024.jpg |
| `Hl.socialky_2-1-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Hl.socialky_2-1-1536x1024.jpg |
| `Hl.socialky_3-1-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Hl.socialky_3-1-1536x1024.jpg |
| `Josef-Kavalec_spravce.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Josef-Kavalec_spravce.jpg |
| `Kuchyne-a-jidelna_1-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Kuchyne-a-jidelna_1-1536x1024.jpg |
| `Kuchyne-a-jidelna_2-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Kuchyne-a-jidelna_2-1536x1024.jpg |
| `Kuchyne-a-jidelna_3-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Kuchyne-a-jidelna_3-1536x1024.jpg |
| `Ohniste_1-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Ohniste_1-1536x1024.jpg |
| `Ohniste_2-1-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Ohniste_2-1-1536x1024.jpg |
| `Ohniste_3-1-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Ohniste_3-1-1536x1024.jpg |
| `Slusovice_socialn-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/Slusovice_socialn-1536x1024.jpg |
| `apartman_na-vysku.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/apartman_na-vysku.jpg |
| `areal-1.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/areal-1.jpg |
| `areal-2.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/areal-2.jpg |
| `beach_hl.photo_-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/beach_hl.photo_-1536x1024.jpg |
| `chatky-u-hl-brany-_2-1-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/chatky-u-hl-brany-_2-1-1536x1024.jpg |
| `chatky-u-hl-brany-_3-1-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/chatky-u-hl-brany-_3-1-1536x1024.jpg |
| `chatky-u-hl-brany-_hl-foto-1-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/chatky-u-hl-brany-_hl-foto-1-1536x1024.jpg |
| `chatky_na-vysku.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/chatky_na-vysku.jpg |
| `klubovna_2-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/klubovna_2-1536x1024.jpg |
| `klubovna_hl.photo_-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/klubovna_hl.photo_-1536x1024.jpg |
| `kuchynka_2-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/kuchynka_2-1536x1024.jpg |
| `kuchynka_3-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/kuchynka_3-1536x1024.jpg |
| `kuchynka_hl.photo_-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/kuchynka_hl.photo_-1536x1024.jpg |
| `ping-pong-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/ping-pong-1536x1024.jpg |
| `slusovice_na-vysku.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/slusovice_na-vysku.jpg |
| `tenis-2-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/12/tenis-2-1536x1024.jpg |
| `tenis_hl.photo_-1536x1024.jpg` | https://baumatheroltice.cz/wp-content/uploads/2024/11/tenis_hl.photo_-1536x1024.jpg |

## Dokumenty do assets/docs/ (3 soubory)

| Soubor | Kde je na starém webu |
|---|---|
| `Cenik-2026.pdf` | https://baumatheroltice.cz/wp-content/uploads/2026/01/Cenik-2026.pdf |
| `Provozni-rad-bazenu-FINAL-2023.docx` | https://baumatheroltice.cz/wp-content/uploads/2025/04/Provozni-rad-bazenu-FINAL-2023.docx |
| `Ubytovaci-rad-2026.docx` | https://baumatheroltice.cz/wp-content/uploads/2026/01/Ubytovaci-rad-2026.docx |

## Formát

**Fotky: WebP, nebo JPG.** Build bere obojí. Když v `assets/img/` najde `Apartman_3-1536x1024.webp`, použije ho místo `.jpg`. Název před tečkou musí zůstat stejný.

- WebP je zhruba o třetinu menší než JPG při stejné kvalitě a web se načte rychleji. Doporučuju ho, pokud fotky stejně upravuješ a exportuješ.
- Kvalita kolem 80 %, šířka kolem 2000 px, hlavní fotka `areal-1` 2400 px. Jedna fotka ideálně do 300 kB.
- Když fotky jen stáhneš ze starého webu a nic s nimi neděláš, nech je klidně jako JPG.

**Logo a favicona už jsou hotové** v `assets/img/`:
- `baumat-logo.svg` barevné logo, `baumat-logo-bez-sro.svg` bez „spol. s r.o."
- `baumat-logo-jednobarevne.svg` a `baumat-logo-jednobarevne-bez-sro.svg` jednobarevná verze, barvu přebírá z okolního textu (`currentColor`)
- `favicon.svg` a `apple-touch-icon.png` (180 × 180 px), zapojené v hlavičce všech stránek
