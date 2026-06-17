# Počítačové sítě

## Osnova

* Co je to počítačová síť
* Historie
* Síťová architektura
* Dělení sítí
* Síťová zařízení
* Topologie

## Co to je?

* **Počítačová síť** - propojená zařízení, která spolu mohou komunikovat na základě stanovených pravidel (např. počítače, telefony, IoT zařízení...).
* **Drátové připojení**:
  * **Metalické kabely**: Využívají elektrické impulsy (např. Ethernet). Jsou pomalejší než rychlost světla, nicméně moderní standardy umožňují rychlosti až 40 Gb/s.
  * **Optické kabely**: Modernější, vedou světelný paprsek téměř rychlostí světla. Nabízejí velmi vysoké přenosové rychlosti (až 100 Gb/s) a jsou ideální na dlouhé vzdálenosti s minimální odezvou mezi kontinenty.
* **Bezdrátové připojení**:
  * **Wi-Fi (rádiové vlny)**: Často využívá frekvenci 2,4 GHz, postupně se přechází na 5 GHz (méně zarušené pásmo, větší šířka pásma).
  * **Bluetooth (rádiové vlny)**: Pro přenos na krátké vzdálenosti v rámci PAN (např. bezdrátová sluchátka). Využívá frekvenční kanály kolem 2,4 GHz.
  * **Mikrovlnné a satelitní připojení**: Přenos na dlouhé vzdálenosti. Vyžaduje přímou viditelnost mezi anténami nebo využívá satelity na oběžné dráze (např. Starlink). Může mít o něco vyšší odezvu (ping) a používá se v oblastech bez kabelové infrastruktury.

## Historie

* První pokusy o komunikaci mezi počítači se datují na konec 50. let 20. století (pro potřeby armády).
* V 60. letech vzniká síť **ARPANET**.
* Na počátku 80. let dochází k masovému rozvoji a pokládají se základy pro celosvětovou síť **WWW** (World Wide Web).

## Síťová architektura

Umožňuje výměnu dat mezi systémy. Vzhledem ke složitosti je architektura rozdělena do vrstev.

![Vrstvy v referenčním modelu ISO/OSI](/informatika/assets/OSI_Model_v1.svg)

Každá vrstva poskytuje službu vyšší vrstvě (např. transportní vrstva zajišťuje přenos paketů pro aplikační vrstvu přes TCP). Funkce jednotlivých vrstev jsou definovány protokoly.

* **Protokol** = soubor pravidel pro výměnu informací mezi dvěma či více komunikujícími prvky.
* **Standardy** - definovány organizacemi jako IETF (Internet Engineering Task Force), které publikují dokumenty RFC (Request for Comments).

### Transportní protokoly

* **TCP (Transmission Control Protocol)**
  * Spolehlivý spojovaný protokol (bezztrátový).
  * Každý paket obsahuje kontrolní informace (pořadové číslo atd.), podle kterých se ověřuje doručení a integrita dat.
  * Pokud dojde ke ztrátě nebo poškození paketu, odešle se znovu. Je kvůli tomu o něco pomalejší.
  * Vhodný pro přenos webových stránek, souborů a dokumentů, kde nesmí dojít ke ztrátě či záměně pořadí dat.
* **UDP (User Datagram Protocol)**
  * Nespolehlivý nespojovaný protokol (ztrátový).
  * Data se přenášejí v podobě datagramů bez zpětného potvrzování a oprav.
  * Vyznačuje se minimální režií a vysokou rychlostí.
  * Vhodný pro přenosy v reálném čase, např. IP telefonie (VoIP), online hry či streamování, kde mírná ztráta dat nevadí, ale klíčová je rychlost a nízké zpoždění.

### Aplikační protokoly

* **HTTP (Hypertext Transfer Protocol)**
  * Protokol pro přenos webových dokumentů (stránek).
  * Většina verzí využívá jako transportní protokol TCP. Od verze HTTP/1.1 se zprávy mohou rozložit na více částí (tzv. chunking), což umožňuje posílat soubory bez nutnosti předem znát jejich celkovou velikost a ukládat je celé do paměti.
  * Komunikace funguje na principu dotaz (request) a odpověď (response).
  * **Struktura HTTP zprávy**:
    * **HTTP hlavička (Header)**:
      * U dotazu obsahuje metodu (např. GET, POST), cestu k dokumentu (např. `/o-nas`) a verzi protokolu.
      * U odpovědi obsahuje číselný stavový kód (např. 200 – OK, 404 – Nenalezeno, 500 – Vnitřní chyba serveru).
      * Dále obsahuje další pole (klíč: hodnota) s informacemi jako typ prohlížeče, cookies, typ serveru atd.
    * **HTTP tělo (Body)**:
      * Obsahuje samotný přenášený soubor (HTML dokument, obrázek, video, text...). U některých typů dotazů může chybět.
