# Zadání – nahrát „Japonsko" průvodce na GitHub

## Cíl
Nahrát hotovou HTML stránku (přehled uložených Instagram reelů z kolekce „Japonsko")
do repozitáře **github.com/mirekstrnad/japan** a zapnout GitHub Pages, aby běžela jako web.

Hlavní soubor k nahrání: **`japonsko_reels.html`** (kompletní, samostatná stránka – vše je v jednom souboru).

## Co je ve stránce
- Záložka **Plán podle měst**: nejlepší místa rozhozená do trasy (Tokio → Kjóto → Nara → Ósaka → výlety),
  přepínač „jen vybraná místa" / „všechny reely podle měst" a filtr podle kategorií.
- Záložka **Všechny reely**: všech 204 reelů s hodnocením, vyhledáváním a řazením.
- U každého reelu: kategorie, moje skóre (1–5), u ověřených míst reálné hodnocení (Google/Tabelog/Tripadvisor),
  odkaz na reel a odkaz na Google Maps.

## Postup (lokální Claude Code / terminál)
1. Naklonuj repo:
   `git clone https://github.com/mirekstrnad/japan.git && cd japan`
2. Zkopíruj `japonsko_reels.html` do složky repa a přejmenuj na `index.html`
   (aby se stránka otevírala jako web):
   `cp /cesta/k/japonsko_reels.html index.html`
3. Commit + push:
   `git add index.html && git commit -m "Add full Japan reels overview" && git push`
4. Zapni GitHub Pages: v repu **Settings → Pages → Source: Deploy from a branch → main / (root) → Save**.
5. Web poběží na: **https://mirekstrnad.github.io/japan/**

## Poznámka k proxy (proč to nešlo z cloudu)
Předchozí session běžela v Anthropic cloudu, kde „git proxy" pouští push jen do repozitářů
přidaných při startu session – proto plnou stránku (~200 KB) nešlo nahrát automaticky.
Lokálně (Claude Code v terminálu) tenhle problém není a `git push` funguje normálně.

## Kdyby bylo potřeba stránku znovu vygenerovat
Ve složce `zdroj/` jsou zdrojová data a build skripty:
- `japonsko.json` – vytažená kolekce (204 reelů: autor, url, hashtagy, popisek)
- `reels_rated.json` – obohacená data (kategorie, skóre, město, ověřená hodnocení, Google Maps dotaz)
- `template.html` – šablona stránky (obsahuje `__DATA__`, `__PLAN__`, `__COLORS__`, `__CATS__`)
- `enrich.py` → kategorie + skóre, `cities.py` → přiřazení měst, `maps.py` → odkazy na mapy
- `build_html2.py` → poskládá finální `japonsko_reels.html` ze šablony a dat

Build (pořadí): `python3 enrich.py && python3 cities.py && python3 maps.py && python3 build_html2.py`
(pozn.: `enrich.py`/`maps.py` čtou/píší `reels_rated.json`; kdyby data chyběla, začni z `japonsko.json`).

## Složka `web/`
Odlehčená verze, která už je nahraná v repu (malý `index.html`, co načítá data z `data/d0-d2.json`).
Pokud nahraješ plný `japonsko_reels.html` jako `index.html`, tuhle odlehčenou verzi můžeš přepsat.
