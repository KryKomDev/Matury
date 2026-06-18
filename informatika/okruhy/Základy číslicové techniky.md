# Základy číslicové techniky

## Osnova

* Co to je
* Logické operace
  * Negace
  * Konjunkce
  * Disjunkce
  * Implikace
  * Ekvivalence
* Základní logické členy
  * Opakovač
  * NOT
  * AND
  * OR
  * NAND
  * NOR
  * XOR
  * XNOR
* Logické obvody
* Bonus: vnitřnosti logických členů

## Co to je

* Obor zabývající se zařízeními, která zpracovávají diskrétní nespojité signály.
  * Nejčastěji binární data.
  * Číslicový ampérmetr provádí měření a ukazuje číslo.
    * Nehrozí lidská chyba při odečtu jako u ručičky.
    * Může třeba převádět jednotky, data ukládat a dál s nimi pracovat.
    * $\rightarrow$ přesnější měření.
  * Analogové signály se musí převádět na číslicové signály.
    * Analogový obvod zpracuje signál.
    * Analogově-číslicový převodník převede do číslicového signálu.
      * Musí být dostatečný počet bitů.
    * Číslicové obvody zpracují číslicový signál.
* VS analogová technika zpracovává data spojitě.
  * Signál se během měření mění v čase (teplota, proud, ...).
  * Ručička ampérmetru ukazuje v danou vteřinu aktuální proud.
    * To je na stupnici.
    * Každý pozorovatel může odečíst jinou hodnotu – udělat chybu.
  * Analogové veličiny – spojitá funkce času.
    * Veličina mění hodnotu s časem / zůstává konstantní.
* Číslicový signál:
  * Označován jako dvojkový (binární).
    * Matematika: 1 / 0
    * Logika: pravda / nepravda
    * Elektrotechnika: různé napětí proti společné zemi.
      * Např. 0 je 0V / 1 je 5V.
      * Pokud je stav 1 reprezentován vyšším napětím (H) a stav 0 reprezentován nižším napětím (L), tak se jedná o **pozitivní logiku**.
      * Pokud je stav 1 reprezentován nižším napětím, tak se jedná o **negativní logiku**.
  * Jeden bit = 2 stavy.
    * Můžeme vyjádřit jen jestli je něco pravda / nepravda.
* Pokud potřebujeme víc stavů, musíme mít víc bitů.
  * Možných stavů přibývá exponenciálně v závislosti na počtu bitů:
    
    ![Bity a stavy](/informatika/assets/cislice/image1.png)
* Booleova algebra:
  * Matematický systém zabývající se logickými operacemi.
  * Binární proměnné.

## Logické operace

* **Unární** – pouze jeden operand (&not;x)
  * Negace:
    * &not;1 &hArr; 0
    * &not;svítí &hArr; nesvítí
* **Binární**
  * Konjunkce (&and;, AND, &&) = logický součin
    * 1 pokud platí oboje
  * Disjunkce (&or;, OR, ||) = logický součet
    * 1 pokud je pravda alespoň jeden výrok
  * Implikace (&rArr;)
    * Vztah vyplývání nebo zahrnutí.
    * 0 právě pokud je první výrok pravda a druhý nepravda.
  * Ekvivalence (&hArr;)
    * Pravda pokud mají oba výroky stejnou hodnotu.

### Pravdivostní tabulka

| A | B | A &and; B | A &or; B | A &rArr; B | A &hArr; B |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 1 | 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 | 0 |
| 0 | 0 | 0 | 0 | 1 | 1 |

## Základní logické členy

* Základní stavební prvky logických obvodů.
* Vyčísluje logickou funkci.
  
  ![Logický člen](/informatika/assets/cislice/image2.png)
  
  * Logický člen přijme vstup, vyčíslí funkci a vydá výstup.
* Logický člen = hradlo.
  * Komponenta v obvodu.
* Pomocí členů AND, OR a NOT lze realizovat jakýkoli logický obvod.
  * Členy AND a OR jsou pomocí členu NOT komplementární.
    * Vhodným způsobem je můžeme za sebe nahradit.
  * Jakýkoliv číslicový systém jde implementovat jen pomocí členů NAND nebo NOR nebo AND a NOT nebo OR a NOT.
    * Vždy stačí člen se dvěma vstupy.
    * Nejde to ale s členem XOR.
  * NAND a NOR = „univerzální logické členy“.
