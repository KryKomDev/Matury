# 3D grafika

## Osnova

* Základní informace
* Základní principy
* 3D model
* Typy 3D modelování
* Textury a materiály
* Světlo
* Kamera
* Rendering
* Animace
* Zobrazení 3D objektu na 2D obrazovce
* Výkon a hardware
* Formáty 3D souborů
* Programy
* Využití
* Výhody a nevýhody

## Základní informace

* Grafika zobrazovaná ve **třech rozměrech** (šířka, výška, hloubka).
* Používá souřadnice X, Y, Z.
* Vytváří **dojem prostoru a hloubky**.
* Umožňuje **realistické modelování** objektů.
* **Použití**: hry, filmy, animace, architektura, reklamy.

## Základní principy

3D grafika pracuje ve třech krocích:
1. **Modelování** – vytvoření 3D objektu.
2. **Texturování** – přidání povrchu (barva, materiál).
3. **Rendering** – výpočet finálního obrazu (vypočítání světla, stínů, odrazů).

## 3D model

* Je tvořen pomocí **vrcholů** (vertices), **hran** (edges) a **ploch** (faces, polygon).
* Nejčastěji se používají **trojúhelníky** (nejjednodušší stabilní plocha).
* Počet polygonů ovlivňuje detailnost a náročnost:
  * Čím více polygonů model obsahuje, tím je detailnější.
  * Vyšší počet polygonů je náročnější na výpočetní výkon.

## Typy 3D modelování

### Polygonální modelování
* Objekt je tvořen sítí **polygonů** (nejčastěji trojúhelníky nebo čtyřúhelníky).
* Polygonální síť (mesh) se skládá z vrcholů, hran a ploch.
* Ze základních geometrických tvarů se postupně vytvářejí složitější objekty.
* **Tvarování**: spočívá v dělení ploch na menší části, posouvání vrcholů a přidávání nových polygonů.
* **Výhody**:
  * Jednoduché vytváření.
  * Vhodné pro real-time rendering.
* **Nevýhody**:
  * Nízký počet polygonů způsobuje, že je objekt hranatý.
  * Vysoký počet polygonů výrazně zatěžuje grafickou kartu.
* **Použití**: nejčastější ve hrách, VR, filmových animacích (jednodušší modely).

### NURBS modelování
* Založeno na matematických křivkách a plochách.
* Povrch je vypočítáván podle matematických vzorců (nikoli z polygonů), což zajišťuje dokonale hladké plochy.
* **Výhody**: přesné tvary, hladké plochy, ideální pro technické návrhy.
* **Nevýhody**: složitější výpočty, při renderingu je často nutný převod do polygonů.
* **Použití**: architektura, letectví, automobilový průmysl.

### Sochařské modelování (sculpting)
* Digitální modelování, které je podobné práci s reálnou hlínou.
* **Tvarování**: spočívá v tahání, vyhlazování a přidávání virtuálního materiálu.
* Model může mít miliony polygonů a využívá se u něj dynamické rozdělování ploch.
* **Výhody**: vysoce realistické výsledky a vysoká úroveň detailů.
* **Nevýhody**: vysoké nároky na výkon, obrovský počet polygonů (často je nutná optimalizace pro hry).
* **Použití**: filmové nebo herní postavy, velmi detailní modely.

## Textury a materiály

* **Textura** – 2D obrázek aplikovaný na povrch 3D objektu (dodává barvu, vzor a detaily).
* **Materiál** – určuje chování povrchu vůči světlu (např. lesk, průhlednost, odrazivost).
* **UV mapování** – proces rozbalení 3D objektu do 2D plochy pro správné nanesení textury.

## Světlo

