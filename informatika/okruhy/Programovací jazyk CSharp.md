# Programovací jazyk C#

**Poznámka**: tato otázka je víc praktická a půjde z velké části o popis kódu.

## Osnova

* Vlastnosti
* .NET
* Vývojová prostředí
* Základní syntaxe

## Vlastnosti

* **Multiparadigmatický programovací jazyk**:
  * Imperativní i deklarativní
  * Objektově orientovaný (OOP)
  * Funkční
* Pochází z rodiny C jazyků.
* **Typy aplikací**:
  * Souborové: `.cs` soubor (např. skript).
  * Projektové: `.csproj` (může zahrnovat více zdrojových souborů, celá aplikace).
* Vytvořen a vyvíjen společností Microsoft.
* O automatickou správu paměti se stará **garbage collector**.
* Kód je kompilovaný do mezijazyka **Common Intermediate Language (CIL)**.
* **Typový systém**: C# je silně typovaný (strong typing) a staticky typovaný (typ proměnné je znám již při kompilaci a musí být striktně dodržován, což pomáhá zachycovat chyby v rané fázi vývoje).
  * Typová inference je však možná pomocí klíčového slova `var`.
* Jazyk je plně postaven na principech **objektově orientovaného programování (OOP)** – podporuje dědičnost, polymorfismus, zapouzdření a abstrakci.
* Je součástí platformy **.NET**, která mu poskytuje rozsáhlou knihovnu tříd, běhové prostředí a možnost jazykové interoperability s jinými .NET jazyky.
* Spouštění C# aplikací zajišťuje běhové prostředí **Common Language Runtime (CLR)**.
  * CLR je virtuální stroj, který se stará o řízení běhu aplikace, ošetřování výjimek, bezpečnost a také o **Just-In-Time (JIT)** kompilaci, která převádí CIL kód do nativního strojového kódu těsně před spuštěním.

