# Fotografie

## Osnova

* **Úvod a historický princip**
  * Camera obscura (dírková komora)
  * Podstata fotografického záznamu
* **Klasická vs. digitální fotografie**
  * Klasická fotografie (kinofilm, halogenidy stříbra, chemický proces, rozlišení)
  * Digitální fotografie (senzor, charakteristika, výhody a nevýhody)
  * Rozlišení a tisk (DPI, PPI, výpočty rozměrů pro tisk)
* **Konstrukce a typy fotoaparátů**
  * Rozdělení přístrojů (kompakty, bezzrcadlovky, digitální zrcadlovky DSLR)
  * Princip zrcadlovky (SLR/DSLR vs. bezzrcadlovka/EVF)
  * Snímače (CCD vs. CMOS, Fill factor, velikost buňky)
  * Záznam barev (Bayerova maska RGBG, interpolace)
  * Velikost snímače, Crop faktor a ekvivalentní ohnisko
* **Expozice a expoziční trojúhelník**
  * Pojem expozice, expoziční stupeň (EV)
  * Dynamický rozsah scény a médií
  * Histogram (podexpozice, přeexpozice)
  * Expoziční čas a závěrka (mechanická vs. elektronická, pohybová neostrost, panning, tepelný šum)
  * Clona a clonové číslo (světelnost, reciprocita)
  * Citlivost ISO a šum (zesílení signálu, redukce šumu)
  * Matematické vyjádření EV a expoziční tabulka
* **Měření expozice a expoziční režimy**
  * Metody měření expozice (celoplošné, se zdůrazněným středem, bodové, maticové)
  * Expoziční režimy (M, P, Tv/S, Av/A, scénické programy)
* **Zaostřování a hloubka ostrosti**
  * Rovina zaostření a rozptylový kroužek (CoC)
  * Definice hloubky ostrosti (DoF) a mezní hodnoty CoC pro různé snímače
  * Faktory ovlivňující hloubku ostrosti (clona, vzdálenost objektu, ohnisková vzdálenost, velikost čipu)
  * Hyperfokální vzdálenost a tlačítko náhledu hloubky ostrosti
  * Metody ostření (Fix fokus, Manuální ostření, Aktivní vs. Pasivní autofokus)
  * Funkce AF (dvoupolohová spoušť, AF lock, jednorázové vs. kontinuální ostření, asistence ve tmě)
  * Softwarové doostření (Sharpening)
* **Optika objektivu a vady zobrazení (aberace)**
  * Ohnisková vzdálenost (širokoúhlé, základní, teleobjektivy, optický vs. digitální zoom)
  * Geometrické vady objektivu (sférická vada, koma, astigmatismus, zklenutí obrazu, zkreslení)
  * Chromatická (barevná) vada
  * Vinětace (optická, mechanická a vinětace senzoru)
  * Vady digitálního snímače (blooming, šum)
* **Otázky a odpovědi k procvičení**

---

## Úvod a historický princip

* **Fotografie** (z řeckého *fós* = světlo a *grafé* = kresba/psaní) je proces zaznamenání trvalého obrazu pomocí světla.
* **Camera obscura (dírková komora)**:
  * Základní optické zařízení známé již ze starověku a renesance.
  * Tvořena světlotěsnou skříní (nebo zatemněnou místností) s malým kruhovým otvorem v jedné stěně.
  * Světelné paprsky procházející otvorem se kříží a na protější stěně vytvářejí **převrácený (stranově i výškově) a zmenšený obraz** vnější scény.
  * Moderní fotoaparát funguje na stejném základním geometrickém principu, otvor je však osazen soustavou čoček (**objektivem**) a obraz dopadá na citlivou záznamovou vrstvu (**kinofilm nebo digitální snímač**).

---

## Klasická vs. digitální fotografie

### Klasická (analogová) fotografie

* **Záznamové médium**: **kinofilm** (nebo svitkový/deskový film). Standardní kinofilmové políčko má rozměry **$24 \times 36\text{ mm}$** (z tohoto rozměru vychází označení *Full-frame*).
* **Princip záznamu**:
  * Film je pokryt světlocitlivou fotografickou emulzí – jemnými **krystalky halogenidů stříbra** (nejčastěji bromid stříbrný $\text{AgBr}$) rozptýlenými v želatině na pružném podkladu.
  * Při dopadu fotonů na krystalky dochází k fotochemické reakci a vzniku okem neviditelného **skrytého (latentního) obrazu**.
* **Chemické zpracování filmu (volání)**:
  1. **Vývojka**: chemický roztok, který přeměňuje exponované krystalky halogenidů stříbra na kovové černé stříbro (viditelný obraz).
  2. **Přerušovač (přerušovací lázeň)**: slabá kyselina (např. kyselina octová), která okamžitě neutralizuje zásaditou vývojku a zastaví proces vyvolávání.
  3. **Ustalovač**: roztok (např. thiosíran sodný), který rozpustí a vyplaví zbylé neosvětlené halogenidy stříbra; tím film znecitliví vůči světlu a obraz zafixuje.
  4. **Vyprání a usušení**: odstranění zbytků chemikálií čistou vodou.
* **Typy filmů**:
  * **Negativní film**: světlé části scény jsou na filmu tmavé a naopak; slouží k následnému kopírování/zvětšování na fotografický papír.
  * **Pozitivní film (diafilm / diapozitiv)**: po vyvolání vzniká přímo věrný pozitivní obraz vhodný pro promítání.
* **Rozlišovací schopnost filmu**:
  * Typický kinofilm rozliší cca **$130\text{ čar/mm}$**.
  * Plocha $24 \times 36\text{ mm}$ kinofilmu odpovídá po přepočtu digitálnímu rozlišení přibližně **8,6 až 14,6 MPix**.

### Digitální fotografie

* **Záznamové médium**: elektronický polovodičový obrazový snímač (**CCD nebo CMOS**).
* **Datová náročnost**:
  * Obraz se skládá z pixelů. Standardní 24bitová barevná hloubka využívá 3 bajty na pixel (RGB, 8 bitů pro každý kanál).
  * *Příklad*: nekomprimovaný 5 MPix snímek má datový objem $5 \times 10^6 \times 24\text{ bitů} = 120\text{ Mbit} \approx \mathbf{15\text{ MB}}$.
* **Výhody digitální fotografie**:
  * **Operativnost a okamžitá kontrola**: výsledek je ihned viditelný na displeji včetně histogramu.
  * **Digitální podoba**: data nepodléhají chemickému stárnutí, snadno se kopírují, zálohují a upravují v počítačových editorech.
  * **Opakovaná použitelnost média**: paměťové karty (SD, CFexpress apod.) lze opakovaně mazat a formátovat.
  * **Možnost změny ISO pro každý snímek zvlášť**: u filmu byla citlivost dána celým vloženým svitkem.
* **Nevýhody digitální fotografie**:
  * **Zpoždění spouště (shutter lag)**: doba potřebná pro přípravné operace elektroniky (vyhodnocení expozice, ostření, vyčištění senzoru).
  * **Závislost na elektrické energii**: nutnost nabíjení akumulátorů.
  * **Vznik digitálního šumu** při vysokých citlivostech ISO nebo dlouhých expozicích.
  * **Nutnost tisku**: pro fyzickou archivaci nebo prohlížení v ruce je nutné fotografii vytisknout.

### Rozlišení a tisková kvalita (DPI a PPI)

