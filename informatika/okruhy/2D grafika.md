# 2D grafika

## Osnova

* Úvod
* Dělení – vektorová, rastrová
* Pixel a rozlišení
* Barevné modely
* Komprese
* Grafické operace
* Grafické programy
* Grafické tablety
* Využití 2D grafiky
* Výhody a nevýhody
* Moderní trendy

## Úvod

* Grafika zobrazovaná ve **dvou rozměrech** (šířka a výška).
* Neobsahuje třetí rozměr (na rozdíl od 3D grafiky).
* **Používá se**: na webu, v dokumentech, v reklamě, v grafických programech, na sociálních sítích.
* **Zobrazuje**: text, obraz, ilustrace, technické výkresy, grafy, fotografie.
* **Zobrazuje se na**: monitorech, displejích, projekčních plochách, papíru (po vytištění).

## Dělení

### Rastrová a bitmapová grafika

* Obraz is složen **mřížkou bodů – z pixelů** (bodů).
* Každý pixel má: **barvu, polohu, barevnou hloubku**.
* Čím více pixelů: obraz je detailnější, má vyšší kvalitu a větší velikost souboru.
* Slouží k zobrazování **obrázků a fotografií**.
* **Vlastnosti**:
  * Kvalita závisí na **rozlišení**.
  * Při zvětšení se obraz rozpadá = **pixelace**.
* **Výhody**: vhodná pro fotografie, realistické detaily.
* **Nevýhody**: velká velikost souboru, ztráta kvality při zvětšení, náročné na paměť.
* **Formáty**:
  * **JPG** – ztrátová komprese (ztráta kvality – redukuje barvy a sytost, jas se zanechává, fotografie).
  * **PNG** – bezztrátová komprese (podporuje průhlednost, vhodné pro web).
  * **BMP** – nekomprimovaný formát (data se ukládají po jednotlivých pixelech, velmi velké soubory, dnes se používá minimálně).
  * **GIF** – omezený počet barev, podpora animace.

### Vektorová grafika

* Obraz je tvořen pomocí **matematických objektů** (křivky, přímky, tvary, body).
* Ideální pro loga, grafiku a technické kresby.
* **Vlastnosti**:
  * Lze **libovolně zvětšovat bez ztráty kvality**.
  * Menší velikost souboru.
  * Snadná editace objektů.
* **Výhody**: ostré hrany při jakémkoliv zvětšení.
* **Nevýhody**: nelze upravovat fotografie.
* **Formáty**: **SVG**, AI, EPS, PDF (může obsahovat vektorovou grafiku).

## Pixel a rozlišení

* **Pixel** = nejmenší bod obrazu (obsahuje informaci o barvě).
* **Rozlišení** – počet pixelů v obrazu (např. 1920 × 1080) – čím větší, tím jemnější detaily. Vyšší rozlišení znamená lepší kvalitu, ale i větší velikost souboru.
* **DPI** (Dots Per Inch) – počet bodů na palec, určuje vizuální kvalitu především u tisku.
* **PPI** (Pixels Per Inch) – počet pixelů na palec, určuje kvalitu obrazu na displejích.
* **Barevná hloubka** – počet barev, které může pixel zobrazit (např. 8 bitů = 256 barev, 24 bitů = 16 milionů barev).

## Barevné modely

* Způsob, jak se **zapisují barvy**.
* **RGB** (Red, Green, Blue):
  * Používá se na obrazovkách.
  * Barvy vznikají kombinací světla (sčítací/aditivní metoda): červené, zelené a modré.
* **CMYK** (Cyan, Magenta, Yellow, Black):
  * Používá se při tisku.
  * Míchání barevných pigmentů (odčítací/subtraktivní metoda).
* **Grayscale** – odstíny šedi, používá se pro černobílý tisk.

## Komprese

* Zmenšení velikosti souboru.
* **Typy**:
  * **Bezztrátová** – neztrácí kvalitu (např. PNG).
  * **Ztrátová** – dochází ke ztrátě části dat výměnou za výraznější zmenšení (např. JPG).

## Grafické operace

* Základní úpravy: změna velikosti (resize), ořez (crop), rotace, úprava barev, filtry, jas a kontrast.

## Grafické programy

### Rastrové editory
* Umožňují **úpravy obrázků**.
* Pracují s pixely a **vrstvami** – ty oddělují jednotlivé části obrazu, takže jejich úprava je nezávislá.
* Výsledný obraz se exportuje do cílového formátu.
* **Příklady**: Adobe Photoshop, GIMP, Affinity Photo.

### Vektorové editory
* Pracují s **objekty**.
* Umožňují **přesné kreslení**.
* **Příklady**: Adobe Illustrator, Inkscape, Zoner Callisto.

## Grafické tablety

* Používají se při **digitální kresbě**.
* Umožňují **přesné ovládání**.
* Tlak pera ovlivňuje **tloušťku čáry**.

## Využití 2D grafiky

* Webdesign
* Reklama
* Tisk (plakáty, letáky)
* Hry
* Prezentace

## Výhody a nevýhody

### Výhody
* Jednoduchost.
* Široké využití.
* Dobrá kompatibilita.
* Snadná distribuce.

### Nevýhody
* **Rastrová grafika**: Ztráta kvality při zvětšení.
* **Vektorová grafika**:
  * Nevhodná pro fotografie.
  * Složitější tvorba realistických obrazů.
  * Může být náročnější na výkon počítače při složitých objektech.

## Moderní trendy

* **Flat design** – jednoduchý, bez stínů a 3D efektů, používá čisté tvary a výrazné barvy.
* **Minimalismus** – jednoduchost a odstranění všech zbytečných prvků.
* **Responzivní grafika** – automatické přizpůsobení velikosti grafiky displeji zařízení.
