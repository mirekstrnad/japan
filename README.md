# Japonsko – plán cesty & přehled uložených IG reelů

Interaktivní průvodce postavený z Instagram kolekce „Japonsko" (204 reelů).

**Web: https://mirekstrnad.github.io/japan/**

## Co stránka umí
- **Plán podle měst** – nejlepší místa rozhozená do trasy (Tokio → Kjóto → Nara → Ósaka → výlety),
  přepínač „jen vybraná místa" / „všechny reely podle měst", filtr podle kategorií.
- **Všechny reely** – všech 204 reelů s hodnocením, vyhledáváním a řazením.
- U každého reelu: kategorie, skóre 1–5, u ověřených míst reálné hodnocení (Google / Tabelog / Tripadvisor),
  odkaz na reel a odkaz na Google Maps.

## Struktura repa
| cesta | co to je |
|---|---|
| `index.html` | hlavní stránka – kompletní a samostatná, žádné externí závislosti |
| `zdroj/` | zdrojová data a build skripty pro znovuvygenerování |
| `data/` | pozůstatek starší odlehčené verze stránky, dnes se nepoužívá |
| `ZADANI.md` | původní zadání / postup |

## Znovuvygenerování stránky
```bash
cd zdroj
python3 enrich.py && python3 cities.py && python3 maps.py && python3 build_html2.py
cp japonsko_reels.html ../index.html
```

- `japonsko.json` – vytažená kolekce (autor, url, hashtagy, popisek)
- `reels_rated.json` – obohacená data (kategorie, skóre, město, ověřená hodnocení, odkaz na mapy)
- `template.html` – šablona (placeholdery `__DATA__`, `__PLAN__`, `__COLORS__`, `__CATS__`)
- `enrich.py` → kategorie + skóre · `cities.py` → města · `maps.py` → odkazy na mapy · `build_html2.py` → finální HTML

Skripty pracují s cestami relativně ke složce `zdroj/`, takže je lze spustit odkudkoliv.