* Simuluje **reálné osvětlení**; bez světla model vypadá nepřirozeně.
* Vytváří stíny, odrazy a celkovou atmosféru scény (např. barvou světla).
* **Typy světel**:
  * **Bodové (point light)** – svítí z jednoho bodu do všech směrů, intenzita klesá se vzdáleností (např. lampy, svíčky, malé zdroje světla).
  * **Směrové (directional light)** – svítí jedním směrem, vzdálenost nehraje roli, vytváří ostré stíny (např. slunce, velmi vzdálené velké zdroje).
  * **Plošné (area light)** – svítí z určité plochy, vytváří měkčí a realističtější stíny, je výpočetně náročné (např. studiové osvětlení, filmové scény).

## Kamera

* Určuje **pohled na scénu**.
* Nastavuje se u ní úhel pohledu, vzdálenost a perspektiva.
* Může být **statická** nebo **animovaná** (pohyblivá).

## Rendering

* Proces **výpočtu finálního 2D obrazu** z 3D scény (velmi náročný na výkon).
* Vypočítává chování světla, stínů, odrazů a vlastnosti materiálů.
* **Typy renderingu**:
  * **Real-time rendering** – výpočet probíhá v reálném čase (např. u počítačových her).
  * **Offline rendering** – dlouhý a detailní výpočet jednoho snímku (např. u animovaných filmů).

## Animace

* Změna polohy, rotace nebo tvaru objektů v čase.
* **Metody animace**:
  * **Keyframing** – animace pomocí klíčových snímků.
  * **Motion capture** – snímání reálného pohybu herců a jeho převod na 3D model (např. filmy Polární expres, Avatar).
* **Využití**: filmy, hry, reklamy.

## Zobrazení 3D objektu na 2D obrazovce

* Používá se projekce (převod souřadnic z 3D prostoru na 2D plochu).
* **Typy projekce**:
  * **Perspektivní** – objekty v dálce se zdají být menší (přirozené pro lidské oko).
  * **Ortogonální** – bez perspektivy, objekty si zachovávají svou velikost bez ohledu na vzdálenost (používá se pro technické výkresy).

## Výkon a hardware

* 3D grafika je extrémně náročná na hardware.
* Klíčové komponenty:
  * **Procesor (CPU)** – zpracovává logiku scény, fyziku a v některých případech i offline rendering.
  * **Grafická karta (GPU)** – specializovaná jednotka pro rychlé grafické výpočty (např. real-time rendering).
* **Důležité technologie**:
  * **Ray tracing** – simulace realistického šíření a odrazu světelných paprsků.
  * **Shader** – program určující vzhled a vlastnosti povrchu objektu při dopadu světla.

## Formáty 3D souborů

* **OBJ** – univerzální formát pro 3D geometrii.
* **STL** – standardní formát využívaný především pro 3D tisk.
* **BLEND** – nativní formát programu Blender.
* **FBX** – formát pro přenos modelů, textur i animací mezi různými programy.

## Programy

* **Blender** – populární open-source program pro modelování, animaci i rendering.
* **Autodesk Maya** – profesionální průmyslový standard pro filmové a herní animace.
* **Cinema 4D** – oblíbený program pro motion design a vizualizace.
* **3ds Max** – nástroj často využívaný v herním průmyslu a architektuře.
* **ZBrush** – specializovaný program na digitální sculpting (sochařské modelování).

## Využití

* Počítačové hry
* Animované a trikové filmy
* Architektonické vizualizace
* Medicína (3D rekonstrukce orgánů)
* Průmyslový design a prototyping
* Virtuální realita (VR) a rozšířená realita (AR)

## Výhody a nevýhody

### Výhody
* Realistické zobrazení a věrná simulace prostoru.
* Interaktivita (možnost otáčení objektem, volba libovolného úhlu pohledu).
* Znovupoužitelnost modelů a snadná změna osvětlení či materiálů.

### Nevýhody
* Vysoké nároky na hardware (především na grafickou kartu).
* Složitější a časově náročnější tvorba modelů a scén.
* Dlouhý čas potřebný pro finální rendering (offline rendering).