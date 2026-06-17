# Programovací jazyky

## Osnova

* Co je to programovací jazyk
* Historie
* Dělení:
  * Dle míry abstrakce (vyšší, nižší / např. Assembly)
  * Dle způsobu překladu a spuštění (kompilované, interpretované)
  * Dle oblasti použití (univerzální, doménově specifické)
  * Dle paradigmatu (procedurální, neprocedurální, multiparadigmatické)
* Kompilace

## Co je to programovací jazyk

* Prostředek pro zápis algoritmů.
* Zápis algoritmu se nazývá program.
* V podstatě se jedná o soubor pravil pro zápis algoritmu.

## Historie

* První programy vznikly už v 19. století (např. tkalcovské stavy, samohrající piana).
* Začátek 20. století: využití děrných štítků.
* Ve 30. a 40. letech:
  * Lambda kalkul (model popisu funkcí).
  * Turingův stroj ([wiki](https://cs.wikipedia.org/wiki/Turing%C5%AFv_stroj)) navržený Alanem Turingem jako teoretický model počítače.
  * Vznikl matematický základ pro algoritmy.
* Po roce 1940: vytvořeny první elektricky napájené digitální počítače a sálové počítače (využívající štítky s dírami).
* 60. léta: vznik jazyka Pascal.
* Nástup domácích počítačů: Basic, Assembly atd.
* 90. léta: vznik jazyků Python, Java a dalších.

## Dělení

### Dle míry abstrakce

* Vyšší jazyky:
  * Nemusíme provádět přímo operace s pamětí (maximálně se pracuje s pointry a alokací, ale neřeší se správa, kde konkrétně co ukládat).
  * Nabízejí lepší čitelnost pro lidi.
  * Příklady: Python, C#, Java.
* Nižší jazyky:
  * Musí se v nich definovat vše (např. ruční operace s pamětí).
  * Mají blízko ke strojovému kódu.
  * Příklad: Assembly (ASM).

### Dle způsobu překladu a spuštění

* Kompilované (překládají se jako celek, viz sekce [Kompilace](#kompilace)).
* Interpretované: interpret přímo vykonává instrukce „řádek po řádku“, často se jedná o skriptovací jazyky (např. JavaScript).

### Dle oblasti použití

* Univerzální:
  * Lze je použít pro všechny možné typy úloh.
  * Příklady: Python, C#.
* Doménově specifické:
  * Navržené pro specifické využití (např. skriptovací jazyky pro aplikace nebo značkovací jazyky).
  * Příklady: HTML, SQL.

### Dle paradigmatu

Vyšší programovací jazyky se dělí podle toho, jak jsou v nich formulována řešení problémů ([wiki](https://cs.wikipedia.org/wiki/Programovac%C3%AD_paradigma)).

#### Imperativní (procedurální) paradigma

* Popisuje výpočet pomocí posloupnosti příkazů a určuje přesný postup (algoritmus).
* Program se skládá ze sady proměnných, které mění svůj stav pomocí příkazů.
* Základní příkazy:
  * Přiřazení (např. `int a = 10`)
  * Cykly (`for`, `while`, …)
  * Příkazy pro větvení (`if`, `else`)
* Podkategorie:
  * **Strukturované**: bez možnosti skoků (bez klíčového slova `goto`), doporučuje se raději používat funkce (například jazyk C).
  * **Nestrukturované**: s možností skoků (použití `goto`).
  * **Objektově orientované (OOP)**: rozšiřuje procedurální přístup o koncept objektů, které sdružují data a chování (metody). Umožňuje zapouzdření, dědičnost a polymorfismus (například Java).

#### Deklarativní (neprocedurální) paradigma

* Popisuje, co se má dělat, nikoliv jak se to má udělat.
* Není možné vytvářet globální proměnné a proměnné samotné se využívají velmi střídmě.
* Všechno jsou hodnoty, které vrací funkce.
* Nejsou k dispozici cykly, pouze rekurze.
* Podkategorie:
  * **Funkcionální**: výpočet probíhá jako vyhodnocení funkcí (například Haskell).
  * **Logické**: použití matematické logiky (například Prolog).

#### Multiparadigmatické paradigma

* Umožňuje kombinovat jak imperativní, tak deklarativní přístupy (například Python, C++).

## Kompilace

* Provádí ji kompilátor, který překládá vyšší jazyk do nižšího (strojového), či přímo do strojového kódu:
  * C: běžně přímo do strojového kódu (může být mezikrok do ASM).
  * C++: mezikroky zahrnují konverzi do ASM, a potom ASM do strojového kódu.
  * C#, Java, Python (který je jinak interpretovaný): kompiluje se nejprve do bytecode/IL a následně se překládá pomocí JIT.

### Just in time kompilace (JIT)

* Zdrojový kód se nejprve přeloží do bytecode, který je nezávislý na platformě.
* Virtuální stroj tento bytecode následně interpretuje a spouští.
* Kompilátor překládá bloky kódu do strojového kódu za běhu programu, až když se mají zrovna spustit (například konkrétní funkci při jejím zavolání).

### Kompilace C++

1. **Preprocessing**:
   * Zpracuje řádky začínající na `#` (např. `#include` fungující jako import, podmíněná kompilace atd.).
   * Přidá konkrétní kód a vyřeší makra.
2. **Kompilace**:
   * Provede kontrolu syntaxe.
   * Převádí kód do ASM.
3. **Assembly**:
   * Převede ASM do object kódu (strojově čitelný, binární formát).
4. **Linking**:
   * Zkombinuje jednotlivé soubory object kódu.
   * Připojí externí knihovny.
   * Vytvoří spustitelný soubor (např. ve Windows přípona `.exe`).

## Zdroje

* C++ Compilation process. In: *GeeksforGeeks* [online]. 18:37:00+00:00 [cit. 22.03.2026]. Dostupné z: [https://www.geeksforgeeks.org/cpp/how-to-compile-a-cpp-program-using-gcc/](https://www.geeksforgeeks.org/cpp/how-to-compile-a-cpp-program-using-gcc/)
* Deklarativní programování. In: *Wikipedie* [online]. 2021 [cit. 22.03.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Deklarativn%C3%AD_programov%C3%A1n%C3%AD&oldid=20747674](https://cs.wikipedia.org/w/index.php?title=Deklarativn%C3%AD_programov%C3%A1n%C3%AD&oldid=20747674)
* Imperativní programování. In: *Wikipedie* [online]. 2021 [cit. 22.03.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Imperativn%C3%AD_programov%C3%A1n%C3%AD&oldid=20696777](https://cs.wikipedia.org/w/index.php?title=Imperativn%C3%AD_programov%C3%A1n%C3%AD&oldid=20696777)
* Objektově orientované programování. In: *Wikipedie* [online]. 2025 [cit. 22.03.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Objektov%C4%9B_orientovan%C3%A9_programov%C3%A1n%C3%AD&oldid=25348608](https://cs.wikipedia.org/w/index.php?title=Objektov%C4%9B_orientovan%C3%A9_programov%C3%A1n%C3%AD&oldid=25348608)
* Programovací jazyk. In: *Wikipedie* [online]. 2025 [cit. 22.03.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Programovac%C3%AD_jazyk&oldid=25074520](https://cs.wikipedia.org/w/index.php?title=Programovac%C3%AD_jazyk&oldid=25074520)
* Programovací paradigma. In: *Wikipedie* [online]. 2025 [cit. 22.03.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Programovac%C3%AD_paradigma&oldid=24932532](https://cs.wikipedia.org/w/index.php?title=Programovac%C3%AD_paradigma&oldid=24932532)
* Strukturované programování. In: *Wikipedie* [online]. 2023 [cit. 22.03.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Strukturovan%C3%A9_programov%C3%A1n%C3%AD&oldid=23157407](https://cs.wikipedia.org/w/index.php?title=Strukturovan%C3%A9_programov%C3%A1n%C3%AD&oldid=23157407)