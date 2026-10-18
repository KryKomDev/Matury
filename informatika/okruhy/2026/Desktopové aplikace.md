# Desktopové aplikace

## Osnova

* Definice a vlastnosti
* Třívrstvá architektura
* Typy desktopových aplikací
* Příklady
* Vývoj desktopových aplikací
* Výhody a nevýhody
* Porovnání s webovými aplikacemi
* Multiplatformní aplikace
* Aktualizace desktopových aplikací
* Bezpečnost

## Definice a vlastnosti

* **Desktopové aplikace** – programy, které se instalují a spouštějí přímo na konkrétním počítači uživatele.
* **Běh přímo v OS** – aplikace běží v prostředí operačního systému, který jim zajišťuje přístup k paměti, komunikaci s hardwarem a spouštění procesů.
* **Využití lokálního výkonu** – aplikace přímo využívají hardwarové prostředky počítače (CPU, RAM, GPU).
* **Lokální práce s daty** – pracují primárně s daty uloženými na lokálním disku počítače.
* **Grafické uživatelské rozhraní (GUI)** – obsahují okna, tlačítka, menu a další prvky, což je uživatelsky přívětivější než textové rozhraní příkazové řádky.
* **Offline fungování** – většinou nevyžadují neustálé připojení k internetu pro svou základní funkčnost.

### Třívrstvá architektura aplikace
Rozdělení na samostatné vrstvy zlepšuje přehlednost kódu, usnadňuje údržbu a umožňuje snadnější budoucí úpravy aplikace:
* **Uživatelské rozhraní (prezentační vrstva)** – zajišťuje komunikaci s uživatelem (okna, tlačítka, menu, grafické prvky).
* **Logika aplikace (aplikační vrstva)** – provádí výpočty, logické operace, zpracování dat a řídí chování aplikace.
* **Datová vrstva** – stará se o ukládání a načítání dat (např. do lokálních souborů nebo databáze).

## Typy desktopových aplikací

* **Kancelářské** – práce s dokumenty (psaní textů, tabulkové výpočty, prezentace).
* **Grafické** – úprava a tvorba rastrové i vektorové grafiky, střih videa a 3D modelování.
* **Vývojové** – nástroje pro programování (IDE, textové editory kódu, kompilátory).
* **Multimediální** – přehrávače hudby, videí a prohlížeče obrázků.
* **Specializované** – účetní a podnikové systémy, hry, CAD nástroje atd.

## Příklady

* **Microsoft Word** – textový editor.
* **Microsoft Excel** – tabulkový procesor.
* **Adobe Photoshop** – rastrový grafický editor.
* **Blender** – open-source nástroj pro tvorbu 3D grafiky a animací.
* **Visual Studio** – integrované vývojové prostředí (IDE) pro vývoj aplikací.

## Vývoj desktopových aplikací

* **Programovací jazyky** – nejčastěji C#, Java, C++, Python apod.
* **Frameworky** – usnadňují vývoj a návrh uživatelského rozhraní (např. .NET, WPF, JavaFX, Qt).

### Životní cyklus vývoje
1. **Návrh** – specifikace toho, co má aplikace dělat, kdo ji bude používat, jak bude vypadat (návrh GUI) a jaká bude její vnitřní struktura.
2. **Vývoj** – psaní samotného zdrojového kódu, implementace funkcí a propojování jednotlivých vrstev.
3. **Testování** – kontrola správné funkčnosti, ladění chyb, testování výkonu a stability.
4. **Instalace/nasazení** – vytvoření instalátoru a předání aplikace koncovým uživatelům.

## Výhody a nevýhody

### Výhody
* **Vysoký výkon** – přímé využití lokálního hardwaru.
* **Práce offline** – nezávislost na internetovém připojení.
* **Přímý přístup k hardwaru** – snadný přístup k USB portům, tiskárnám, GPU apod.
* **Stabilita** – chod aplikace není ovlivněn výpadky vzdáleného serveru.

### Nevýhody
* **Nutnost instalace** – aplikace se musí před použitím stáhnout a nainstalovat do systému.
* **Závislost na OS** – aplikace napsaná pro Windows obvykle neběží přímo na macOS bez úprav.
* **Správa aktualizací** – aktualizace musí provádět uživatel (nebo běžet na pozadí na lokálním stroji).
* **Horší dostupnost** – omezení na konkrétní zařízení, kde je aplikace nainstalovaná (data nejsou automaticky synchronizována všude).

## Porovnání s webovými aplikacemi

| Parametr | Desktopové aplikace | Webové aplikace |
| :--- | :--- | :--- |
| **Běhové prostředí** | Běží přímo v operačním systému | Běží uvnitř webového prohlížeče |
| **Instalace** | Je vyžadována instalace do systému | Není vyžadována žádná instalace |
| **Připojení** | Mohou pracovat zcela offline | Vyžadují neustálé připojení k internetu |
| **Výkon** | Vyšší (přímý přístup k HW a CPU) | Nižší (omezeno možnostmi prohlížeče) |
| **Kompatibilita** | Závislé na konkrétním OS | Multiplatformní (spustitelné na jakémkoli OS s prohlížečem) |
| **Dostupnost** | Dostupné jen na nainstalovaném zařízení | Dostupné odkudkoliv přes internet |
| **Aktualizace** | Nutnost lokální aktualizace | Aktualizace probíhají automaticky na serveru |
| **Bezpečnostní rizika** | Riziko infekce viry a malwarem | Vyšší riziko úniku dat z centrálního serveru |

## Multiplatformní aplikace

* Aplikace, které lze spustit na více různých operačních systémech (např. Windows, macOS, Linux).
* **Způsob realizace**:
  * Vývoj samostatných verzí pro každý operační systém zvlášť.
  * Využití multiplatformních frameworků (např. Electron, Qt, JavaFX, .NET MAUI), které umožňují psát jeden kód pro více platforem.

## Aktualizace desktopových aplikací

* **Manuální** – aktualizaci vyhledává a instaluje sám uživatel.
* **Automatické** – aplikace se aktualizuje na pozadí bez nutnosti zásahu uživatele.

### Typy aktualizací
* **Bezpečnostní** – opravují zranitelnosti a chyby v kódu.
* **Funkční** – přinášejí nové funkce a vylepšení uživatelského rozhraní.

### Význam aktualizací
Pravidelné aktualizace jsou klíčové pro stabilní chod, opravu softwarových chyb, zajištění bezpečnosti dat a přidávání nových možností pro uživatele.

## Bezpečnost

* **Riziko virů a malwaru** – stažením a spuštěním neověřeného programu může dojít k napadení celého systému.
* **Antivirová ochrana** – nutnost kontroly stahovaných souborů a sledování chování aplikací antivirovým softwarem.
* **Lokální ztráta dat** – jelikož aplikace ukládají data lokálně, existuje riziko jejich ztráty při selhání hardwaru (důležité je provádět pravidelné zálohování).
* **Zabezpečení aktualizací** – instalace pouze z důvěryhodných a oficiálních zdrojů.
