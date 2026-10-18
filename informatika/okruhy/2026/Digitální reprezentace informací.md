# Digitální reprezentace informací

## Osnova

* Úvod
* Jednotky informace
* Binární soustava
* Reprezentace čísel
* Reprezentace textu
* Reprezentace obrazu
* Reprezentace zvuku
* Reprezentace videa
* Komprese dat
* Výhody a nevýhody digitální reprezentace

## Úvod

* Digitální reprezentace informací = **převod informací** do podoby, kterou **dokáže zpracovat počítač**
* Počítače pracují s čísly, konkrétně s **binární soustavou** (hodnoty 0 a 1)
* **Každá informace** – text, číslo, obrázek, zvuk nebo video – **uložena jako posloupnost bitů**

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
  * 1 kB = 1024 B
  * 1 MB = 1024 kB
  * 1 GB = 1024 MB
  * 1 TB = 1024 GB

## Binární soustava

* Počítače používají dvojkovou soustavu → dva stabilní stavy:
  * Proud teče → 1
  * Proud neteče → 0
* **Každé číslo lze převést do binární podoby** pomocí mocnin dvou
* Například číslo 13: 13₁₀ = 1101₂
* To znamená: 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 13

## Reprezentace čísel

### Celá čísla
* Ukládají se přímo v binární podobě
  * Například: 25₁₀ = 11001₂
* **Rozsah čísel závisí na počtu bitů:**
  * 8 bitů → 0–255
  * 16 bitů → 0–65535
* **Záporná čísla**
  * Používá se tzv. **doplňkový kód** (two’s complement)
  * Umožňuje jednodušší aritmetické operace

### Reálná čísla
* Používá se tzv. **pohyblivá desetinná čárka** (floating point) - standard IEEE 754
* **Číslo je rozděleno na:**
  * Znaménko
  * Exponent
  * Mantisu
* To umožňuje ukládat velmi velká i velmi malá čísla

## Reprezentace textu

* Text je uložen pomocí znakových sad
* **ASCII**
  * 7 bitů (128 znaků)
  * Obsahuje anglickou abecedu, číslice a speciální znaky
* **Rozšířené ASCII**
  * 8 bitů (256 znaků)
* **Unicode**
  * Umožňuje zápis znaků všech jazyků
  * Dnes nejpoužívanější kódování UTF-8

## Reprezentace obrazu

* Digitální **obraz je tvořen pixely** (obrazovými body)
* Každý pixel má uloženou svou **barvu v binární podobě**
* Udává počet pixelů (např. 1920 × 1080)
* **Vyšší rozlišení:**
  * Lepší kvalita
  * Větší velikost souboru

### Barevné modely
* **RGB**
  * Používá se na obrazovkách
  * Každá složka (R, G, B) má často 8 bitů (0–255)
  * Celkem tedy: 24 bitů na pixel → přes 16 milionů barev
* **Grayscale**
  * Pouze odstíny šedi
  * Menší datová náročnost

## Reprezentace zvuku

* Zvuk je původně **analogový signál**
* Pro zpracování počítačem musí být **převeden do digitální podoby**
* Tento proces se skládá z:
  * **Vzorkování (sampling)** – měření hodnoty zvuku v pravidelných intervalech (např. 44 100 vzorků za sekundu pro CD kvalitu)
  * **Kvantování** – každému vzorku je přiřazena číselná hodnota
* **Kvalita a velikost souboru:**
  * Čím vyšší vzorkovací frekvence a bitová hloubka (určuje přesnost záznamu), tím vyšší kvalita zvuku, ale větší velikost souboru

## Reprezentace videa

* Video je tvořeno:
  * Sérií obrázků (např. 30 fps, snímky uloženy jako digitální obraz)
  * Zvukovou stopou
* Kvůli velké velikosti se používají kodeky: H.264, MPEG, HEVC

## Komprese dat

* Komprese slouží ke zmenšení velikosti souborů
* **Bezztrátová komprese**
  * Nedochází ke ztrátě dat
  * Např. ZIP, PNG
* **Ztrátová komprese**
  * Část dat je odstraněna
  * Např. JPG, MP3
  * Používá se tam, kde malá ztráta kvality není poznat

## Výhody digitální reprezentace

* Snadné ukládání a kopírování
* Odolnost proti šumu
* Možnost šifrování
* Rychlý přenos
* Snadné zpracování algoritmy

## Nevýhody digitální reprezentace

* Nutnost převodu analog → digitál
* Velké objemy dat (např. video ve 4K)
* Nutnost komprese
* Možné chyby při přenosu
