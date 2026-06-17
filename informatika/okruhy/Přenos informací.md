# Přenos informací

## Osnova

* Definice dat a informací
  * Data, informace, bit, byte
* Způsoby přenosu
  * Historie vs. dnes
  * Komunikační model, přenosové kanály, signály (digitální, analogový)
* Kódování a modulace
* Rychlost přenosu informací
  * Kapacita kanálu – Shannon
  * Komunikační protokoly a vrstvy
* Komprese dat – ztrátová, bezztrátová
* Bezpečnost přenosu
* Chyby při přenosu informací
  * Šum, zkreslení atd.
* Uchovávání a přenos
* Příklady přenosu informací

## Definice dat a informací

* **Data**: Jednotlivé údaje zpracovávané počítačem (čísla, znaky atd.). Sama o sobě nemusí mít význam, ten získávají až kontextem.
* **Informace**: Data, která získají význam v určitém kontextu; slouží ke zpracovávání, uchovávání nebo přenášení.
  * Dělení informací: textové, obrazové, zvukové.
* **Bit**: Nejmenší jednotka informace (nabývá hodnoty 0 nebo 1).
* **Byte**: Skupina 8 bitů, používá se pro vyjádření velikosti souborů a kapacity paměti.
* **Signál**: Nosič informace, dělí se na:
  * **Analogový (spojitý)**: plynulé hodnoty, většinou vstupní signál (např. záznam mikrofonu, kamery).
  * **Digitální (diskrétní)**: oddělené stavy, „vzorkovaný“ signál (např. digitální výstup počítače).
* **Metadata**: Data poskytující informace o jiných datech (slouží pro vyhledávání nebo zpracování popisovaných dat).
* **A/D převodník**: Převádí analogový signál na digitální data (např. z hlasu do počítače).
* **D/A převodník**: Převádí digitální data na analogový signál (např. z počítače do zvuku).
* **Digitalizace**: Převod analogového signálu na digitální data.

## Způsoby přenosu

* **Historický vývoj**:
  * Dříve: přenos pomocí fyzických nosičů jako diskety, CD.
  * Dnes: optické sítě, UTP (kroucená dvoulinka – twisted pair, kde nedochází k tak velkému rušení dat a dosahuje se vyšší rychlosti přenosu).
* **Komunikační model**:
  * Zdroj informace -> kódování (převod na bity) -> vysílač -> přenosový signál (kabel/vzduch/optika) -> (rušení/šum) -> přijímač -> dekódování -> příjemce informace.
* **Přenosové kanály**:
  * **Metalické vedení**: drát z jednoho místa na druhé (např. měděný kabel).
  * **Optické vlákno**: přenos světelnými impulzy – extrémně rychlý, odolný vůči elektromagnetickému rušení.
  * **Bezdrátové kanály**: přenos vzduchem (např. Wi-Fi, Bluetooth), odstraňuje nutnost fyzické kabeláže.
* **Sériový vs. paralelní přenos**:
  * Sériový přenos: dnes převažující způsob, data se posílají postupně v jednom kanále.
  * Paralelní přenos: dříve využívaný (např. 8 kanálů najednou), byl však pomalejší na delší vzdálenosti kvůli nesynchronizaci vodičů.
* **Směrovost přenosu**:
  * **Simplex**: jednosměrný přenos (např. televizní vysílání, rádio).
  * **Half-duplex**: obousměrný přenos, ale střídavý (např. vysílačky).
  * **Full-duplex**: obousměrný přenos současně (např. telefonování, moderní počítačové sítě).
* **Metody přepojování**:
  * **Paketový přenos**: data se rozdělí na pakety, které mohou v síti cestovat různými trasami a na cílovém zařízení se opět složí (např. internet).
  * **Okruhový přenos**: vytvoří se vyhrazené, stálé spojení po celou dobu trvání komunikace (např. klasické telefonní linky).

## Kódování a modulace

Aby informace mohly být zpracovány počítačem, musí být převedeny na data. To se provádí kódováním a následnou modulací pro přenos.

* **Kódování**: Převod informace na bity (určuje, jak informaci zapíšeme do bitů a jak ji odešleme).
* **Modulace**: „Namíchání“ bitů do nosného signálu (umožňuje přenášet data na určité frekvenci, což vede k lepšímu využití přenosového kanálu).

## Rychlost přenosu informací

* Rychlost přenosu závisí na: fyzické přenosové rychlosti, zpoždění (latenci) a celkové propustnosti.
* **Kapacita kanálu (Shannon-Hartleyův teorém)**:
  * Teoretická maximální kapacita kanálu závisí na šířce frekvenčního pásma a poměru signálu k šumu.
* **Komunikační protokoly a vrstvy**:
  * Pravidla komunikace a strukturování síťových funkcí (např. v modelech OSI nebo TCP/IP).

## Komprese dat

Komprese dat je speciální případ konverze dat, jejímž hlavním cílem je zmenšit celkový objem a zrychlit přenos.

* **Ztrátová komprese**: Některé informace jsou z dat nevratně odstraněny (nelze je zpětně plně rekonstruovat).
  * Příklady formátů: JPEG, MP3.
* **Bezztrátová komprese**: Nedosahuje tak vysoké úrovně komprese jako ztrátová, ale soubor lze zpětně zcela přesně zrekonstruovat do původní podoby.
  * Příklady formátů: ZIP, PNG.

## Bezpečnost přenosu

* Základní pilíře zabezpečení přenosu:
  * **Důvěrnost**: data jsou chráněna před neoprávněným čtením.
  * **Integrita**: záruka, že data nebyla při přenosu změněna.
  * **Autentizace**: ověření identity odesílatele a příjemce.
* Příklady zabezpečovacích mechanismů: HTTPS, WPA2/WPA3, VPN.

## Chyby při přenosu informací

* **Šum**: Náhodné a nežádoucí změny signálu (způsobené např. vlivem vnitřní elektroniky, tepla nebo okolního prostředí).
* **Zkreslení**: Změna tvaru nebo kvality signálu vyvolaná přenosovými vlastnostmi média.
* **Útlum**: Postupné oslabení signálu během přenosu (vlivem vzdálenosti, fyzických překážek nebo opotřebení média).
* **Rušení (interference)**: Ovlivnění užitečného signálu jiným vnějším signálem (např. elektromagnetické vlny z okolních spotřebičů).
* **Oprava a řešení chyb**:
  * Opakované odeslání (např. mechanismus v protokolu TCP).
  * Samoopravné kódy (např. parita, Hammingův kód), které umožní detekovat a případně přímo opravit chyby bez nutnosti znovuzasílání.

## Uchovávání a přenos informací

* **Režimy přenosu**:
  * **Online**: data jsou přenášena v reálném čase přes síťové připojení.
  * **Offline**: data jsou uchovávána a přenášena na fyzických médiích bez přímého síťového propojení.
* **Příklady přenosových služeb**:
  * Web (HTTP/HTTPS), e-mail, video streaming, cloudová úložiště, VoIP (Voice over IP) atd.

## Zdroje

* Informace a data - WikiSkripta. In: [cit. 31.03.2026]. Dostupné z: [https://www.wikiskripta.eu/w/Informace_a_data](https://www.wikiskripta.eu/w/Informace_a_data)