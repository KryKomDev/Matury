# Algoritmizace

## Osnova

* Algoritmus a jeho principy
* Vlastnosti algoritmů
* Druhy algoritmů
* Algoritmická složitost
* Známé algoritmy

## Algoritmus

* Teoretický princip řešení problému.
* Nejedná se o konkrétní implementaci v konkrétním programovacím jazyce, ale o logický návrh postupu.
* Příklad mimo programování: recept v kuchařce – jasný postup krok za krokem.

## Vlastnosti algoritmů

Co musí postup splňovat, aby se jednalo o algoritmus:

* **Elementárnost** – skládá se z konečného počtu jednoduchých (elementárních) kroků.
* **Konečnost** – počet kroků musí být konečný a algoritmus musí pro každý vstup skončit v konečném čase.
* **Obecnost** – neřeší jeden konkrétní výpočet (např. 1+2), ale obecnou třídu obdobných problémů (např. jak spočítat součet dvou libovolných čísel).
* **Determinovanost** – každý krok musí být jednoznačně a přesně definován. V každém okamžiku musí být jasné, co se bude dít v následujícím kroku. Lidské jazyky toto nesplňují kvůli své nejednoznačnosti, což vedlo ke vzniku programovacích jazyků s přesnou syntaxí a sémantikou.
* **Výstup** – algoritmus must mít alespoň jeden výstupní výsledek.

## Druhy algoritmů

### Rekurzivní
Opakovaně využívají samy sebe (funkce volá sama sebe).
* Příklad: výpočet faktoriálu.

```javascript
FUNCTION factorial(n) {
    IF (n == 1) return n;
    ELSE return n * factorial(n-1);
}
```

### Pravděpodobnostní
Provádí některá svá rozhodnutí náhodně.

### Genetické
Napodobují biologické evoluční procesy (např. Conwayova hra Game of life).

### Heuristické
Za cíl si nekladou nalézt absolutně přesné řešení, ale pouze nějaké dostatečně dobré přiblížení (aproximaci) v rozumném čase.

## Algoritmická složitost

* Účelem je navrhnout algoritmus, který skončí v rozumném čase a nespotřebuje příliš mnoho paměti.
* Jeden problém má často více různých řešení (více různých algoritmů). Nejjednodušší, nejméně komplexní a časově nejméně náročný algoritmus je většinou ten nejlepší.
* **Příklad s šachovým robotem**:
  * Mohli bychom pro každou herní pozici simulovat celou hru a najít absolutně nejlepší tah.
  * Extrémní počet možných kombinací tahů však nelze výpočetně zpracovat, i když teoreticky je to jednoduché (vyžadovalo by to obrovské množství výkonu, času a paměti).
  * Proto se využívají jiné algoritmy, které jsou složitější na pochopení, ale jsou efektivní a méně komplexní.

### Zápis složitosti – „Big O“ notace
Zápis vyjadřuje závislost výpočetního času (nebo paměťového prostoru) na velikosti vstupu (počtu prvků $n$).

* **O(n)** – lineární složitost. Počet kroků závisí lineárně na počtu vstupních dat (např. $n$ dat = $n$ kroků).
* **O(log n)** – logaritmická složitost. Počet kroků roste logaritmicky s počtem vstupních dat.
* **O(1)** – konstantní složitost. Nezávisí na množství dat, operace se provede vždy ve stejném počtu kroků (např. v jednom kroku).

Zároveň takto rozlišujeme složitost:
* **Časovou** – jak dlouho trvá běh programu.
* **Datovou/paměťovou** – jak velký prostor v operační paměti program za běhu zabere.

#### Příklad na výpočet sumy

```pascal
FUNCTION sumRecursive(n)
    IF n == 0 THEN
        RETURN 0
    ELSE
        RETURN n + sumRecursive(n - 1)
    END IF
END FUNCTION
```

```pascal
FUNCTION sumFormula(n)
    RETURN n * (n + 1) / 2
END FUNCTION
```

* **sumRecursive** – rekurzivní funkce:
  * Časová složitost: $O(n)$
  * Musí provést $n$ kroků.
  * Popis: zadáme číslo $n$, funkce následně volá sama sebe s hodnotou $n-1$, dokud se nedostane k nule.
  * Průběh pro $n = 4$:
    * `sumRecursive(4)`
      * `return 4 + sumRecursive(3)`
        * `return 3 + sumRecursive(2)`
          * `return 2 + sumRecursive(1)`
            * `return 1 + sumRecursive(0)`
              * `return 0`
    * Výstup: 4 + 3 + 2 + 1 + 0 (4 rekurzivní volání = 4 kroky).
    * Datová složitost je zde rovněž $O(n)$ kvůli ukládání volání do paměťového zásobníku.
* **sumFormula** – výpočet pomocí matematického vzorce:
  * Časová složitost: $O(1)$
  * Musí provést pouze jeden krok.
  * Popis: zadáme číslo $n$, funkce provede přímý matematický výpočet a okamžitě vrací výsledek.
  * Průběh pro $n = 4$:
    * `sumFormula(4)`
      * `return 4 * (4 + 1) / 2`
    * Výstup: 10.
    * Datová složitost je $O(1)$ (konstantní paměť).
* **Závěr**: Výpočet pomocí vzorce (`sumFormula`) je výrazně rychlejší a paměťově efektivnější než rekurze.

## Známé algoritmy

* **Dijkstrův algoritmus** – hledání nejkratší cesty v grafu (využití např. v GPS navigacích).
* **Řadicí algoritmy**:
  * **Bubble sort** (bublinkové řazení):
    * Postupně prochází prvky po dvojicích a pokud jsou ve špatném pořadí, prohodí je.
    * Příklad průchodu polem `[4, 1, 8, 5, 6]`:
      * (4, 1) → prohození na (1, 4)
      * (4, 8) → beze změny
      * (8, 5) → prohození na (5, 8)
      * (8, 6) → prohození na (6, 8)
      * Vznikne pole `[1, 4, 5, 6, 8]`. Poté se provede další kontrolní průchod. Pokud při průchodu nedojde k žádnému prohození, algoritmus končí.
    * Vysoká časová náročnost: $O(n^2)$.
  * **Heapsort** (řazení haldou).
  * **Quicksort** (rychlé řazení).

## Zdroje

* OTÁHAL, Ing Tomáš. Algoritmizace – úvod.
* Algoritmus. In: *Wikipedie* [online]. 2026 [cit. 08.03.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Algoritmus&oldid=25576234](https://cs.wikipedia.org/w/index.php?title=Algoritmus&oldid=25576234)
* Řadicí algoritmus. In: *Wikipedie* [online]. 2025 [cit. 08.03.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=%C5%98adic%C3%AD_algoritmus&oldid=25073222](https://cs.wikipedia.org/w/index.php?title=%C5%98adic%C3%AD_algoritmus&oldid=25073222)