* Realizace zapojením vhodných součástek: tranzistory, diody, rezistory, ...
  * Z nich se poté tvoří logické obvody.
  * Existují i IMPLY a NIMPLY pro implikaci.

### Přehled hradel

#### Opakovač (repeater)
* Funkce identity: ![identity](/informatika/assets/cislice/image3.png)
* Použití: buffer – zpožďuje signál.
* Schéma:
  
  ![repeater schematic](/informatika/assets/cislice/image16.png)

#### NOT (invertor)
* Funkce logické negace: ![negation](/informatika/assets/cislice/image4.png)
* V programování: Q = !A
* Schéma:
  
  ![not schematic](/informatika/assets/cislice/image24.png)

#### AND (konjunktor)
* Funkce logického součinu = konjunkce: ![conjunction](/informatika/assets/cislice/image5.png)
* V programování: Q = A && B
* Schéma:
  
  ![and schematic](/informatika/assets/cislice/image18.png)

#### OR (disjunktor)
* Funkce logického součtu = disjunkce: ![disjunction](/informatika/assets/cislice/image6.png)
* V programování: Q = A || B
* Schéma:
  
  ![or schematic](/informatika/assets/cislice/image14.png)

#### NAND (Shefferova funkce)
* Funkce negovaného logického součinu: ![nand](/informatika/assets/cislice/image7.png)
* V programování: Q = !(A && B)
* Schéma:
  
  ![nand schematic](/informatika/assets/cislice/image19.png)

#### NOR (Perceova funkce)
* Funkce negovaného logického součtu: ![nor](/informatika/assets/cislice/image7.png)
* V programování: Q = !(A || B)
* Schéma:
  
  ![nor schematic](/informatika/assets/cislice/image17.png)

#### XOR (exkluzivní OR)
* Exkluzivní logický součet.
* Pravda jen když ![xor condition](/informatika/assets/cislice/image8.png) ([1, 0], [0, 1])
* Matematické vyjádření: ![xor math](/informatika/assets/cislice/image9.png)
* V programování: Q = A ^ B = (!A && B) || (A && !B)
* Schéma:
  
  ![xor schematic](/informatika/assets/cislice/image13.png)

#### XNOR (negace exkluzivního OR)
* Negace exkluzivního logického součtu.
* Pravda jen když A = B ([0, 0], [1, 1]).
* Matematické vyjádření: ![xnor math](/informatika/assets/cislice/image10.png)
* V programování: Q = !(A ^ B) = (A && B) || (!A && !B)
* Schéma:
  
  ![xnor schematic](/informatika/assets/cislice/image20.png)

## Logické obvody

* Pracuje s diskrétními stavy.
* Tvoří ho logické členy.
* Skládají se z nich číslicové systémy (zařízení pracující s daty v digitální podobě).
* Dělíme na:
  * **Kombinační**
    * Hodnoty výstupních proměnných jsou funkcí vstupních proměnných.
    * Záleží jen na kombinaci vstupních hodnot.
    * Příklady: binární sčítačka, kodér, dekodér, ...
  * **Sekvenční**
    * Nezáleží pouze na kombinaci vstupních hodnot, ale i na nějaké sekvenci předchozích vstupních hodnot.
    * Obvody mají paměť = vnitřní stav obvodu.
    * Příklady: CPU, ...

### Poloviční sčítačka

* Realizuje sčítání dvou jednobitových čísel.
* Vstup: sčítance A, B
* Výstup: S – součet, C – přenos do vyššího řádu
* Zvládá přenášet příznak do vyššího řádu, ale nedokáže zpracovat přenos z nižšího řádu.
  
  ![half adder schematic](/informatika/assets/cislice/image21.png)
  
  *Autor: en:User:Cburnett – Vlastní dílo Tento vektorový obrázek byl vytvořen programem Inkscape ., CC BY-SA 3.0, [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=1477592)*

| A (vstup) | B (vstup) | C (přenos) | S (součet) | číslo |
| :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | 00 |
| 0 | 1 | 0 | 1 | 01 |
| 1 | 0 | 0 | 1 | 01 |
| 1 | 1 | 1 | 0 | 10 |

### Úplná sčítačka

* Realizuje sčítání dvou jednobitových čísel s přihlédnutím k přenosu z nižšího řádu.
* Vstup:
  * sčítance A, B
  * příznak přenosu z nižšího řádu carry-in ($C_i$): ![carry-in](/informatika/assets/cislice/image11.png)
