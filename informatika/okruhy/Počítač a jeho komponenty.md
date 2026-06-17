# Počítač a jeho komponenty

## Osnova

* Úvod
* Základní architektura počítače
* Základní deska (Motherboard)
* Procesor
* Operační paměť
* Úložná zařízení
* Grafická karta
* Sběrnice
* Zdroj
* Chlazení
* Vstupní a výstupní zařízení
* Moderní trendy

## Úvod

* **Počítač** - zařízení určené ke zpracování informací podle předem daného programu.
* **Princip fungování**: Vstup dat -> Zpracování -> Výstup výsledků -> Ukládání dat.
* Rozděluje se na **hardware** (fyzické komponenty) a **software** (programové vybavení).
* Všechny informace jsou uvnitř počítače reprezentovány **binárně** (pomocí 0 a 1).
* Moderní počítače koncepčně vycházejí z tzv. **von Neumannovy architektury** (program i zpracovávaná data jsou uloženy ve společné operační paměti).

## Základní architektura počítače

Základní stavební bloky počítačového systému tvoří:
* **Procesor (CPU)**
* **Operační paměť (RAM)**
* **Úložné zařízení** (HDD, SSD)
* **Sběrnice** (zajišťují fyzické propojení komponent a přenos signálů)
* **Vstupní zařízení**
* **Výstupní zařízení**

## Základní deska (Motherboard)

* Základní deska **propojuje všechny komponenty** počítače a umožňuje jim vzájemně komunikovat.
* Bez ní by jednotlivé komponenty nemohly spolupracovat.
* **Obsahuje**:
  * Patici pro procesor (socket)
  * Sloty pro operační paměť (RAM)
  * Konektory pro disky (SATA, M.2)
  * PCIe sloty pro rozšiřující karty (např. grafickou kartu)
  * Čipset (řídí komunikaci mezi komponentami)
  * BIOS/UEFI - základní software, který spouští a konfiguruje hardware při zapnutí počítače ještě před zavedením operačního systému

## Procesor (CPU)

* **Nejdůležitější součást počítače** („mozek počítače“).
* Postupně **načítá instrukce** z paměti, **dekóduje** je a **vykonává**.
* Zajišťuje **řízení** ostatních komponent a provádění **aritmetických a logických operací**.

### Vnitřní části procesoru

* **Řadič (Control Unit)**
  * Řídí tok instrukcí a určuje, jaké operace se mají v jakém pořadí provést.
* **ALU (Aritmeticko-logická jednotka)**
  * Provádí matematické operace (sčítání, násobení) a logické operace (AND, OR, NOT).
* **Registry**
  * Velmi malé a velmi rychlé paměti přímo uvnitř CPU, které uchovávají aktuálně zpracovávaná data a instrukce.

### Důležité parametry CPU

* **Frekvence (GHz)** - počet hodinových cyklů procesoru za sekundu.
* **Počet jader** - moderní procesory mají více fyzických jader (např. 4, 8, 16), z nichž každé může samostatně a paralelně zpracovávat vlastní úlohu.
* **Vlákna (threads)** - technologie (např. Hyper-Threading) umožňující jednomu fyzickému jádru zpracovávat více softwarových vláken současně.
* **Cache paměť** - velmi rychlá vyrovnávací paměť uvnitř procesoru (L1, L2, L3), která výrazně zrychluje přístup k často používaným datům.

## Operační paměť (RAM)

* Pracovní paměť počítače (Random Access Memory).
* **Vlastnosti**:
  * Velmi rychlá.
  * Data jsou volatilní (po vypnutí napájení se smažou).
  * Ukládá aktuálně spuštěné programy a jejich data.
* **Vliv na výkon**: Čím větší je kapacita RAM, tím lepší je multitasking a tím méně dochází ke zpomalování systému.
* **Typy RAM**: DDR4, DDR5.

## Úložná zařízení

Slouží k dlouhodobému a trvalému ukládání dat (nevolatilní paměti).

* **HDD (Hard Disk Drive)**
  * Mechanické zařízení obsahující rotující magnetické plotny a čtecí hlavy.
  * Výhody: nižší cena za jednotku kapacity.
  * Nevýhody: pomalejší přenosové rychlosti, náchylnost k mechanickému poškození a otřesům.
* **SSD (Solid State Drive)**
  * Polovodičové zařízení bez pohyblivých částí, využívající flash paměť.
  * Výhody: mnohem rychlejší než HDD, tichý chod, vysoká odolnost vůči otřesům a nárazům.
  * Nevýhody: omezený počet cyklů zápisu.

## Grafická karta (GPU)

* Specializovaný procesor navržený pro rychlé paralelní výpočty grafiky (obsahuje tisíce malých výpočetních jednotek).
* **Používá se pro**: zobrazování obrazu, 3D grafiku, hry, video rendering, strojové učení a AI.
* **Typy podle integrace**:
  * **Integrovaná** - je přímou součástí procesoru (CPU), sdílí s ním operační paměť RAM, vhodná pro méně náročné úlohy.
  * **Dedikovaná** - samostatná karta s vlastním grafickým procesorem (GPU), vlastní rychlou grafickou pamětí (VRAM) a chlazením.

## Sběrnice

* Systém vodičů a spojů, který umožňuje přenos dat a řídicích signálů mezi jednotlivými komponentami.
* **Základní typy sběrnic**:
  * **Datová sběrnice** - slouží k samotnému přenosu dat.
  * **Adresová sběrnice** - určuje, ze které nebo do které paměťové lokace se mají data číst či zapisovat.
  * **Řídicí sběrnice** - přenáší řídicí signály a příkazy (např. požadavek na čtení, zápis, synchronizaci hodin atd.).
* Rychlost a šířka sběrnice přímo ovlivňují celkový výkon systému (dnes jsou sběrnice často integrovány do jednoho propojení, např. PCIe).

## Zdroj

* Napájí elektrickou energií všechny komponenty počítače a musí disponovat dostatečným výkonem (např. 500 W, 750 W).
* Převádí střídavý proud ze zásuvky (230 V) na stejnosměrné napětí požadované komponentami (12 V, 5 V, 3,3 V).

## Chlazení

* Komponenty (zejména CPU a GPU) produkují při práci značné množství tepla. Bez účinného chlazení hrozí přehřátí, snížení výkonu (thermal throttling) či poškození hardwaru.
* **Způsoby chlazení**:
  * **Vzduchové chlazení** - pasivní chladiče (kovové pasivy) v kombinaci s ventilátory pro odvod teplého vzduchu.
  * **Kapalinové chlazení** - uzavřený okruh s chladicí kapalinou, která efektivněji odvádí teplo z procesoru k radiátoru.

## Vstupní a výstupní zařízení

* **Vstupní zařízení** - slouží k zadávání dat a příkazů do počítače (např. klávesnice, myš, skener, mikrofon, webkamera).
* **Výstupní zařízení** - slouží k prezentaci a zobrazování zpracovaných dat z počítače uživateli (např. monitor, tiskárna, reproduktory, sluchátka).

## Moderní trendy

* Vícejádrové a hybridní architektury procesorů (kombinace výkonných a úsporných jader).
* Neustálá miniaturizace výrobních procesů (např. 3nm technologie).
* Cloud computing (přesun výpočtů a dat na vzdálené servery).
* Specializované hardwarové akcelerátory pro umělou inteligenci (AI čipy, NPU).
* Důraz na energetickou efektivitu a ekologický provoz komponent.