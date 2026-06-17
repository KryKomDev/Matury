# Paměť

## Osnova

* Co je to paměť
* Historie
* Paměťová hierarchie
* Dělení podle volatility (energetická závislost)
* Správa paměti

## Co je to paměť

* Fyzické zařízení k ukládání programů nebo dat pro okamžitou či trvalou potřebu.

### Vnitřní paměť

* Slouží k ukládání informací ve fyzických zařízeních s vysokou rychlostí přístupu (např. RAM).

### Vnější paměť

* Fyzická zařízení pro dlouhodobé ukládání programů a dat (např. HDD, SSD).
* Pomalá rychlost přístupu, ale výrazně větší kapacita.

### Virtuální paměť

* Procesy nemají přímý přístup k reálným fyzickým adresám.
* Přístup zajišťuje operační systém, který procesům přiděluje virtuální adresy.
  * **Důvod (bezpečnost)**: Zamezení tomu, aby procesy mohly přistupovat do paměti jiných procesů.
* Umožňuje využít část vnější paměti (např. SSD/HDD) k rozšíření kapacity vnitřní paměti (RAM) – tomu se říká **swap** či **paging**.

### Polovodičová paměť

* **Energeticky závislá** (např. RAM) – data se při odpojení napájení ztratí.
* **Energeticky nezávislá** (např. flash, ROM) – data zůstávají zachována.
* **Paměťové buňky**:
  * Mohou nabývat 2 stavů: zapnuto/vypnuto (reprezentuje 1 bit).
  * Shlukují se do „slov“ s pevnou délkou, přičemž každé slovo má svou unikátní adresu.

## Historie

* **40. léta 20. století** – paměti měly kapacitu jen několik bajtů.
  * Počítač ENIAC využíval elektronky a umožňoval výpočty pouze s 20místnými čísly.
  * Později se používala paměť s akustickou zpožďovací linkou.
  * Na konci 40. let začaly snahy o vývoj energeticky nezávislých pamětí (např. feritové paměti).
* **60. léta** – nástup tranzistorových pamětí.

## Paměťová hierarchie

Popisuje uspořádání paměťových zařízení podle rychlosti přístupu, kapacity a ceny. Cílem je zajistit, aby procesor měl co nejrychlejší přístup k datům, která aktuálně potřebuje (nedávno přistoupená data se ukládají blíže k procesoru).

### Dělení podle rychlosti a velikosti

* **Registry**
  * Nejrychlejší a nejmenší paměť přímo v procesoru (CPU).
  * Slouží k uchovávání aktuálně zpracovávaných dat a instrukcí.
* **Cache (L1, L2, L3)**
  * Velmi rychlá a malá paměť (SRAM) umístěná v blízkosti CPU nebo přímo v něm.
  * **L1 Cache**: Nejmenší a nejrychlejší, oddělená pro data a instrukce, umístěná přímo v jádře CPU.
  * **L2 Cache**: Větší než L1, ale pomalejší, obvykle sdílená jádry.
  * **L3 Cache**: Největší a nejpomalejší z cache pamětí, často sdílená všemi jádry procesoru.
* **Hlavní paměť (RAM)**
  * Větší a pomalejší než cache, realizovaná jako DRAM.
  * Slouží jako pracovní paměť pro spuštěné programy.
* **Sekundární úložiště (SSD/HDD)**
  * Nabízí největší kapacitu a nejpomalejší přístup.
  * Slouží pro trvalé ukládání dat a rozšíření RAM pomocí virtuální paměti.

## Dělení podle volatility

### Volatilní paměť

Vyžaduje neustálé napětí pro uchování informací.

* **Statická RAM (SRAM)**
  * Nepotřebuje periodickou obnovu dat.
  * Rychlá, ale složitější a drahá (využívá čtyři až šest tranzistorů na jeden bit).
  * Používá se především jako hardwarová cache.
