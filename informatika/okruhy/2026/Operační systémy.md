# Operační systémy

## Osnova

* Definice OS
* Hlavní funkce OS
* Proč OS vznikl?
* Architektura OS
* Druhy OS podle oblasti použití
* Druhy OS podle počtu uživatelů
* Druhy OS podle počtu úloh
* Příklady významných OS
* Multitasking
* Přístupová práva a bezpečnost v OS
* Práce se soubory

## Definice operačního systému

* **Operační systém** = základní software, který zajišťuje chod počítače a umožňuje uživateli pracovat s aplikacemi.
* Program či soubor programů, který se spustí při startu počítače.
* Zajišťuje komunikaci mezi hardwarem a aplikacemi (bez něj nelze spouštět programy).

## Hlavní funkce OS

* **Správa procesů**
  * Přidělování výpočetního času CPU jednotlivým procesům
  * Rozhoduje, který proces poběží a jak dlouho
* **Správa paměti**
  * Přiděluje operační paměť procesům
  * Chrání paměť jednotlivých procesů před sebou navzájem
* **Správa zařízení**
  * Ovládá periferie (klávesnice, myš, tiskárna…) + využívá ovladače zařízení
* **Organizace přístupu k datům**
  * Ukládání a čtení dat z disků
  * Práce se soubory a složkami (případně zamezení neoprávněného přístupu)
* **Komunikace s uživatelem** prostřednictvím speciálního programu zvaného obecně Shell
* **Provádění zadaných příkazů** (uživatelem) a spouštění aplikací

## Proč OS vznikl?

Každý proces potřebuje: procesor, paměť a vstupní a výstupní zařízení. Bez OS by si každý proces musel řídit hardware sám a systém by byl složitý a nestabilní.

OS vznikl proto, aby:
* **Sjednotil přístup k hardware**
* **Zjednodušil tvorbu programů**
* **Zvýšil bezpečnost a stabilitu**
* Obecně zjednodušil práci programům i uživatelům

## Architektura OS

* **Jádro** (kernel) - základní část OS
  * Zajišťuje: správu procesů, správu paměti, komunikaci s hardwarem
  * Bez jádra OS nefunguje
* **Ovladače zařízení** - zajišťují komunikaci s hardwarem
* **Pomocné programy** - např. správa uživatelů, update OS...
* **Uživatelské rozhraní** - prostředník mezi uživatelem a OS
  * Textové (příkazový řádek)
  * Grafické (okna, ikonky)
  * Umožňují spuštění programů a práci se soubory

## Druhy OS podle oblasti použití

* **Desktopové** - osobní počítače a notebooky
* **Serverové** - servery -> stabilita, bezpečnost, více uživatelů
* **Mobilní** - telefony a tablety -> dotykové ovládání, úspora energie
* **Vestavěné** - jednoúčelové zařízení -> spotřebiče, auta, průmysl

## Druhy OS podle počtu uživatelů

* **Jednouživatelské** - OS určen pro jednoho uživatele (Windows, macOS)
* **Víceuživatelské** - OS umožňuje práci více uživatelů současně (každý uživatel má vlastní účet a prostředí - např. Linux, serverové systémy)

## Druhy OS podle počtu úloh

* **Jednoúlohové** - OS umožňuje běh pouze jednoho programu v daný čas
* **Víceúlohové** - OS umožňuje běh více programů současně (procesor rychle přepíná mezi úlohami, uživatel má pocit, že běží současně)

## Příklady významných OS

* **Windows** - nejrozšířenější desktopový OS
* **Linux** - otevřený systém, často na serverech
* **macOS** - OS pro počítače Apple
* **iOS** - mobilní OS od Apple, uzavřený ekosystém
* **Android** - mobilní OS, založený na Linuxu

## Multitasking

Schopnost OS spouštět více programů současně (ve skutečnosti OS rychle přepíná procesor mezi úlohami).
* **Kooperativní** - programy si předávají řízení, nestabilní
* **Preemptivní** - OS přiděluje čas sám (lze nastavit priority)
  * Moderní OS používají preemptivní multitasking

## Přístupová práva a bezpečnost v OS

* OS umožňuje práci více uživatelů
* Každý uživatel má: účet, heslo, přístupová práva
* Rozdělení uživatelů: **administrátor, běžný uživatel**
* OS chrání: soubory, paměť, procesy
* Další bezpečnostní prvky: aktualizace, firewall, šifrování
* **Cíl**: zabránit zneužití, ochránit data i systém

## Práce se soubory

* **Soubor** = základní jednotka pro ukládání dat (text, program, obrázek...)
* Organizace souborů do **složek** (OS udržuje hierarchii)
* **Základní operace**: vytvoření, otevření, uložení, kopírování, čtení...
* Atributy a metadata - velikost, datum vytvoření, změny, read-only...
* Práva k souborům - OS "hlídá", kdo může soubor číst / upravovat / spouštět
* **Cesta k souboru**:
  * **Absolutní** - umístění souboru od úplného začátku:
    ```text
    C:\Users\Kuba\Documents\škola\poznámky.txt
    ```
  * **Relativní** - umístění souboru vzhledem k aktuální složce:
    ```text
    obrazky\graf.png
    ```

### Souborový systém

Způsob, jakým OS **ukládá a organizuje soubory na disku**.

* **Vytvoření** - OS zapíše do "evidence", že soubor existuje a přidělí mu místo na disku
* **Uložení** - data se zapíšou do přidělených bloků na disku + metadata se aktualizují
* **Otevření** - OS najde podle evidence, kde soubor leží a načte ho
* **Smazání** - OS odstraní záznam v evidenci a označí místo jako volné
* **Příklady**: NTFS (Windows), FAT32/exFAT (flash disky)

## Zdroje

* TANENBAUM, Andrew S. a Albert WOODHULL. *Operating systems: design and implementation: [the MINIX book]*. 3. ed. vyd. Upper Saddle River, NJ: Pearson Prentice Hall, 2006. The MINIX book. ISBN 978-0-13-142938-3.
* Informatika na Gymnáziu a Jazykové škole s právem státní jazykové zkoušky Zlín. In: [cit. 31.03.2026]. Dostupné z: [https://www.gjszlin.cz/ivt/esf/ostatni-sin/operacni-systemy-2.php](https://www.gjszlin.cz/ivt/esf/ostatni-sin/operacni-systemy-2.php)
* Jak na Internet - Operační systémy. In: [cit. 31.03.2026]. Dostupné z: [https://www.jaknainternet.cz/page/1757/operacni-systemy/](https://www.jaknainternet.cz/page/1757/operacni-systemy/)
* Operační systém. In: *Wikipedie* [online]. 2026 [cit. 31.03.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Opera%C4%8Dn%C3%AD_syst%C3%A9m&oldid=25745441](https://cs.wikipedia.org/w/index.php?title=Opera%C4%8Dn%C3%AD_syst%C3%A9m&oldid=25745441)
* Operační systémy – Umíme to. In: [cit. 31.03.2026]. Dostupné z: [https://www.umimeinformatiku.cz/cviceni-operacni-systemy](https://www.umimeinformatiku.cz/cviceni-operacni-systemy)