* Výstup:
  * součet S
  * příznak přenosu do vyššího řádu carry-out ($C_o$): ![carry-out](/informatika/assets/cislice/image12.png)
* 2 poloviční sčítačky + OR.
  * OR můžeme nahradit i XOR, protože [1, 1] nikdy nenastane.
    * pro sestavení úplné sčítačky tedy stačí jen 2 hradla.
* můžeme je řetězit ($C_o$ se propojí s $C_i$) &rarr; sčítání vícebitových čísel.
  
  ![full adder schematic](/informatika/assets/cislice/image25.png)

| $C_i$ (vstup) | B (vstup) | A (vstup) | $C_o$ (výstup) | S (výstup) |
| :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 1 |
| 0 | 1 | 0 | 0 | 1 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 1 |

## Bonus: vnitřnosti logických členů

* Tranzistorová či tranzistorovo-rezistorová implementace logických členů.

### NOT
![not transistor implementation](/informatika/assets/cislice/image15.png)
*By Tim Mathias - Own work, CC BY-SA 4.0, [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=94091301)*

### AND
![and transistor implementation](/informatika/assets/cislice/image22.png)
*By EBatlleP - Own work, CC BY-SA 3.0, [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=32544198)*

### OR
![or transistor implementation](/informatika/assets/cislice/image23.png)
*By EBatlleP - Own work, CC BY-SA 3.0, [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=32105652)*

## Zdroje

* PECINA, Mgr Pavel. Základy číslicové techniky.
* Binární sčítačka. In: *Wikipedie* [online]. 2025 [cit. 13.05.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Bin%C3%A1rn%C3%AD_s%C4%8D%C3%ADta%C4%8Dka&oldid=25378412](https://cs.wikipedia.org/w/index.php?title=Bin%C3%A1rn%C3%AD_s%C4%8D%C3%ADta%C4%8Dka&oldid=25378412)
* Booleova logika. In: *Wikipedie* [online]. 2025 [cit. 13.05.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Booleova_logika&oldid=25117538](https://cs.wikipedia.org/w/index.php?title=Booleova_logika&oldid=25117538)
* Číslicová technika. In: *Wikipedie* [online]. 2024 [cit. 13.05.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=%C4%8C%C3%ADslicov%C3%A1_technika&oldid=23884617](https://cs.wikipedia.org/w/index.php?title=%C4%8C%C3%ADslicov%C3%A1_technika&oldid=23884617)
* Disjunkce. In: *Wikipedie* [online]. 2026 [cit. 13.05.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Disjunkce&oldid=25677915](https://cs.wikipedia.org/w/index.php?title=Disjunkce&oldid=25677915)
* Ekvivalence (matematika). In: *Wikipedie* [online]. 2025 [cit. 13.05.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Ekvivalence_(matematika)&oldid=25070071](https://cs.wikipedia.org/w/index.php?title=Ekvivalence_(matematika)&oldid=25070071)
* Implikace. In: *Wikipedie* [online]. 2025 [cit. 13.05.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Implikace&oldid=25543876](https://cs.wikipedia.org/w/index.php?title=Implikace&oldid=25543876)
* Konjunkce (logika). In: *Wikipedie* [online]. 2022 [cit. 13.05.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Konjunkce_(logika)&oldid=21779255](https://cs.wikipedia.org/w/index.php?title=Konjunkce_(logika)&oldid=21779255)
* Logic gates unified symbols - Wikimedia Commons. In: [cit. 13.05.2026]. Dostupné z: [https://commons.wikimedia.org/wiki/Logic_gates_unified_symbols](https://commons.wikimedia.org/wiki/Logic_gates_unified_symbols)
* Logická operace. In: *Wikipedie* [online]. 2023 [cit. 13.05.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Logick%C3%A1_operace&oldid=22462587](https://cs.wikipedia.org/w/index.php?title=Logick%C3%A1_operace&oldid=22462587)
* Logický člen. In: *Wikipedie* [online]. 2025 [cit. 13.05.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Logick%C3%BD_%C4%8Dlen&oldid=25377993](https://cs.wikipedia.org/w/index.php?title=Logick%C3%BD_%C4%8Dlen&oldid=25377993)
* Logický obvod. In: *Wikipedie* [online]. 2025 [cit. 13.05.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Logick%C3%BD_obvod&oldid=24544951](https://cs.wikipedia.org/w/index.php?title=Logick%C3%BD_obvod&oldid=24544951)