* **Dynamická RAM (DRAM)**
  * Při každém přečtení se data vymažou, kondenzátory se vybíjejí, a proto vyžaduje neustálé obnovovací cykly.
  * Jeden bit je tvořen jedním tranzistorem a kondenzátorem, což přináší nižší cenu při vyšší kapacitě.
  * **Synchronní DRAM (SDRAM)**: Moderní paměti využívané dnes (např. DDR3, DDR4, DDR5).

### Nevolatilní paměť

Uchovává informace i bez napájení.

* **ROM (Read-Only Memory)**
  * Paměť určená pouze pro čtení, zápis probíhá pouze při výrobě.
  * Používá se pro ukládání firmwaru.
* **Flash**
  * Používá se ve flash discích, SD kartách a také pro ukládání firmwaru.
  * Lze z ní číst i do ní zapisovat.
* **HDD (Pevný disk)**
  * Data se zapisují mechanicky na točící se magnetické disky.
* **SSD (Polovodičový disk)**
  * Využívá elektrické buňky rozdělené do stránek a bloků (digitální reprezentace dat).
  * **Výhody**: Vyšší rychlost, odolnost vůči otřesům.
  * **Nevýhody**: Horší životnost ve srovnání s HDD.

## Správa paměti

Soubor metod, které operační systém využívá pro přidělování a uvolňování operační paměti, nastavování ochrany a správu adresace.

* **Garbage collection** - automatizovaná správa paměti, která uvolňuje již nepoužívanou paměť.
* **Ruční správa paměti** - programátor sám žádá o alokaci paměti a následné uvolnění (např. v jazyce C pomocí funkcí `malloc`, `free` atd.).
* **Adresování**:
  * **Přímé (fyzické)** - logický adresový prostor odpovídá přímo fyzickému hardwaru.
  * **Virtuální** - logický adresový prostor, který umožňuje přistupovat k médiím jako SSD/HDD stejně jako k RAM (jednoduché rozšíření paměti).

### Úkoly správy fyzického adresového prostoru (plní OS)

* Přidělování paměťových regionů na požádání procesů.
* Uvolňování paměťových regionů na požádání procesů.
* Udržování informací o obsazení adresového prostoru.
* Zabezpečení ochrany paměti – zabránění přístupu procesu k paměti mimo jeho přidělený region.
* Podpora střídavého běhu více procesů u víceúlohových systémů.

### Chyby při správě paměti

* **Aritmetické přetečení (integer overflow)**
* **Únik paměti (memory leak)** - proces nevrátí přidělenou paměť zpět systému, paměť se postupně zaplňuje, dokud se proces neukončí.
* **Porušení ochrany paměti** - proces se pokouší přistoupit k paměti, do které nemá přístup; OS jej z bezpečnostních důvodů ukončí.
* **Přetečení vyrovnávací paměti (buffer overflow)** - proces zapisuje data mimo alokovanou paměť, čímž přepíše paměť jiných procesů (častý základ softwarových zranitelností).

## Zdroje

* C Memory Management (Memory Allocation). In: [cit. 12.05.2026]. Dostupné z: [https://www.w3schools.com/c/c_memory_management.php](https://www.w3schools.com/c/c_memory_management.php)
* Memory Management in Operating System. In: *GeeksforGeeks* [online]. 00:52:07+00:00 [cit. 12.05.2026]. Dostupné z: [https://www.geeksforgeeks.org/operating-systems/memory-management-in-operating-system/](https://www.geeksforgeeks.org/operating-systems/memory-management-in-operating-system/)
* Počítačová paměť. In: *Wikipedie* [online]. 2026 [cit. 12.05.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Po%C4%8D%C3%ADta%C4%8Dov%C3%A1_pam%C4%9B%C5%A5&oldid=25644691](https://cs.wikipedia.org/w/index.php?title=Po%C4%8D%C3%ADta%C4%8Dov%C3%A1_pam%C4%9B%C5%A5&oldid=25644691)
* Správa paměti. In: *Wikipedie* [online]. 2025 [cit. 12.05.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Spr%C3%A1va_pam%C4%9Bti&oldid=24803657](https://cs.wikipedia.org/w/index.php?title=Spr%C3%A1va_pam%C4%9Bti&oldid=24803657)
