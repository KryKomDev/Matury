# Objektově orientované programování

## Osnova

* Základní informace
* Koncepce OOP
  * Objekty, abstrakce, zapouzdření, kompozice, delegování, dědičnost, polymorfismus
* Programovací jazyky
* Teorie objektů
  * Třída, dědičnost, metoda, atomizace

## Základní informace

* **OOP** = Objektově Orientované Programování.
* Programovací paradigma modelované podle reálného světa (snaha o reprezentaci reality v poměru 1:1).
* Implementace se mezi jednotlivými programovacími jazyky liší.

## Koncepce OOP

* **Objekty**
  * Každý objekt má svou třídu (je její instancí).
* **Abstrakce**
  * Pokud potřebujeme opakovat nějakou činnost, vytvoříme pro ni abstrakci (např. metodu).
  * V kontextu tříd: supertřída nemusí implementovat nějakou metodu, přenechá její implementaci podtřídám.
* **Zapouzdření**
  * Každý objekt má své rozhraní pro přístup.
  * Některé vnitřní prvky a data jsou zvenčí (z jiných objektů) nepřístupné.
* **Kompozice**
  * Objekt může obsahovat jiné objekty jako své součásti.
* **Delegování**
  * Objekt může využívat služeb jiných objektů (přenechává jim provedení operace).
* **Dědičnost**
  * Třída může dědit od jiné třídy (vytváří se stromová struktura 1:N).
  * Příklad hierarchie:
    * `Animal` (předek) -> `Dog`, `Cat`, `Fish` (potomci)
    * `Dog` (předek) -> `Shepherd`, `Bulldog` (potomci)
* **Polymorfismus** (mnohotvárnost)
  * Objekt se chová podle toho, jaké třídy je instancí.
  * Několik objektů může sdílet stejné rozhraní – navenek pracují stejně, ale vnitřně se chování liší podle implementace.
  * **Polymorfismus dědičnosti:**
    * Tam, kde je očekávána instance určité třídy, můžeme dosadit instanci její podtřídy.
    * Příklad: do metody `void greetAnimal(Animal)` můžeme předat instanci `Dog`, `Cat`, `Fish`, ale i nepřímé podtřídy jako `Shepherd` nebo `Bulldog`.

## Programovací jazyky

* Jazyky: Java, C++, C#, PHP, Python, Rust, Go, …
* **Čistě objektové jazyky** (vše musí být definováno uvnitř třídy):
  * Java, C#
* **Multiparadigmatické jazyky** (objekty umožňují, ale nevyžadují):
  * Python, PHP

## Teorie objektů

* **Třída**
  * Uspořádání informací do jedné entity.
  * **Instance** = objekt. Skládá se z:
    * Atributů (vlastností)
    * Operací (metod) – jejich zveřejněním vzniká rozhraní pro práci s objektem.
  * U objektu nás zajímá, jaké služby poskytuje, nikoli to, jak je vnitřně vykonává (zapouzdření).
* **Dědičnost**
  * **Supertřída** – třída, ze které se dědí (rodič).
  * **Podtřída** – třída, která dědí od supertřídy (potomek).
  * **Překrytí (override)** – přepis metody podtřídou, čímž se definuje nová logika.
* **Metoda**
  * Představuje rozhraní třídy a vykonává určitou činnost.
  * **Překrytí (override)** – změna chování metody v podtřídě.
  * **Přetížení (overload)**
    * **Přetížení metody:**
      * Rozhodnutí o tom, která konkrétní metoda bude volána, provádí překladač při kompilaci podle počtu a typu parametrů.
      * Můžeme mít metody se stejným názvem, ale s různými parametry.
      * Příklad: `prumer(int cislo1, int cislo2)` a `prumer(int cislo1, int cislo2, int cislo3)`. Volání `prumer(1, 1)` vybere první, volání `prumer(1, 1, 1)` vybere druhé.
    * **Přetížení operátoru:**
      * Například v jazyce C# lze přetížit operátor `+` a definovat tak, co se stane, když sečteme dvě instance dané třídy.
* **Atomizace**
  * Metoda i objekt by měly řešit právě jeden konkrétní, jasně vymezený problém.

## Zdoje

* Dědičnost (objektově orientované programování). In: *Wikipedie* [online]. 2024 [cit. 29.03.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=D%C4%9Bdi%C4%8Dnost_(objektov%C4%9B_orientovan%C3%A9_programov%C3%A1n%C3%AD)&oldid=24142117](https://cs.wikipedia.org/w/index.php?title=D%C4%9Bdi%C4%8Dnost_(objektov%C4%9B_orientovan%C3%A9_programov%C3%A1n%C3%AD)&oldid=24142117)
* Objektově orientované programování. In: *Wikipedie* [online]. 2025 [cit. 29.03.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Objektov%C4%9B_orientovan%C3%A9_programov%C3%A1n%C3%AD&oldid=25348608](https://cs.wikipedia.org/w/index.php?title=Objektov%C4%9B_orientovan%C3%A9_programov%C3%A1n%C3%AD&oldid=25348608)
* Přetěžování. In: *Wikipedie* [online]. 2026 [cit. 29.03.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=P%C5%99et%C4%9B%C5%BEov%C3%A1n%C3%AD&oldid=25774178#P%C5%99et%C3%AD%C5%BEen%C3%AD_funkce](https://cs.wikipedia.org/w/index.php?title=P%C5%99et%C4%9B%C5%BEov%C3%A1n%C3%AD&oldid=25774178#P%C5%99et%C3%AD%C5%BEen%C3%AD_funkce)