# Informace a dvojková soustava

## Osnova

* Informace
* Jednotky informace
* Dvojková soustava
* Další číselné soustavy
* Kódování informací
* Digitalizace
* Výhody digitálního zpracování
* Přenos informací
* Chyby a zabezpečení

## Informace

* **Rozdíl mezi daty a informací:**
  * **Data** = surové hodnoty (čísla, znaky, symboly), např. číslo „25“
  * **Informace** = zpracovaná a interpretovaná data, např. „Teplota je 25 °C“
* **Analogová informace**
  * Spojitá, nabývá nekonečně mnoha hodnot -> věrné zachycení reality
  * Citlivost na šum a rušení -> zhoršení kvality při kopírování
  * Příklad: gramofonová deska, kazeta
* **Digitální informace**
  * Informace převedená do binární podoby
  * Snadné ukládání a přenos, možnost komprese
  * Kopírování bez ztráty kvality
  * Příklad: CD, DVD, počítače,…

## Jednotky informace

* **Bit** (binary digit)
  * Nejmenší jednotka informace
  * Může nabývat **hodnoty 0 nebo 1**
  * Reprezentuje dva stavy (ano/ne, zapnuto/vypnuto)
* **Byte**
  * **8 bitů**
  * Umožňuje zapsat **256 kombinací** (2⁸)
  * Používá se k **uložení jednoho znaku** (např. písmeno)
* **Vyšší jednotky**
  * 1 kB = 1000 B, ale 1 KiB = 1024 B – jednodušší na vyjádření ve dvojkové soustavě
  * 1 MB = 1000 kB, 1 MiB = 1024 KiB
  * 1 GB = 1000 MB, 1 GiB = 1024 MiB
  * 1 TB = 1000 GB, 1 TiB = 1024 GiB

## Dvojková soustava

* Základní jazyk počítačů
* Číselná soustava o základu 2
* Používá pouze číslice **0 a 1**
* **Proč počítače používají binární soustavu?**
  * Elektrické obvody mají dva stabilní stavy: proud teče (1), proud neteče (0)
  * Jednodušší a spolehlivější než více stavů
* **Převod z desítkové do dvojkové soustavy**
  * Princip: číslo dělíme dvěma, zapisujeme zbytky po dělení (0 nebo 1), čteme odzadu
  * Příklad: 13₁₀ = 1101₂
* **Převod z dvojkové do desítkové soustavy**
  * Používá se součet mocnin dvou:
  * 1101₂ = 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 8 + 4 + 0 + 1 = 13₁₀

## Další číselné soustavy

* **Osmičková** (základ 8) – číslice 0–7
* **Šestnáctková** (hexadecimální, základ 16)
  * Číslice 0–9 + A–F
  * Používá se pro: zápis barev (#FF0000), adresy v paměti, programování

## Kódování informací

* Počítač používá znakové sady:
* **ASCII**
  * 7 bitů
  * 128 znaků
  * Základní anglická abeceda + znaky
* **Unicode**
  * Umožňuje zápis znaků všech jazyků
  * Dnes standard UTF-8

## Digitalizace

* **Převod analogové informace na digitální**
* Probíhá ve třech krocích:
  1. **Vzorkování**
  2. **Kvantování**
  3. **Kódování**
* Příklad: mikrofon → zvuková karta → digitální zvuk

## Výhody digitálního zpracování

* Snadné ukládání a kopírování
* Rychlý přenos dat
* Odolnost proti šumu
* Možnost komprese

## Přenos informací

* Způsob, jakým se informace přenášejí mezi zařízeními
* **Informace se přenášejí jako:**
  * Elektrické signály
  * Optické impulzy (optický kabel)
  * Rádiové vlny (Wi-Fi)
* **Rychlost přenosu:**
  * Bit za sekundu (bps)
  * Např. 100 Mb/s

## Chyby a zabezpečení

* **Chyby při přenosu**
  * Šum
  * Rušení signálu
  * Ztráta dat
  * Kontrolní součty (CRC)
* **Šifrování**
  * Převod dat do nečitelné podoby
  * Používá se při internetové komunikaci (HTTPS)
