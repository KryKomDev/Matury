# CPU a GPU

## Osnova

* Úvod
* CPU (Central Processing Unit)
* GPU (Graphics Processing Unit)
* Hlavní rozdíly
* Paralelní vs. sekvenční zpracování
* CPU a GPU v umělé inteligenci
* Vývoj CPU a GPU
* Výhody a nevýhody

## Úvod

* Dvě klíčové výpočetní jednotky moderního počítače.
* Obě slouží ke zpracování dat, ale jsou navrženy pro zcela rozdílné typy úloh.
* **CPU (Central Processing Unit)** – centrální procesor, funguje jako „mozek počítače“.
* **GPU (Graphics Processing Unit)** – grafický procesor, specializovaný na paralelní výpočty a grafiku.

## CPU (Central Processing Unit)

* Hlavní **řídicí a výpočetní** jednotka počítače.
* Stará se o **vykonávání instrukcí** operačního systému i všech spuštěných aplikací.

### Funkční cyklus CPU
Procesor pracuje v neustále se opakujícím cyklu (miliardkrát za sekundu):
1. **Fetch** – načtení instrukce z operační paměti.
2. **Decode** – dekódování instrukce (převod na konkrétní mikrooperace podle instrukční sady).
3. **Execute** – vykonání samotné instrukce v příslušné jednotce.
4. **Store** – uložení výsledku zpět do registru nebo paměti.

### Vnitřní struktura CPU
* **Řadič (Control Unit)** – řídí tok instrukcí a koordinuje činnost ostatních částí procesoru.
* **ALU (Aritmeticko-logická jednotka)** – provádí veškeré matematické (aritmetické) a logické operace (AND, OR, NOT).
* **Registry** – vnitřní, extrémně rychlé paměti procesoru o velmi malé kapacitě. Slouží k uchování dat, se kterými CPU aktuálně pracuje.
* **Cache paměť** – rychlá vyrovnávací paměť (úrovně L1, L2, L3), která uchovává často používaná data a instrukce, aby se zamezilo pomalejším přístupům do RAM.
* **Pipelining** – zřetězené zpracování instrukcí uvnitř jádra. Zatímco se jedna instrukce načítá, druhá se dekóduje a třetí se již vykonává.

### Parametry CPU
* **Frekvence (taktovací kmitočet)** – udává se v GHz a určuje, kolik miliard cyklů za sekundu dokáže jádro vykonat.
* **Počet jader (cores)** – samostatné fyzické výpočetní jednotky uvnitř procesoru. Každé jádro zpracovává úlohy nezávisle. Moderní CPU mají obvykle 4 až 16 jader.
* **Počet vláken (threads)** – logická jádra. Určuje, kolik úkolů dokáže jádro zpracovávat paralelně (např. díky technologii Hyper-Threading/SMT). Nejčastěji jsou to 2 vlákna na jedno jádro.
* **Velikost cache** – celková kapacita vyrovnávací paměti.
* **Architektura (např. x86, ARM)** – definuje sadu instrukcí procesoru. Programy musí odpovídat instrukční sadě dané architektury.

### Charakteristika CPU
* Vysoká **univerzálnost** (komunikuje s operačním systémem, programy a všemi komponentami).
* **Rychlá reakce na změny** toku instrukcí.
* Nízký celkový počet jader, ale velmi vysoký výkon na jedno jádro.

## GPU (Graphics Processing Unit)

* Specializovaný procesor navržený **primárně pro zpracování grafiky**.
* Dnes se kromě grafiky používá také pro:
  * Umělou inteligenci a strojové učení.
  * Vědecké a technické výpočty (GPGPU).
  * Kryptografii a těžbu kryptoměn.
  * Rendering videa a 3D scén.

### Funkce a architektura GPU
* GPU je navrženo pro **paralelní zpracování**.
* Dokáže provádět **tisíce jednoduchých operací současně** (např. výpočet barvy pro miliony pixelů najednou nebo trénování neuronových sítí).

### Vnitřní struktura GPU
* Skládá se z tisíců menších výpočetních jader.
* Využívá vlastní vysokorychlostní grafickou paměť **VRAM** (Video RAM).
* Obsahuje specializované jednotky:
  * **Tensorová jádra (Tensor Cores)** – optimalizovaná pro rychlé maticové výpočty využívané v AI.
  * **Ray Tracing Cores** – určená pro simulaci realistického chování světla.

### Typy GPU
* **Integrované GPU** – je přímo součástí procesoru, sdílí systémovou paměť RAM, má nižší výkon a je energeticky úsporné.
* **Dedikované GPU** – samostatná grafická karta s vlastním grafickým čipem a vlastní pamětí VRAM. Nabízí vysoký výkon za cenu vyšší spotřeby energie.

## Hlavní rozdíly

| Parametr | CPU | GPU |
| :--- | :--- | :--- |
| **Jádra** | Má méně výkonných jader (obvykle 4–16) | Má tisíce jednoduchých jader |
| **Typ výpočtů** | Běžné univerzální výpočty | Masivní paralelní výpočty |
| **Výkon na jádro** | Vyšší výkon na jedno jádro | Nižší výkon na jedno jádro |
| **Řízení** | Řídí a koordinuje celý počítač | Provádí specializované výpočty |
| **Paměť** | Pracuje se systémovou RAM | Používá dedikovanou VRAM |

## Paralelní vs. sekvenční zpracování

* **Sekvenční zpracování (CPU)**:
  * Instrukce jsou vykonávány postupně, jedna po druhé.
  * Vhodné pro: operační systém, běžné aplikace, složité podmínky a logické větvení.
* **Paralelní zpracování (GPU)**:
  * Mnoho výpočtů a instrukcí probíhá současně v jeden okamžik.
  * Vhodné pro: 3D grafiku, výpočty matic, neuronové sítě a fyzikální simulace.

## CPU a GPU v umělé inteligenci

* Trénování neuronových sítí vyžaduje obrovské množství paralelních výpočtů a operací s maticemi.
* **GPU je v AI mnohem efektivnější** než CPU (např. trénování modelu, které by na CPU trvalo dny, trvá na GPU pouze hodiny).
* Moderní GPU obsahují speciální jednotky jako Tensor Cores a dedikované AI akcelerátory.

## Vývoj CPU a GPU

* **Vývoj CPU**:
  * Původně se vývoj zaměřoval na zvyšování frekvence.
  * Z důvodu fyzikálních limitů (přehřívání) se přešlo na vícejádrové architektury.
  * Dnes se klade důraz také na energetickou efektivitu a specializované instrukční sady.
* **Vývoj GPU**:
  * Masivní nárůst počtu jader.
  * Rozvoj paralelního programování a rozhraní (např. technologie CUDA od společnosti NVIDIA).
  * Využití grafických karet pro obecné výpočty mimo grafiku (GPGPU).

## Výhody a nevýhody

### CPU
* **Výhody**: univerzálnost, vysoká flexibilita, efektivní řízení systému.
* **Nevýhody**: omezený výkon při potřebě masivního paralelního zpracování.

### GPU
* **Výhody**: extrémní paralelní výkon, ideální pro zpracování grafických prvků, video rendering a AI výpočty.
* **Nevýhody**: méně flexibilní architektura pro obecný běh aplikací, vyšší spotřeba elektrické energie.