* **HTTPS (HTTP Secure)**
  * Zabezpečená verze protokolu HTTP.
  * Data jsou šifrována, čímž se brání jejich odposlechu.
  * Využívá bezpečnostní certifikáty k ověření identity serveru (uživatel má jistotu, s kým komunikuje).
  * K šifrování se používají protokoly SSL (Secure Sockets Layer) a novější TLS (Transport Layer Security).

### Protokol IP

Každé zařízení připojené do sítě (v LAN i v Internetu) má přidělenou IP adresu. Existují i vyhrazené privátní rozsahy a adresy pro speciální účely (např. loopback `127.0.0.1` či rozsahy jako `10.0.0.1` – `10.0.0.255`).

Rozlišujeme dvě verze IP adres:
* **IPv4** - 32bitová adresa zapsaná jako čtyři čísla oddělená tečkami (každé číslo má 8 bitů, tj. hodnotu 0-255, např. `142.251.141.174`). Adresy tohoto protokolu byly již vyčerpány (kolem roku 2011).
* **IPv6** - 128bitová adresa zapsaná hexadecimálně v 8 skupinách oddělených dvojtečkami (např. `2001:db8:0:1234:0:567:8:1`). Řeší nedostatek adres v IPv4.

## Dělení sítí

### Podle rozlehlosti

* **PAN (Personal Area Network)**
  * Osobní síť jednotlivce pro propojení vlastních zařízení na krátké vzdálenosti (např. mobil a chytré hodinky).
  * Využívá technologie jako Bluetooth nebo USB.