![][image1]
*By Deviousasti - Own work, CC BY-SA 4.0, [Wikimedia](https://commons.wikimedia.org/w/index.php?curid=88880454)*

* Celý systém C# a .NET se řídí standardem **Common Language Infrastructure (CLI)**, který definuje specifikace pro běhové prostředí a formáty spustitelných souborů.
* Díky .NET je C# multiplatformní a umožňuje vývoj široké škály aplikací:
  * Webové aplikace (ASP.NET Core)
  * Desktopové aplikace (Universal Windows Platform, WPF, Windows Forms)
  * Mobilní aplikace (Xamarin, .NET MAUI)
  * Herní vývoj (např. engine Unity)
  * IoT řešení

## .NET

* Bezplatná open-source platforma (framework).
* Vyvíjen primárně společností Microsoft a komunitou.
* Vznikl společně s jazykem C#.
* Nabízí podporu pro více programovacích jazyků (např. C#, F#).
* **Meziplatformní využití**:
  * Webové aplikace (ASP.NET Core)
  * CLI (příkazové) aplikace
  * Knihovny a API
  * Desktopové aplikace
* **Package manager**: NuGet (slouží k distribuci knihoven a nástrojů).

## Vývojová prostředí

* **Visual Studio**
  * Plnohodnotné integrované vývojové prostředí (IDE) od Microsoftu.
  * Model freemium (edice Community je zdarma pro jednotlivce a výuku, často na školních počítačích).
* **Rider**
  * Pokročilé integrované vývojové prostředí od společnosti JetBrains (placená licence).
* **Visual Studio Code**
  * Lehký textový editor od Microsoftu, pro C# je nutné nainstalovat příslušné pluginy (rozšíření). Zdarma.

## Základní syntaxe

### Import knihoven a jmenné prostory

* **Klíčové slovo `using`**: Slouží k importu knihoven (např. jmenného prostoru `System`).
* **Klíčové slovo `namespace`**: Kontejner pro organizaci tříd a dalších jmenných prostorů.

### Proměnné a typy

* Deklarace proměnné se provádí ve formátu: `typ jméno = hodnota;`.
* **Klíčové slovo `var` (typová inference)**: Umožňuje kompilátoru automaticky odvodit typ proměnné na základě přiřazené hodnoty (např. zápis `var a = "ahoj";` je ekvivalentní k `string a = "ahoj";`). Typ proměnné je však stále pevně dán při kompilaci.
* **Omezení přístupu (v kontextu tříd)**:
  * `public` - přístupné odevšad.
  * `private` - přístupné pouze v rámci dané třídy.
  * `protected` - přístupné v dané třídě a jejích potomcích.
  * `internal` - přístupné pouze v rámci aktuální assembly (projektu).
  * `private protected` / `protected internal` - specifické kombinace omezení přístupu.

### Hodnotové vs. odkazové typy

* **Hodnotové typy (Value types)**:
  * Uchovávají svá data přímo v paměti (na zásobníku - stack).
  * Patří sem předdefinované číselné a jiné primitivní typy (např. `int`, `bool`, `float`, `double`, `char`), struktury (`struct`) a výčtové typy (`enum`).
* **Odkazové typy (Reference types)**:
  * Obsahují odkaz (pointer) na objekt, který je uložen na spravované haldě (heap).
  * Patří sem třídy (`class`), pole, delegáty (metody jako argumenty – lambda výrazy, callbacky) a řetězce (`string`).
  * Pozor: `string` (řetězec) je odkazový typ, i když se zapisuje s malým počátečním písmenem.
  * **Příklad sdílení odkazů**:
    * Mějme proměnnou `pepa` odkazující na nějaký objekt.
    * Vytvoříme proměnnou `svalovec` a přiřadíme jí hodnotu: `svalovec = pepa`.
    * Obě proměnné nyní odkazují na stejný objekt v paměti. Volání `svalovec.pozdrav()` provede totéž co `pepa.pozdrav()`.
* Kompletní přehled vestavěných typů naleznete v [oficiální tabulce](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types).

### Cykly (Loopy)

* **`for` a `foreach`**: Používají se pro iteraci přes kolekce či stanovené rozsahy.
* **`while` a `do-while`**:
  * `while` nejprve vyhodnotí podmínku a pokud neplatí, tělo cyklu se vůbec nespustí.
  * `do-while` nejprve vykoná tělo cyklu a podmínku vyhodnotí až poté (cyklus se tedy spustí vždy alespoň jednou).

### Vlastnosti a modifikátory přístupu (Accessory)

* **`get` a `set`**: Slouží k definování přístupových metod (vlastností) pro čtení a zápis privátních proměnných.
* **`static`**: Označuje, že daná proměnná, metoda či celá třída patří samotnému typu (třídě), nikoli konkrétní instanci (objektu).
* **`const`**: Slouží k definování konstant, jejichž hodnota je známa při kompilaci a nelze ji později změnit (např. `public const string Version = "v1.0.0";`).

### Dědičnost

* Pro dědičnost se používá symbol dvojtečky `:` (např. `class Car : Vehicle`).
* **`sealed`**: Zamezuje dědění od dané třídy (např. `sealed class Vehicle`). Pokud se pak pokusíte dědit, kompilátor vyhodí chybu.
* **`abstract`**: Označuje abstraktní třídy nebo metody. Implementaci takové metody pak musí poskytnout odvozená třída (potomek).

### Vstup a výstup

* Pro přístup k chybovému, standardnímu vstupu a výstupu se využívá třída `Console` (např. `Console.WriteLine()`, `Console.ReadLine()`).

## Zdroje

* BILLWAGNER. Built-in types - C# reference. In: [cit. 29.03.2026]. Dostupné z: [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types)
* BILLWAGNER. C# Keywords and contextual keywords - C# reference. In: [cit. 29.03.2026]. Dostupné z: [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/)
* BILLWAGNER. Iteration statements -for, foreach, do, and while - C# reference. In: [cit. 29.03.2026]. Dostupné z: [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/iteration-statements](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/iteration-statements)
* BILLWAGNER. static modifier - C# reference. In: [cit. 29.03.2026]. Dostupné z: [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/static](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/static)
* BILLWAGNER. Systém typů jazyka C# - C#. In: [cit. 29.03.2026]. Dostupné z: [https://learn.microsoft.com/cs-cz/dotnet/csharp/fundamentals/types/](https://learn.microsoft.com/cs-cz/dotnet/csharp/fundamentals/types/)
* BILLWAGNER. The base keyword - C# reference. In: [cit. 29.03.2026]. Dostupné z: [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/base](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/base)
* BILLWAGNER. Using Properties - C#. In: [cit. 29.03.2026]. Dostupné z: [https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/using-properties](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/using-properties)
* C++/CLI. In: *Wikipedia* [online]. 2025 [cit. 29.03.2026]. Dostupné z: [https://en.wikipedia.org/w/index.php?title=C%2B%2B/CLI&oldid=1314679652](https://en.wikipedia.org/w/index.php?title=C%2B%2B/CLI&oldid=1314679652)
* C# Inheritance. In: [cit. 29.03.2026]. Dostupné z: [https://www.w3schools.com/cs/cs_inheritance.php](https://www.w3schools.com/cs/cs_inheritance.php)
* C Sharp (programming language). In: *Wikipedia* [online]. 2026 [cit. 29.03.2026]. Dostupné z: [https://en.wikipedia.org/w/index.php?title=C_Sharp_(programming_language)&oldid=1344058409](https://en.wikipedia.org/w/index.php?title=C_Sharp_(programming_language)&oldid=1344058409)
* C# Syntax. In: [cit. 29.03.2026]. Dostupné z: [https://www.w3schools.com/cs/cs_syntax.php](https://www.w3schools.com/cs/cs_syntax.php)
* .NET. In: *Wikipedia* [online]. 2026 [cit. 29.03.2026]. Dostupné z: [https://en.wikipedia.org/w/index.php?title=.NET&oldid=1342765345](https://en.wikipedia.org/w/index.php?title=.NET&oldid=1342765345)

[image1]: <data:image/png;base64,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>