* **PPI (Pixels Per Inch)**: hustota obrazových bodů (pixelů) na jeden palec ($1\text{ palec} = 2{,}54\text{ cm}$) na zobrazovacích zařízeních (displejích).
  * Běžný starší monitor $1024 \times 768$ (úhlopříčka 17"): cca **90 PPI**.
  * Televize s úhlopříčkou 72 cm: cca **36 DPI**.
* **DPI (Dots Per Inch)**: počet tiskových bodů na jeden palec při tisku.
  * **300 DPI**: norma pro **špičkový, vysoce kvalitní tisk** fotografií (lidské oko z běžné čtecí vzdálenosti nerozezná jednotlivé body).
  * **150 DPI**: rozumná, běžně dostačující kvalita pro prohlížení z mírného odstupu.
  * **100 DPI**: absolutní přijatelné minimum.
  * **Klasická fotolaboratoř (minilab, formát $9 \times 13\text{ cm}$)**: dosahuje rozlišení až **690 DPI**.
* **Vzorec pro výpočet DPI z počtu pixelů a rozměru v centimetrech**:
  $$\text{DPI} = \frac{\text{počet pixelů}}{\text{rozměr v cm}} \times 2{,}54$$
  * *Příklad 1*: fotografie $9 \times 13\text{ cm}$ ze 6 Mpix fotoaparátu (cca 2000 px na kratší straně):
    $$\text{DPI} = \frac{2000}{9} \times 2{,}54 \approx \mathbf{565\text{ DPI}}$$
  * *Příklad 2*: fotografie $9 \times 13\text{ cm}$ ze 3 Mpix fotoaparátu (cca 1000 px na kratší straně):
    $$\text{DPI} = \frac{1000}{9} \times 2{,}54 \approx \mathbf{235\text{ DPI}}$$
  * *Příklad 3*: fotografie $18 \times 24\text{ cm}$ z fotoaparátu s 4,8 Mpix (např. $2530 \times 1900\text{ px}$):
    $$\text{DPI} = \frac{1900}{18} \times 2{,}54 \approx \mathbf{268\text{ DPI}}$$

#### Tabulka maximálních rozměrů fotografií podle rozlišení senzoru

| Rozlišení snímače | Typické rozlišení v pixelech | Max. rozměr při 300 DPI | Max. rozměr při 150 DPI |
| :--- | :--- | :--- | :--- |
| **2 Mpix** | $1600 \times 1200$ | $13 \times 10\text{ cm}$ | $26 \times 20\text{ cm}$ |
| **3 Mpix** | $2000 \times 1500$ | $17 \times 13\text{ cm}$ | $34 \times 26\text{ cm}$ |
| **4 Mpix** | $2500 \times 1600$ | $21 \times 14\text{ cm}$ | $42 \times 28\text{ cm}$ |
| **5 Mpix** | $2800 \times 1800$ | $24 \times 15\text{ cm}$ | $48 \times 30\text{ cm}$ |
| **6 Mpix** | $3000 \times 2000$ | $25 \times 17\text{ cm}$ | $50 \times 34\text{ cm}$ |
| **8 Mpix** | $3500 \times 2300$ | $30 \times 20\text{ cm}$ | $60 \times 40\text{ cm}$ |

---

## Konstrukce a typy fotoaparátů

### Kategorie digitálních fotoaparátů

1. **Základní přístroje a digitální hračky**: miniaturní senzory, jednoduchá optika, bez možnosti manuálního nastavení.
2. **Kompakty pro nenáročné amatéry**: malé rozměry, univerzální zoom objektiv bez možnosti výměny, plná automatika.
3. **Kompakty střední třídy**: lepší světelnost, pokročilejší expoziční režimy (P, Tv, Av, M).
4. **Hi-end kompakty**: větší senzory (např. 1" nebo APS-C), vysoce světelné objektivy, záznam do formátu RAW.
5. **Digitální zrcadlovky (DSLR) pro pokročilé amatéry**: výměnné objektivy, optický hledáček, velký senzor (APS-C).
6. **Profesionální zrcadlovky a bezzrcadlovky**: full-frame senzory, robustní těla chráněná proti povětrnostním vlivům, vysoká rychlost snímání a spolehlivost.

### Zrcadlovky vs. bezzrcadlovky

```text
DSLR (Digitální zrcadlovka):
Objektiv ──> Sklopné zrcátko (45°) ──[odraz nahoru]──> Matnice ──> Pětiboký hranol ──> Optický hledáček
                     │ (při expozici se zvedne)
                     └──> Závěrka ──> Snímač (senzor)

Bezzrcadlovka (EVF / SLR-like):
Objektiv ──> Závěrka ──> Snímač (trvalý chod) ──[elektronika]──> Displej / EVF hledáček
```

* **DSLR (Digital Single Lens Reflex) – digitální pravá jednooká zrcadlovka**:
  * Světlo prochází objektivem a odráží se od **sklopného zrcátka** nahoru na matnici a přes **optický hranol (pentaprism)** do **optického hledáčku**.
  * Fotograf vidí scénu v reálném čase, opticky čistou, bez jakéhokoliv zpoždění a bez spotřeby energie.
  * Při stisku spouště se zrcátko sklopí nahoru, otevře se mechanická závěrka a světlo exponuje senzor. Po expozici se závěrka zavře a zrcátko sklopí zpět (typické „cvaknutí“).
* **Bezzrcadlovka (SLR-like, Mirrorless, EVF)**:
  * Nemá žádné zrcátko ani optický hranol. Světlo dopadá přímo na hlavní snímač.
  * Obraz je neustále vyčítán a promítán na zadní displej nebo do malého displeje v hledáčku (**EVF – Electronic Viewfinder**).
  * **Výhody**: menší rozměry a hmotnost těla, možnost zobrazit reálný náhled expozice, vyvážení bílé, histogram i přepaly přímo před expozicí.
  * **Nevýhody podle prezentace**:
    * Hrubší rozlišení starších EVF hledáčků ztěžuje precizní manuální ostření.
    * Mírné elektronické **zpoždění obrazu** (lag).
    * Vyšší spotřeba elektrické energie (displej i senzor musí běžet nepřetržitě).

### Obrazové snímače (CCD vs. CMOS)

Digitální snímač se skládá z milionů samostatných buněk (fotodiod), které mění dopadající fotony na elektrický náboj.

* **CCD (Charge-Coupled Device)**:
  * Náboj z jednotlivých fotodiod se po řádcích posouvá přes analogové posuvné registry ke společnému zesilovači a externímu A/D převodníku.
  * **Vlastnosti**: nižší šum, vyšší rovnoměrnost a čistota obrazu; nevýhodou je vyšší spotřeba energie, pomalejší vyčítání a vyšší výrobní náklady.
* **CMOS (Complementary Metal-Oxide-Semiconductor)**:
  * Každá buňka obsahuje kromě fotodiody i **vlastní tranzistorový zesilovač**.
  * Buňky se adresují maticově po řádcích a sloupcích (X, Y) jako u pamětí RAM.
  * **Vlastnosti**: velmi nízká spotřeba energie, vysoká rychlost odečtu dat (umožňuje rychlé sériové snímání i video), nízké výrobní náklady.
  * **Nevýhoda**: integrované tranzistory zabírají část plochy buňky na úkor fotodiody.

#### Fill factor (činitel zaplnění)

* **Definice**: poměr citlivé plochy fotodiody k celkové ploše buňky:
  $$\text{Fill factor} = \frac{\text{citlivá plocha fotodiody}}{\text{celková plocha buňky}}$$
* Protože podpůrná elektronika u CMOS ubírá světlocitlivou plochu, umisťují se nad každou buňku **mikroobjektivy (mikročočky)**, které soustředí dopadající světlo z celé plochy buňky přímo na fotodiodu.

#### Fyzická velikost buňky a její vliv

* Velikost buňky se počítá jako poměr fyzického rozměru čipu a rozlišení:
  $$\text{Velikost buňky} = \frac{\text{šířka senzoru v mm}}{\text{horizontální rozlišení}}$$
  * *Příklad 1 (APS-C DSLR)*: senzor $22{,}3 \times 14{,}9\text{ mm}$ při rozlišení $4752 \times 3168$ (15 Mpix) má buňku o hraně **$4{,}7\ \mu\text{m}$**.
  * *Příklad 2 (kompakt 1/2.5")*: senzor $5{,}75 \times 4{,}31\text{ mm}$ při rozlišení $3072 \times 2304$ (7 Mpix) má buňku o hraně pouhých **$1{,}9\ \mu\text{m}$**.
* **Důsledek velikosti buňky**: větší buňka zachytí výrazně více fotonů, má vyšší kapacitu náboje, lepší odstup signálu od šumu a větší dynamický rozsah. Miniaturní buňky na malých senzorech trpí vysokým šumem.

### Snímání barev – Bayerova maska

* Samotný křemíkový fotodetektor je **barvoslepý** – reaguje pouze na počet dopadlých fotonů bez ohledu na jejich barvu (vlnovou délku).
* Aby vznikl barevný obraz, je před snímač předřazena mozaika barevných mikrofiltrů – **Bayerova maska (RGBG / RGGB)**:
  * Skládá se ze střídajících se filtrů červené (R), zelené (G) a modré (B).
  * **Zelených buněk je 50 %**, červených 25 % a modrých 25 %. Dvojnásobné zastoupení zelené barvy odpovídá biologické citlivosti lidského oka, které je nejcitlivější na zelené světlo a vnímá v něm jasovou složku (luminanci).
  * *Příklad*: 6 Mpix senzor má 3 miliony zelených buněk, 1,5 milionu červených a 1,5 milionu modrých.
* **Interpolace (demosaicing)**: chybějící dvě barevné složky pro každý jednotlivý pixel se matematicky dopočítávají ze sousedních pixelů v procesoru fotoaparátu.
* **Barevná hloubka**: 8 bitů na kanál (256 úrovní) pro R, G i B dává dohromady $256 \times 256 \times 256 = \mathbf{16\,777\,216\text{ barev}}$ (24bitová hloubka, True Color).

---

## Velikost snímače, Crop faktor a optika

### Formáty senzorů

* **Full-frame (kinofilmové políčko)**: rozměr $24 \times 36\text{ mm}$, délka úhlopříčky $43{,}3\text{ mm}$.
* **APS-C (Nikon DX, Sony E)**: rozměr cca $23{,}6 \times 15{,}8\text{ mm}$, úhlopříčka cca $28{,}4\text{ mm}$.
* **APS-C (Canon)**: rozměr cca $22{,}3 \times 14{,}9\text{ mm}$, úhlopříčka cca $26{,}8\text{ mm}$.
* **Senzory kompaktů**: značeny historicky ve zlomcích palce podle průměru snímacích elektronek vidikonu (např. 1/1.8", 1/2.5"). Reálná úhlopříčka senzoru odpovídá přibližně jen **dvěma třetinám udané hodnoty zlomku** (např. 1/2.5" má úhlopříčku cca $7{,}2\text{ mm}$).

### Crop faktor

* **Crop faktor (ořezový faktor)** udává poměr úhlopříčky referenčního kinofilmového políčka ($24 \times 36\text{ mm}$) k úhlopříčce daného menšího snímače:
  $$\text{Crop faktor} = \frac{\text{úhlopříčka kinofilmu }(43{,}3\text{ mm})}{\text{úhlopříčka senzoru v mm}}$$
  * APS-C (Nikon DX, Sony): $\frac{43{,}3}{28{,}4} \approx \mathbf{1{,}5}$
  * APS-C (Canon): $\frac{43{,}3}{26{,}8} \approx \mathbf{1{,}6}$
  * Kompakty: crop faktor bývá $4\times$ až $6\times$.
* Menší senzor vyřízne z obrazového kruhu promítaného objektivem pouze menší středovou část – zorný úhel se zmenší (obraz vypadá jako přiblížený).

### Ekvivalentní ohnisková vzdálenost

* Abychom mohli porovnávat úhly záběru objektivů na různých tělech, přepočítává se fyzická ohnisková vzdálenost pomocí Crop faktoru na ekvivalent pro kinofilm:
  $$\text{Ekvivalentní ohnisko} = \text{skutečné ohnisko }(f) \times \text{Crop faktor}$$
  * *Příklad 1*: objektiv $50\text{ mm}$ na APS-C těle s cropem $1{,}5$ má zorný úhel odpovídající objektivu **$75\text{ mm}$** na full-frame těle ($50 \times 1{,}5 = 75\text{ mm}$).
  * *Příklad 2*: objektiv $28\text{ mm}$ na APS-C těle ($1{,}5\times$) odpovídá **$42\text{ mm}$** na kinofilmu ($28 \times 1{,}5 = 42\text{ mm}$).

### Rozdělení objektivů podle ohniskové vzdálenosti (přepočteno na kinofilm)

* **Základní (standardní) objektiv**: ohnisko cca **$50\text{ mm}$**. Zorný úhel (cca 45–50°) a perspektiva odpovídají zornému poli lidského oka.
* **Širokoúhlý objektiv**: ohnisko **menší než $50\text{ mm}$** (např. 14–35 mm). Široký zorný úhel, zdůrazňuje popředí a opticky rozšiřuje prostor (krajina, architektura, interiéry).
* **Teleobjektiv**: ohnisko **větší než $50\text{ mm}$** (např. 70–300 mm a více). Úzký zorný úhel, opticky stlačuje perspektivu a přibližuje vzdálené objekty (sport, zvířata, portréty).
* **Zoom objektiv**: objektiv s proměnnou ohniskovou vzdáleností (např. 18–55 mm, 70–200 mm).
* **Digitální zoom**: nejedná se o optické přiblížení, ale o pouhý **výřez ze středu snímku a jeho softwarové roztažení (interpolaci)** na plné rozlišení. Způsobuje výraznou ztrátu detailů a ostrosti – **jeho použití se nedoporučuje**.

---

## Expozice a expoziční trojúhelník

* **Expozice**: celkové množství světelné energie, které dopadne na film nebo digitální senzor během fotografování.
* **Expoziční trojúhelník**: expozice je dána vzájemnou kombinací tří parametrů:
  1. **Expoziční čas** (doba, po kterou je senzor vystaven světlu)
  2. **Clona** (velikost otvoru, kterým světlo prochází)
  3. **Citlivost ISO** (míra zesílení signálu ze senzoru)

```text
                       [Expoziční čas]
                     (pohybová ostrost)
                            /\
                           /  \
                          /    \
                         /      \
                        /________\
             [Clona]                  [ISO]
        (hloubka ostrosti)            (šum)
```

### Expoziční stupeň (EV – Exposure Value)

* **EV** je logaritmická jednotka pro měření množství světla scény a nastavení expozice.
* **Změna o $1\text{ EV}$** znamená **zdvojnásobení nebo rozpůlení** množství světla dopadajícího na záznamové médium.
* Definice nuly: **$0\text{ EV}$** odpovídá expozici času **$t = 1\text{ s}$** při cloně **$f/1{,}0$** a citlivosti **$\text{ISO } 100$**.

#### Typické hodnoty EV v praxi

| EV hodnota | Typická světelná situace |
| :--- | :--- |
| **$-6$ až $-2\text{ EV}$** | Hluboká noc daleko od civilizace, scéna osvětlena jen hvězdami či měsícem |
| **$-1$ až $1\text{ EV}$** | Noční krajina s osvětleným městem v dálce |
| **$2$ až $5\text{ EV}$** | Scéna osvětlená svíčkami, spoře osvětlená noční ulice |
| **$5$ až $7\text{ EV}$** | Spoře osvětlené interiéry (kostely, divadla), noční silně osvětlená ulice |
| **$7$ až $8\text{ EV}$** | Běžně osvětlené interiéry, sportovní haly, nákupní centra, hluboký les |
| **$9$ až $11\text{ EV}$** | Východ a západ slunce, zamračená denní krajina, stín za slunného dne |
| **$12$ až $13\text{ EV}$** | Světlý den s lehkou oblačností, jarní slunný opar |
| **$14$ až $16\text{ EV}$** | Jasný, přímý slunný letní den |
| **$17\text{ EV}$ a více** | Extrémní světlo v přírodě (sníh/ledovce na slunci), silné bodové reflektory |

### Dynamický rozsah a histogram

* **Dynamický rozsah**: poměr mezi nejjasnějším a nejtmavším odstínem scény, které je médium schopno zaznamenat současně bez ztráty kresby.
  * **Lidské oko**: v jedné scéně $11\text{ až }15\text{ EV}$, s adaptací zornice až **$30\text{ EV}$** (kontrastní poměr až $1 : 20\,000$).
  * **Kinofilm**: $6\text{ až }7\text{ EV}$ (negativ až $7\text{ až }8\text{ EV}$ s pozvolnou „S“ charakteristikou v jasech i stínech).
  * **Digitální fotoaparáty**: starší/běžné kompakty $4\text{ až }7\text{ EV}$, moderní a profesionální zrcadlovky $7\text{ až }8+\text{ EV}$ (kontrast čipu cca $1 : 600$).
* **Limitace senzoru**: shora je dán kapacitou buňky (při zaplnění fotodiody náboj přeteče – vznikne bílý přepal), zdola je dán úrovní vlastního šumu buňky (slabý signál zanikne v šumu).
* **Histogram**: grafické znázornění rozložení jasových tónů na fotografii:
  * Osa X znázorňuje jas od nejtmavší černé (hodnota 0 vlevo) po nejjasnější bílou (hodnota 255 vpravo).
  * Osa Y znázorňuje počet pixelů s daným jasem.
  * **Podexponování (tmavý snímek)**: histogram je posunutý doleva a naráží do levého okraje. Dochází ke slití stínů do čisté černé bez detailů.
  * **Přeexponování (přesvětlený snímek)**: histogram je posunutý doprava a naráží do pravého okraje. Vznikají **přepaly** (čistě bílé plochy bez kresby).
  * **Správná expozice**: tóny jsou rozprostřeny v ploše grafu bez ořezu na okrajích.

---

## Prvky expozičního trojúhelníku

### 1. Expoziční čas a závěrka

* **Expoziční čas**: doba, po kterou závěrka umožňuje světlu dopadat na senzor/film.
* **Typy závěrek**:
  * **Mechanická závěrka**: lamelová štěrbinová závěrka umístěná před senzorem, mechanicky odkrývá a zakrývá plochu čipu.
  * **Elektronická závěrka**: senzor je trvale odkryt, expozice je řízena zapnutím a vypnutím sběru náboje v buňkách. Umožňuje extrémně krátké časy (např. 1/4000 s až 1/32000 s) a zcela tichý provoz.
* **Standardní řada expozičních časů** (každý krok mění množství světla na polovinu/dvojnásobek, tj. o 1 EV):
  $$1\text{ s} \quad \frac{1}{2}\text{ s} \quad \frac{1}{4}\text{ s} \quad \frac{1}{8}\text{ s} \quad \frac{1}{15}\text{ s} \quad \frac{1}{30}\text{ s} \quad \frac{1}{60}\text{ s} \quad \frac{1}{125}\text{ s} \quad \frac{1}{250}\text{ s} \quad \frac{1}{500}\text{ s} \quad \frac{1}{1000}\text{ s} \quad \frac{1}{2000}\text{ s}$$
* **Důsledky volby času**:
  * **Rozhýbání snímku vlivem chvění rukou**:
    * Bezpečný čas pro udržení fotoaparátu z ruky bez rozmazání je dán převrácenou hodnotou přepočtené ohniskové vzdálenosti:
      $$t_{\text{bezpečný}} \le \frac{1}{f \times \text{Crop faktor}}$$
    * *Příklad*: pro ohnisko $200\text{ mm}$ na APS-C fotoaparátu ($1{,}6\times$) je bezpečný čas:
      $$t \le \frac{1}{200 \times 1{,}6} = \frac{1}{320}\text{ s}$$
  * **Pohybová neostrost**: rychlý pohyb vyžaduje krátký čas pro „zmrazení“ (např. 1/1000 s pro sport), dlouhý čas pohyb záměrně rozmaže (např. tekoucí voda).
  * **Panning (švenkování)**: fotograf sleduje fotoaparátem pohybující se objekt při delším času (např. 1/30 až 1/60 s). Objekt zůstává ostrý, zatímco pozadí je rozmazané šmouhami ve směru pohybu, což vytváří silnou iluzi rychlosti.
  * **Tepelný šum při dlouhých časech (> 1 s, Dark current noise)**:
    * Dlouhou expozicí se senzor zahřívá a tepelný pohyb uvolňuje náhodné elektrony i v naprosté tmě.
    * **Redukce šumu dlouhé expozice (Long Exposure Noise Reduction)**: fotoaparát po skončení expozice provede druhou, stejně dlouhou expozici se zavřenou závěrkou (tzv. *Dark frame* – snímek temného proudu), změří samotný tepelný šum a odečte ho od pořízeného snímku. Proces trvá dvojnásobek expozičního času.

### 2. Clona a clonové číslo

* **Clona**: irisový kruhový otvor proměnlivého průměru tvořený lamelami uvnitř objektivu.
* Množství procházejícího světla je úměrné **ploše kruhového otvoru** ($S = \pi r^2 = \pi \frac{D^2}{4}$).
  * Aby se plocha otvoru zdvojnásobila (propustila $2\times$ více světla), musí se průměr otvoru zvětšit $\sqrt{2} \approx \mathbf{1{,}414\times}$.
* **Clonové číslo ($F$)**: poměr ohniskové vzdálenosti objektivu ($f$) k účinnému průměru vstupního otvoru clony ($D$):
  $$F = \frac{f}{D} \implies D = \frac{f}{F}$$
* **Standardní řada clonových čísel** (násobky $\sqrt{2} \approx 1{,}4$):
  $$f/1{,}0 \quad f/1{,}4 \quad f/2{,}0 \quad f/2{,}8 \quad f/4{,}0 \quad f/5{,}6 \quad f/8 \quad f/11 \quad f/16 \quad f/22 \quad f/32$$
  * **Čím vyšší clonové číslo, tím menší otvor a méně světla!**
  * Přechod na nejbližší vyšší clonové číslo propustí přesně **polovinu světla** ($-1\text{ EV}$).
* **Světelnost objektivu**: minimální clonové číslo, které objektiv umožňuje nastavit (plně otevřená clona).
  * *Příklad*: objektiv $f = 200\text{ mm}$ se světelností $f/4$ má maximální průměr clony $D = \frac{200}{4} = \mathbf{50\text{ mm}}$.
  * U objektivu $f = 300\text{ mm}$ při cloně $f/4$ je průměr $D = \frac{300}{4} = \mathbf{75\text{ mm}}$.
  * U objektivu $f = 20\text{ mm}$ při cloně $f/4$ je průměr $D = \frac{20}{4} = \mathbf{5\text{ mm}}$.
* **Zákon vzájemnosti (reciprocita expozice)**:
  * Různé kombinace času a clony mohou propustit stejné celkové množství světla:
  * *Příklad*: $\frac{1}{25}\text{ s}$ při cloně $f/8$ dá **stejnou expozici** jako $\frac{1}{50}\text{ s}$ při cloně $f/5{,}6$.

### 3. Citlivost ISO a digitální šum

* **ISO citlivost**:
  * U klasické fotografie vyjadřuje chemickou citlivost filmové emulze.
  * U digitální fotografie představuje **elektronické zesílení signálu** z fotodiod senzoru.
* **Stupnice citlivosti ISO**:
  $$50 \quad 100 \quad 200 \quad 400 \quad 800 \quad 1600 \quad 3200 \quad 6400 \quad 12800$$
  * Zdvojnásobení ISO hodnoty znamená zisk $+1\text{ EV}$ – umožní použít poloviční expoziční čas nebo o stupeň vyšší clonu.
* **Digitální šum**:
  * Protože se při zvýšení ISO signál zesiluje, **zesiluje se společně s ním i šum** pozadí (poměr signál/šum klesá).
  * **Příčina šumu**: tepelný pohyb atomů v krystalové mřížce polovodiče uvolňuje náhodné falešné elektrony. Nelze jej stoprocentně odstranit.
  * **Projevy šumu**:
    * Náhodné barevné body v obraze (chromatický šum).
    * Ztráta kontrastu a rozmazání jemných hran.
    * Pokles ostrosti a mikrokontrastu (tzv. brizance).
  * **Softwarové odšumování ve fotoaparátu / editoru**: šum potlačuje rozostřením barevných kanálů a sléváním ploch, což vede ke „žehlení“ detailů a ztrátě kresby.

---

## Matematické vyjádření EV a expoziční tabulka

Hodnotu expozice lze exaktně vyjádřit pomocí dvojkového logaritmu z clonového čísla ($F$), expozičního času v sekundách ($t$) a citlivosti ($\text{ISO}$):

$$EV = \log_2\left(\frac{F^2}{t}\right) - \log_2\left(\frac{\text{ISO}}{100}\right) = 2 \cdot \log_2 F - \log_2 t - \log_2\left(\frac{\text{ISO}}{100}\right)$$

Alternativní součinový zápis:
$$2^{EV} = \frac{F^2}{t} \cdot \frac{100}{\text{ISO}}$$

### Expoziční tabulka přírůstků EV

Výsledná hodnota expozice je dána součtem dílčích přírůstků:
$$EV = \Delta EV_{\text{čas}} + \Delta EV_{\text{clona}} + \Delta EV_{\text{ISO}}$$

| Hodnota indexu | Expoziční čas $t$ [s] | Přírůstek EV (čas) | Clonové číslo $F$ | Přírůstek EV (clona) | Citlivost ISO | Přírůstek EV (ISO) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0** | $1$ | $0$ | $1{,}0$ | $0$ | $100$ | $0$ |
| **1** | $1/2$ | $+1$ | $1{,}4$ | $+1$ | $50$ | $+1$ |
| **2** | $1/4$ | $+2$ | $2{,}0$ | $+2$ | $200$ | $-1$ |
| **3** | $1/8$ | $+3$ | $2{,}8$ | $+3$ | $400$ | $-2$ |
| **4** | $1/15$ | $+4$ | $4{,}0$ | $+4$ | $800$ | $-3$ |
| **5** | $1/30$ | $+5$ | $5{,}6$ | $+5$ | $1600$ | $-4$ |
| **6** | $1/60$ | $+6$ | $8{,}0$ | $+6$ | $3200$ | $-5$ |
| **7** | $1/125$ | $+7$ | $11{,}0$ | $+7$ | $6400$ | $-6$ |
| **8** | $1/250$ | $+8$ | $16{,}0$ | $+8$ | $12800$ | $-7$ |
| **9** | $1/500$ | $+9$ | $22{,}0$ | $+9$ | — | — |
| **10** | $1/1000$ | $+10$ | $32{,}0$ | $+10$ | — | — |
| **11** | $1/2000$ | $+11$ | $45{,}0$ | $+11$ | — | — |

*Příklad výpočtu*: Pro čas $t = 1/60\text{ s}$ ($\Delta EV = +6$), clonu $f/8$ ($\Delta EV = +6$) a citlivost $\text{ISO } 400$ ($\Delta EV = -2$):
$$EV = 6 + 6 + (-2) = \mathbf{10\text{ EV}}$$

---

## Měření expozice a expoziční režimy

### Metody měření expozice

Fotoaparáty měří **světlo odražené od fotografované scény** (vestavěným expozimetrem). Měření je kalibrováno na průměrnou odrazivost scény odpovídající **18% střední šedé**.

1. **Celoplošné integrální měření**:
   * Měří světlo rovnoměrně z celého obrazového pole.
2. **Integrální se zdůrazněným středem (Center-weighted)**:
   * Měří celé pole, ale středu obrazu (cca 60–80 % váhy) přisuzuje nejvyšší prioritu. Vhodné pro standardní podmínky.
3. **Bodové měření (Spot metering)**:
   * Měří expozici pouze z velmi malé plochy (typicky **1 % až 2 %** plochy uprostřed nebo v aktivním ostřícím bodě).
   * Vhodné pro scény s extrémním kontrastem, protisvětlem nebo při divadelní fotografii.
4. **Středové částečné měření (Partial)**:
   * Měří plochu cca **8 % až 10 %** ve středu záběru.
5. **Maticové / zónové měření (Matrix / Evaluative)**:
   * Scéna je rozdělena na síť zón (desítky až stovky segmentů).
   * Procesor porovnává jasové poměry, barvy a zaostřenou vzdálenost s interní databází typických scén a zvolí optimální expozici. Běžný výchozí režim moderních fotoaparátů.

### Expoziční režimy fotoaparátu

* **M (Manual – plně manuální režim)**:
  * Fotograf ručně nastavuje expoziční čas, clonu i citlivost ISO. Fotoaparát pouze ukazuje odchylku na stupnici expozimetru.
* **P (Programová automatika – poloautomatický režim)**:
  * Fotograf nastavuje ISO, fotoaparát automaticky dopočítává kombinaci času a clony (lze provádět programový posuv).
* **Tv / S (Time value / Shutter priority – priorita času)**:
  * Fotograf volí expoziční čas (a ISO), fotoaparát dopočítá clonu. Vhodné pro pohybující se objekty (sport, tekoucí voda, panning).
* **Av / A (Aperture value – priorita clony)**:
  * Fotograf volí clonu (a ISO), fotoaparát dopočítá expoziční čas. Klíčový režim pro **kontrolu hloubky ostrosti** (portrét, krajina, makro).
* **Kreativní / scénické režimy**:
  * Plně automatické režimy přizpůsobené konkrétnímu žánru: Portrét (malá clona pro rozostření pozadí), Krajina (velká clona pro ostré celé pole), Sport (krátký čas), Makro (ostření na blízko).

---

## Zaostřování a hloubka ostrosti

### Rovina zaostření a rozptylový kroužek (CoC)

* **Rovina zaostření (Focal plane)**: geometrická rovina v prostoru před objektivem, na kterou je objektiv přesně zaostřen.
  * Světelné paprsky vycházející z bodu v rovině zaostření se na senzoru protnou přesně v jednom bodě.
* **Rozptylový kroužek (Circle of Confusion – CoC)**:
  * Paprsky z bodu, který leží před nebo za rovinou zaostření, se na senzoru neprotnou v bodě, ale vytvoří kužel světla dopadající jako **rozostřený kroužek (ploška)**.
  * Dokud je průměr tohoto kroužku menší než rozlišovací schopnost lidského oka na výsledné fotografii, vnímá oko tento bod jako **ostrý**.

```
Objekt mimo rovinu ──> Objektiv ──> Světelný kužel ──> Senzor ──> [Rozptylový kroužek CoC]
```

### Definice hloubky ostrosti (DoF – Depth of Field)

* **Hloubka ostrosti**: pásmo prostoru před a za rovinou zaostření, ve kterém se objekty na výsledném obraze jeví lidskému oku jako přijatelně ostré.
* **Oficiální technická norma pro výpočet CoC**:
  * Povolena je taková odchylka od roviny zaostření, která vytvoří na senzoru rozptylový kroužek CoC o takovém maximálním průměru, aby po zvětšení na fotografii formátu **$8 \times 12\text{ palců}$ ($20{,}32 \times 30{,}48\text{ cm}$, formát cca A4)** pozorovanou ze standardní vzdálenosti **$38\text{ až }40\text{ cm}$** standardním lidským okem (rozlišovací schopnost cca $0{,}25\text{ mm}$) nebylo rozostření na fotografii větší než **$0{,}25\text{ mm}$**.

#### Mezní hodnoty rozptylového kroužku CoC pro různé snímače

Čím menší je fyzický snímač, tím více se musí obraz zvětšit na formát A4, a tím menší musí být mezní hodnota CoC na samotném snímači:

| Typ snímače | Rozměr [mm] | Úhlopříčka [mm] | Nutné zvětšení na A4 | Mezní CoC (přesný) | Standardně používaný CoC |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Kinofilm / Full-frame (35 mm)** | $24 \times 36$ | $43\text{ mm}$ | $8{,}5\times$ | $0{,}0295\text{ mm}$ | **$0{,}03\text{ mm}$** |
| **APS-C snímač (DSLR)** | $16 \times 24$ | $28\text{ mm}$ | $12{,}8\times$ | $0{,}0195\text{ mm}$ | **$0{,}02\text{ mm}$** |
| **Kompakt (1/2.5" snímač)** | $4{,}3 \times 5{,}8$ | $7{,}2\text{ mm}$ | $51\times$ | $0{,}0049\text{ mm}$ | **$0{,}005\text{ mm}$** |

### Faktory ovlivňující hloubku ostrosti

Hloubku ostrosti ovlivňují tři základní fyzikální faktory:

1. **Clona**:
   * **Zavřená clona** (vysoké clonové číslo, např. $f/11, f/16$) zužuje světelný kužel $\implies$ rozptylové kroužky mimo rovinu zaostření jsou menší $\implies$ **VELKÁ hloubka ostrosti**.
   * **Otevřená clona** (nízké clonové číslo, např. $f/1{,}4, f/2{,}8$) vytváří široký kužel paprsků $\implies$ **MALÁ hloubka ostrosti** (pozadí je silně rozostřené – vzniká *bokeh*).
2. **Vzdálenost fotografovaného objektu (zaostřovací vzdálenost)**:
   * Čím je fotografovaný objekt **dále** od fotoaparátu, tím je hloubka ostrosti **větší**.
   * Čím je objekt **blíže** (např. u makrofotografie), tím je hloubka ostrosti **menší** (často jen několik milimetrů).
3. **Ohnisková vzdálenost objektivu**:
   * **Dlouhé ohnisko (teleobjektiv)** $\implies$ **malá hloubka ostrosti** (výrazná izolace objektu od pozadí).
   * **Krátké ohnisko (širokoúhlý objektiv)** $\implies$ **velká hloubka ostrosti** (ostré téměř celé pole od popředí k horizontu).
4. **Vliv velikosti senzoru na hloubku ostrosti**:
   * Malý senzor (např. v mobilu či kompaktu) vyžaduje pro dosažení stejného úhlu záběru **mnohem kratší skutečnou ohniskovou vzdálenost** (např. 4–6 mm namísto 50 mm).
   * Tato extrémně krátká ohnisková vzdálenost způsobuje, že **kompakty a mobilní telefony mají obrovskou hloubku ostrosti**, a je u nich prakticky nemožné opticky dosáhnout rozostřeného pozadí.

#### Porovnání hloubky ostrosti při zaostření na 10 metrů a cloně f/2.8

| Ekvivalentní ohnisko | 35mm SLR (CoC = 0,03 mm) | APS-C DSLR (CoC = 0,02 mm) | Kompakt (CoC = 0,005 mm) |
| :---: | :---: | :---: | :---: |
| **20 mm** | $3\text{ m} - \infty$ | $2{,}2\text{ m} - \infty$ | $0{,}7\text{ m} - \infty$ |
| **50 mm** | $7{,}5 - 15\text{ m}$ | $6{,}4 - 23{,}4\text{ m}$ | $3{,}3\text{ m} - \infty$ |
| **100 mm** | $9{,}2 - 10{,}9\text{ m}$ | $8{,}8 - 11{,}7\text{ m}$ | $6{,}6 - 20\text{ m}$ |
| **200 mm** | $9{,}8 - 10{,}2\text{ m}$ | $9{,}7 - 10{,}4\text{ m}$ | $8{,}9 - 11{,}5\text{ m}$ |
| **300 mm** | $9{,}9 - 10{,}1\text{ m}$ | $9{,}8 - 10{,}2\text{ m}$ | $9{,}5 - 10{,}6\text{ m}$ |

### Hyperfokální vzdálenost ($H$)

* **Definice**: speciální zaostřovací vzdálenost, při jejímž zaostření sahá hloubka ostrosti **od poloviny této vzdálenosti ($H/2$) až do nekonečna ($\infty$)**.
* **Vzorec pro výpočet**:
  $$H = \frac{f^2}{F \cdot c}$$
  * $f$ = ohnisková vzdálenost objektivu [mm]
  * $F$ = clonové číslo
  * $c$ = průměr mezního rozptylového kroužku CoC [mm]
* **Praktický význam**: klíčové nastavení pro krajinářskou a reportážní fotografii. Zaostří-li fotograf na hyperfokální vzdálenost (např. $6\text{ m}$), je vše od $3\text{ m}$ ($H/2$) až po nejvzdálenější obzor v nekonečnu ostré bez nutnosti přeostřování.

### Tlačítko náhledu hloubky ostrosti

* V hledáčku zrcadlovky je clona při komponování **vždy plně otevřená** na maximum (aby byl hledáček světlý a umožnil přesné zaostření).
* Po stisku **tlačítka náhledu hloubky ostrosti** (umístěného na těle fotoaparátu vedle bajonetu) se clona uzavře na hodnotu nastavenou pro expozici.
* Obraz v hledáčku sice ztmavne, ale fotograf přesně vidí skutečnou hloubku ostrosti a míru rozostření pozadí.

---

## Metody zaostřování a Autofokus (AF)

1. **Fix fokus (pevné zaostření)**:
   * Objektiv nemá zaostřovací mechanismus; je trvale zaostřen na pevnou vzdálenost (blízkou hyperfokální). Využívá se u levných hraček a jednorázových fotoaparátů s malým snímačem a velkou hloubkou ostrosti.
2. **Manuální ostření (Manual focus – MF)**:
   * Fotograf otáčí ostřícím kroužkem objektivu.
   * U klasických zrcadlovek pomáhal **mikroprizmatický prstenec** nebo **klínový dálkoměr** (půlené pole v hledáčku – při rozostření jsou linie rozpojené, při zaostření na sebe navazují).
3. **Automatické ostření (Autofokus – AF)**:
   * Dělí se na aktivní a pasivní systémy.

### Aktivní vs. Pasivní autofokus

| Vlastnost | Aktivní autofokus | Pasivní autofokus |
| :--- | :--- | :--- |
| **Princip fungování** | Fotoaparát **vysílá vlastní signál** (infračervený paprsek nebo ultrazvuk), měří odražené echo a ze zpoždění/úhlu spočítá vzdálenost. | Nevysílá nic; měří světlo ze scény procházející objektivem (**TTL – Through The Lens**) a analyzuje kontrast či fázový posun. |
| **Typy snímačů** | Samostatný vysílač a přijímač vedle hledáčku na těle přístroje. | Samostatný fázový AF senzor (DSLR) nebo přímo pixely hlavního obrazového snímače (bezzrcadlovky). |
| **Výhody** | • Bleskově rychlý<br>• **Funguje ve stoprocentní tmě** | • **Nemá omezení vzdálenosti** (ostří i na kilometry/nekonečno)<br>• Funguje skrz sklo, výlohy i mříže<br>• Měří přesně to, co vidí objektiv |
| **Nevýhody** | • **Omezený dosah** (cca do 5–6 metrů)<br>• **Selhává přes sklo, ploty či větve** (odrazí se od překážky)<br>• Ostří pouze na střed záběru<br>• Selhává na černých površích pohlcujících infračervené světlo | • **Potřebuje dostatek světla** (ve tmě selhává)<br>• Vyžaduje kontrastní hrany<br>• Závisí na světelnosti objektivu<br>• Zkouší polohy tam a zpět (u kontrastního AF) |

#### Jak prakticky otestovat typ autofokusu

* Ze vzdálenosti 1–2 metry se pokuste zaostřit na **čistý bílý kancelářský papír bez textury**, který vyplňuje celé zorné pole (nebo na jednolitou zamračenou oblohu).
* **Pokud fotoaparát odmítne zaostřit** (objektiv bezradně projíždí celý rozsah tam a zpět), přístroj disponuje **pasivním systémem ostření** (chybí mu kontrastní hrany). Aktivní systém by vzdálenost změřil bez potíží.

### Pomocné systémy pro ostření ve tmě u pasivního AF

* **Pomocné světlo AF (AF assist lamp)**: zabudovaná LED dioda na těle fotoaparátu, která na krátkou vzdálenost osvítí scénu.
* **Interní blesk**: vysílá sérii rychlých stroboskopických záblesků před expozicí pro osvětlení hran.
* **Laserová mřížka (Hologram AF)**: promítne na snímaný objekt laserový kontrastní kříž/vzor, na jehož hrany pasivní senzor okamžitě spolehlivě zaostří.

### Režimy a funkce autofokusu

* **Dvoupolohová spoušť**:
  * **Namáčknutí do poloviny (half-press)**: aktivuje měření expozice a zaostří objektiv. Konec měření ohlásí pípnutí a rozsvícení potvrzovacího bodu v hledáčku.
  * **Domáčknutí**: aktivuje závěrku a exponuje snímek.
* **AF Lock (uzamknutí zaostření)**: podržením namáčknuté spouště v režimu jednorázového ostření se vzdálenost zaostření uzamkne, což umožní překomponovat záběr.
* **Jednorázový AF (AF-S / One-Shot AF – priorita zaostření)**: po zaostření na statický objekt zůstane zaostřeno; spoušť nedovolí exponovat, dokud není přesně zaostřeno.
* **Kontinuální AF (AF-C / AI Servo – priorita snímku)**: fotoaparát neustále přeostřuje a prediktivně sleduje pohybující se objekt po celou dobu namáčknutí spouště.
* **Předostření (prefocus / zone focus)**: fotograf zaostří na konkrétní místo v prostoru, kde očekává objekt (např. zatáčka při závodech), zaostření uzamkne a exponuje v okamžiku příjezdu.
* **Důvody selhání pasivního AF**:
  * Nedostatek světla (šero, noc).
  * Silné přímé protisvětlo.
  * Zcela bezkontrastní scény (hladká zeď, mlha, obloha).
  * Extrémní makrosnímky (nedostatek světla a mikroskopická hloubka ostrosti).

### Doostření obrazu (Sharpening)

* **Princip**: softwarový proces, který **lokálně zvyšuje kontrast podél existujících hran** v obraze (světlá strana hrany se ještě zesvětlí, tmavá ještě ztmaví).
* Doostření **nevytváří nové detaily**, pouze opticky obnovuje a zvýrazňuje hrany, které byly změkčeny průchodem optikou a antialiasing filtrem snímače.
* **Rozdíl přístupů**:
  * Kompaktní přístroje a mobily silně doostřují přímo v přístroji („co je ostré, to je pěkné“).
  * Zrcadlovky a pokročilé fotoaparáty aplikují jen minimální tovární doostření (hodnota blízká nule) – **doostřovat se má až jako poslední krok při úpravách v počítači** po změně velikosti pro konkrétní tisk či web.

---

## Optika objektivu a vady zobrazení (aberace)

Žádná jednoduchá optická čočka není ideální. Konstrukce objektivů proto kombinuje více spojných a rozptylných čoček z různých druhů optického skla pro potlačení vad.

### 1. Geometrické vady objektivu

* **Sférická (otvorová) vada**:
  * Paprsky procházející okrajem čočky se lámou více než paprsky procházející blízko středu (paraxiální paprsky) $\implies$ bod se nezobrazí jako bod, ale jako neostrá ploška.
  * **Korekce**: zaclonění objektivu (odřízne okrajové paprsky), použití asférických čoček, kombinace spojky a rozptylky.
* **Koma**:
  * Vada šikmých paprsků přicházejících mimo optickou osu; bodový zdroj světla se zobrazí s nesymetrickým chvostem (jako kometa nebo kapka).
  * **Korekce**: aplanatická korekce (odstraňuje se společně se sférickou vadou).
* **Astigmatismus**:
  * Paprsky v horizontální a vertikální rovině se lámou do různých ohniskových vzdáleností $\implies$ bodový zdroj se zobrazí jako úsečka nebo elipsa.
  * **Korekce**: anastigmát (speciální soustava čoček s opačným astigmatismem).
* **Zklenutí obrazového pole (Curvature of field)**:
  * Ostrý obraz rovinné scény nevzniká v rovině, ale na zakřivené kulové ploše.
  * Pokud dopadne na plochý senzor, je **ostrý střed a neostré okraje**, nebo naopak po přeostření ostré okraje a neostrý střed.
* **Zkreslení obrazu (distorze)**:
  * Nestejné příčné zvětšení obrazu v různých vzdálenostech od optické osy:
  * **Soudkovité zkreslení**: zvětšení směrem k okrajům klesá, přímky se prohýbají ven (typické pro širokoúhlé objektivy).
  * **Poduškovité zkreslení**: zvětšení směrem k okrajům roste, přímky se prohýbají dovnitř (typické pro teleobjektivy).
* *Důležitá poznámka*: Geometrické vady nemohou být konstrukcí objektivu odstraněny všechny současně; optický návrh je vždy hledáním kompromisu.

### 2. Chromatická (barevná) vada

* **Příčina**: disperze světla – **index lomu skla závisí na vlnové délce světla**.
  * Krátkovlnné světlo (modré) se láme více než dlouhovlnné světlo (červené). Každá barva má své ohnisko v jiné vzdálenosti za čočkou.
* **Projev**: barevné duhové kontury (nejčastěji fialové, azurové či zelené) na kontrastních přechodech (např. větve stromu proti světlé obloze).
* **Korekce**:
  * Použití zrcadlových objektivů (odraz na zrcadle netrpí disperzí).
  * Skládání čoček z různých druhů skel (korunové a flintové sklo s různou disperzí) – tzv. **achromatické** a **apochromatické** soustavy čoček.

### 3. Vinětace

* **Projev**: úbytek jasu a ztmavnutí rohů obrazu směrem od středu k okrajům.
* **Příčiny**:
  1. **Optická vinětace objektivu**: šikmé paprsky dopadají pod úhlem $\theta$, přičemž osvětlení klesá podle zákona $\cos^4 \theta$.
  2. **Mechanická vinětace**: tubus objektivu, příruby čoček, filtry nebo nevhodná sluneční clona fyzicky stíní okrajové paprsky.
  3. **Vinětace digitálního snímače**: fotodiody jsou zapuštěné v hlubších křemíkových šachtách pod mikročočkami; kolmo dopadající světlo uprostřed čipu projde plně, zatímco šikmé paprsky v rozích narážejí na stěny šachet a na fotodiodu dopadnou jen částečně.
* **Korekce**: zaclonění objektivu, konstrukce objektivů s větší vstupní pupilou, softwarová korekce profilu objektivu.

### 4. Vady digitálního snímače

* **Blooming**:
  * Nastává při extrémním lokálním přesvětlení (např. přímé slunce nebo bodový reflektor v záběru).
  * Světlocitlivá buňka zcela naplní svou nábojovou kapacitu a přebytečné elektrony **přetečou do sousedních buněk**.
  * Na snímku se projeví jako vertikální nebo horizontální světlé pruhy a linky vycházející ze světelného zdroje podél čtecích registrů.

---

## Otázky a odpovědi k procvičení

Tato sekce přímo shrnuje kontrolní otázky ze všech tří prezentací:

### 1. Co je to expozice a expoziční stupeň (EV)?

* **Expozice** je celkové množství světla, které dopadne na citlivou vrstvu filmu nebo senzoru.
* **EV (Exposure Value)** je logaritmická jednotka množství světla a expozičního nastavení. Změna o $1\text{ EV}$ znamená dvojnásobné nebo poloviční množství světla. $0\text{ EV}$ odpovídá času $1\text{ s}$ při cloně $f/1{,}0$ a citlivosti $\text{ISO } 100$.

### 2. Jak se ve fotografii reguluje množství světla?

* Pomocí **expozičního trojúhelníku**:
  1. **Expozičním časem** (délka otevření závěrky).
  2. **Clonovým číslem** (velikost otvoru v objektivu).
  3. **Citlivostí ISO** (elektronické zesílení signálu snímače).

### 3. Co je clona a na co má vliv?

* Clona je kruhový otvor s proměnlivým průměrem ve středu objektivu.
* Ovlivňuje:
  1. Množství procházejícího světla (expozici).
  2. **Hloubku ostrosti** (čím větší clonové číslo, tím větší hloubka ostrosti).
  3. Optické vady objektivu (zaclonění potlačuje sférickou vadu a vinětaci, přílišné zaclonění však způsobuje difrakci/ohyb světla).

### 4. Jaká je stupnice standardních hodnot pro čas, clonu a ISO?

* **Čas**: $1\text{ s}, 1/2, 1/4, 1/8, 1/15, 1/30, 1/60, 1/125, 1/250, 1/500, 1/1000, 1/2000\text{ s}\dots$
* **Clona**: $f/1{,}0, f/1{,}4, f/2{,}0, f/2{,}8, f/4{,}0, f/5{,}6, f/8, f/11, f/16, f/22, f/32\dots$ (násobky $\sqrt{2} \approx 1{,}4$).
* **ISO**: $50, 100, 200, 400, 800, 1600, 3200, 6400, 12800\dots$

### 5. Co je důsledkem dlouhých expozičních časů?

* Rozmazání pohybujících se objektů (pohybová neostrost), rozhýbání snímku chvěním rukou fotografa a výrazný nárůst **tepelného šumu senzoru** (Dark current noise při časech $> 1\text{ s}$).

### 6. Co znamená dynamický rozsah scény a co je histogram?

* **Dynamický rozsah scény** je poměr mezi jasem nejtmavšího stínu a nejjasnějšího světla ve scéně.
* **Histogram** je sloupcový graf rozložení jasových tónů na fotografii od černé (vlevo) po bílou (vpravo). Pomáhá odhalit podexpozici (slití stínů) a přeexpozici (přepaly).

### 7. Kolik DPI má fotografie $18 \times 24\text{ cm}$ vyfotografovaná 4,8 Mpix fotoaparátem?

* Rozlišení $4{,}8\text{ Mpix}$ odpovídá přibližně $2530 \times 1900\text{ pixelům}$.
* Výpočet: $\text{DPI} = \frac{1900}{18} \times 2{,}54 \approx \mathbf{268\text{ DPI}}$ (velmi dobrá kvalita blízká standardu 300 DPI).

### 8. Na jaký maximální formát lze vytisknout 2 Mpix a 8 Mpix fotografii při 300 DPI?

* **2 Mpix** ($1600 \times 1200\text{ px}$): maximálně cca **$13 \times 10\text{ cm}$** při 300 DPI ($26 \times 20\text{ cm}$ při 150 DPI).
* **8 Mpix** ($3500 \times 2300\text{ px}$): maximálně cca **$30 \times 20\text{ cm}$** při 300 DPI ($60 \times 40\text{ cm}$ při 150 DPI).

### 9. Co je SLR, DSLR a jaký je rozdíl oproti bezzrcadlovkám?

* **SLR (Single Lens Reflex)** je jednooká zrcadlovka (klasická filmová), **DSLR** je digitální zrcadlovka. Využívají sklopné optické zrcátko a optický pětiboký hranol pro přímý pohled přes objektiv v reálném čase.
* **Bezzrcadlovka (EVF)** nemá optické zrcátko; obraz ze senzoru promítá na displej nebo do elektronického hledáčku (EVF).

### 10. Porovnejte snímače CCD a CMOS.

* **CCD**: náboj se posouvá přes sousední buňky k externímu zesilovači; poskytuje nižší šum a vysokou kvalitu obrazu, ale má vysokou spotřebu a je pomalý.
* **CMOS**: každá buňka má vlastní zesilovač a tranzistory; je rychlý, úsporný a levný na výrobu, avšak elektronika na buňce zmenšuje účinnou plochu fotodiody (menší Fill factor).

### 11. Jak funguje snímání barev u digitálního fotoaparátu?

* Čip je sám o sobě barvoslepý. Před pixely je předřazena **Bayerova maska RGBG** (50 % zelená, 25 % červená, 25 % modrá). Zbývající barevné složky pro každý pixel se dopočítávají ze sousedních pixelů pomocí **interpolace (demosaicing)**.

### 12. Co je Crop faktor a jak ovlivňuje ohniskovou vzdálenost?

* Crop faktor je poměr úhlopříčky kinofilmového políčka ($43{,}3\text{ mm}$) k úhlopříčce menšího snímače.
* Násobí ohniskovou vzdálenost objektivu na **ekvivalentní ohniskovou vzdálenost** z hlediska úhlu záběru ($f_{\text{ekv}} = f \times \text{Crop}$).

### 13. Co je rovina zaostření, rozptylový kroužek (CoC) a hloubka ostrosti?

* **Rovina zaostření**: rovina v prostoru, na kterou je objektiv přesně zaostřen.
* **Rozptylový kroužek (CoC)**: rozostřená kruhová ploška na senzoru vzniklá z bodů ležících mimo rovinu zaostření.
* **Hloubka ostrosti**: pásmo před a za rovinou zaostření, kde je CoC menší než limit rozlišovací schopnosti oka, takže obraz vnímáme jako ostrý.

### 14. Co ovlivňuje hloubku ostrosti?

1. **Clona**: vyšší clonové číslo $\implies$ větší hloubka ostrosti.
2. **Vzdálenost objektu**: větší vzdálenost $\implies$ větší hloubka ostrosti.
3. **Ohnisková vzdálenost**: kratší ohnisko $\implies$ větší hloubka ostrosti.
4. **Velikost snímače**: menší snímač vyžaduje kratší reálné ohnisko pro stejný záběr $\implies$ výrazně větší hloubka ostrosti.

### 15. Jaký je rozdíl mezi aktivním a pasivním autofokusem?

* **Aktivní AF**: vysílá infračervený paprsek a měří echo; funguje ve tmě, ale jen do cca 6 m, ostří na střed a selhává přes sklo.
* **Pasivní AF**: analyzuje světlo procházející objektivem (kontrast nebo fázový posun); funguje na jakoukoli vzdálenost a přes sklo, ale potřebuje světlo a kontrastní hrany.

### 16. Jak zjistit, jaký typ autofokusu přístroj má?

* Zaostřete na čistě bílý papír bez textury na vzdálenost 1–2 metry. Pokud fotoaparát odmítne zaostřit, máte pasivní systém autofokusu.

<!-- vygenerováno pomocí Agy CLI -->