* **LAN (Local Area Network)**
  * Lokální počítačová síť v domácnostech, školách nebo kancelářích. Může být drátová i bezdrátová (WLAN).
  * **VLAN (Virtual LAN)**: Virtuální lokální síť, která umožňuje logicky rozdělit jednu fyzickou síť na více samostatných podsítí (např. oddělení dvou počítačových učeben na jednom switchi).
    ![VLAN Concept](/informatika/assets/VLAN_Concept.svg)
    *Autor: Michel Bakni – Tento soubor byl odvozen z: Workstation symbol-Blue.svg, Switch symbol-Blue.svg, CC BY-SA 4.0, [Wikimedia](https://commons.wikimedia.org/w/index.php?curid=151750621)*
* **MAN (Metropolitan Area Network)**
  * Metropolitní síť propojující území v rámci města či městské části.
* **WAN (Wide Area Network)**
  * Rozlehlá síť pokrývající rozsáhlé geografické území (státy, kontinenty). Nejznámějším příkladem sítě WAN je Internet.
    ![Diagram sítí](/informatika/assets/Component%20diagram%20for%20project%20Liberouter.svg)
    *Autor: Původně soubor načetl Kratochvíla na projektu Wikipedie v jazyce čeština – Na Commons přenesl z cs.wikipedia uživatel jitka., CC BY-SA 3.0, [Wikimedia](https://commons.wikimedia.org/w/index.php?curid=4224433)*

### Podle způsobu přepojování

* **Sítě s přepojováním okruhů (komutační)**
  * Komunikace probíhá po vyhrazené fyzické trase (okruhu), která je rezervována po celou dobu spojení.
  * Typické pro starší telefonní systémy a telegrafii.
* **Sítě s přepojováním paketů**
  * Data se rozdělí na menší části (pakety), které mohou k cíli putovat různými trasami na základě směrování (IP protokol).
  * Pakety mohou dorazit v jiném pořadí nebo se ztratit (rekonstrukci pořadí řeší TCP). Typickým příkladem je Ethernet a Internet.

### Podle postavení uzlů

* **Klient-server**
  * **Server** poskytuje služby (souborové, webové, tiskové...).
  * **Klient** o tyto služby žádá a využívá je.
* **P2P (Peer-to-Peer)**
  * Decentralizovaný model, kde jsou si všechny uzly v síti rovny (každý uzel může vystupovat jako klient i server).
  * Využívá se např. pro sdílení souborů (torrenty).

### Podle druhu signálu

* **Analogové sítě** - přenášejí spojitě se měnící signál (např. staré telefonní linky).
* **Digitální sítě** - přenášejí signál v diskrétních stavech (např. binární signál 0 a 1).

### Podle vlastnictví a přístupu

* **Veřejné sítě** - telekomunikační sítě určené pro veřejnost (poskytovatelé se řídí příslušnou legislativou).
* **Privátní sítě** - uzavřené sítě určené pouze pro interní potřebu organizace (využívají vyhrazené privátní IP adresy).
* **VPN (Virtual Private Network)**
  * Virtuální privátní síť, která šifruje veškerou komunikaci a přenáší ji zabezpečeným kanálem přes veřejnou síť.
  * Umožňuje simulovat lokální síť (LAN) na dálku, obcházet geografická omezení (georestrikce) a zvyšuje anonymitu a bezpečnost uživatele.

## Síťová zařízení

### Aktivní síťové prvky

Aktivně působí na přenášené signály (zesilují je, upravují apod.) a slouží k propojení zařízení v síti.

* **Opakovač (Repeater)** - přijímá oslabený či zkreslený signál, čistí ho, zesiluje a posílá dál, čímž prodlužuje dosah média.
* **Hub (Rozbočovač)** - jednoduché zařízení pro větvení sítě. Přijatá data bez přemýšlení rozešle do všech svých portů. Dnes se již nepoužívá.
* **Switch (Přepínač)** - inteligentní zařízení, které směruje data pouze do portu, kde se nachází adresované zařízení (pracuje na základě MAC adres). Nabízí vysoký počet portů.
* **Bridge (Most)** - propojuje dva různé segmenty sítě a filtruje provoz mezi nimi, čímž snižuje celkové zatížení.
* **Router (Směrovač)** - pracuje na síťové vrstvě (směruje pakety podle IP adres) a umožňuje propojení různých sítí (např. domácí sítě LAN s internetem).

### Pasivní síťové prvky

* Zahrnují prvky, které signál neupravují ani nezesilují (např. metalická a optická kabeláž, konektory, patch panely atd.).

## Topologie

Definuje tvar a strukturu zapojení prvků v počítačové síti.

* **Sběrnicová (Bus)** - všechna zařízení jsou zapojena na jeden společný kabel (např. koaxiální). Porucha kabelu vyřadí celou síť.
* **Hvězdicová (Star)** - všechna zařízení jsou připojena k centrálnímu aktivnímu prvku (např. switch). Nejčastější typ zapojení (kroucená dvojlinka).
* **Kruhová (Ring)** - zařízení jsou zapojená v uzavřeném kruhu. Data obíhají jedním směrem.
* **Stromová (Tree)** - hierarchické propojení několika hvězdicových topologií, typické pro rozsáhlejší LAN sítě.
* **Obecný graf (Mesh)** - obsahuje redundantní (záložní) spoje pro případ výpadku. Typické pro WAN sítě (např. Internet).
* **Samostatný počítač** - virtuální síťové rozhraní (loopback) pro testovací účely na jednom stroji.

## Zdroje

* Přispěvatelé Wikipedie, *Počítačová síť* [online], Wikipedie: Otevřená encyklopedie, c2025, Datum poslední revize 27. 11. 2025, 10:13 UTC, [citováno 29. 11. 2025] <[https://cs.wikipedia.org/w/index.php?title=Po%C4%8D%C3%ADta%C4%8Dov%C3%A1_s%C3%ADt%C4%9B&oldid=25446803](https://cs.wikipedia.org/w/index.php?title=Po%C4%8D%C3%ADta%C4%8Dov%C3%A1_s%C3%ADt%C4%9B&oldid=25446803)>
* Přispěvatelé WikiSkripta, *Počítačové sítě* [online], , c2025, Datum poslední revize 10. 02. 2025, 09:31 UTC, [citováno 29. 11. 2025] <[https://www.wikiskripta.eu/index.php?title=Po%C4%8D%C3%ADta%C4%8Dov%C3%A9_s%C3%ADt%C4%9B&oldid=493847](https://www.wikiskripta.eu/index.php?title=Po%C4%8D%C3%ADta%C4%8Dov%C3%A9_s%C3%ADt%C4%9B&oldid=493847)>
* Počítačové sítě (článek) | Internet. In: *Khan Academy* [online] [cit. 29.11.2025]. Dostupné z: [https://cs.khanacademy.org/computing/informatika-pocitace-a-internet/x8887af37e7f1189a:internet/x8887af37e7f1189a:site-a-jejich-propojovani/a/computer-networks-overview](https://cs.khanacademy.org/computing/informatika-pocitace-a-internet/x8887af37e7f1189a:internet/x8887af37e7f1189a:site-a-jejich-propojovani/a/computer-networks-overview)
* Přispěvatelé Wikipedie, Referenční model ISO/OSI [online], Wikipedie: Otevřená encyklopedie, c2025, Datum poslední revize 10. 09. 2025, 12:15 UTC, [citováno 29. 11. 2025] <https://cs.wikipedia.org/w/index.php?title=Referen%C4%8Dn%C3%AD_model_ISO/OSI&oldid=25202890>