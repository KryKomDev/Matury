# Webová aplikace

## Osnova

* Definice (web server, přístup přes prohlížeč, příklady)
* Historický kontext (přechod z desktopových aplikací na webové standardy)
* Frontend (HTML, CSS, JavaScript, formuláře)
* Backend (frameworky, databáze, REST API)
* Stack aplikace (ukázka celého stacku)

## Co to je?

* **Aplikace poskytovaná z webového serveru**:
  * Přenos probíhá skrz síť (internet, LAN nebo intranet – interní síť v rámci nějaké společnosti).
* **Uživatel k ní přistupuje přes webový prohlížeč** (jednoduchý přístup):
  * Výhoda: netřeba aplikaci instalovat na koncových zařízeních.
  * Nevýhoda: mnohdy horší výkon než u desktopových aplikací a nekonzistentní implementace webových specifikací napříč prohlížeči.
* **Příklady**:
  * Internetové bankovnictví, online kancelářské programy (Google Docs), aukční portály, e-shopy, mapové služby.
* **Architektura klient-server**:
  * Klient: webový prohlížeč.
  * Server: webový server – je sám o sobě bezstavový (nepamatuje si předešlé požadavky). K přidání stavu (např. pro trvalé přihlášení uživatele) se vytvářejí relace (sessions), jejichž identifikátory se nejčastěji ukládají u klienta v cookies.
* **Síťové protokoly**:
  * Používá se HTTP, HTTPS, případně WebSockets pro obousměrnou komunikaci v reálném čase.

## Historie

* **Dřívější koncept klient-server**:
  * Klientem byla přímo dedikovaná desktopová aplikace, server zpracovával data.
  * Nevýhoda: při aktualizaci serveru (např. přidání nové funkce) bylo nutné aktualizovat klientské aplikace na každém jednotlivém počítači.
* **Přechod na webové aplikace**:
  * Server generuje HTML kód dynamicky a prohlížeč jej pouze zobrazuje.
  * Přidání interaktivity na klientské straně pomocí skriptovacího jazyka JavaScript.
* **Příchod HTML5 (2014)**:
  * Umožnil fungování offline aplikací.
  * Přinesl řadu nových sémantických tagů a element `<canvas>` umožňující přímé vykreslování grafiky.
* **Klientské dotazy na pozadí**:
  * Využívání API přímo na klientské straně (pomocí `fetch` požadavků, dříve XHR).
* **Současný stav**:
  * Velké množství moderních aplikací je realizováno jako webové.
  * Desktopové verze webových aplikací se dnes často vyvíjejí s využitím frameworků jako Electron (embedovaný prohlížeč zobrazující webovou aplikaci – např. Discord, Steam, Obsidian, WhatsApp).

## Frontend

* Uživatelské rozhraní běžící na straně klienta.
* Prohlížeč stahuje a interpretuje HTML soubory s tagy pro jednotlivé elementy stránky (např. tlačítka, textová vstupní pole atd.).
* Vzhled a rozložení prvků definuje CSS (kaskádové styly):
  * Zajišťuje změnu layoutu stránky, barevnost, nastavení fontů atd.
* Interaktivitu a dynamické chování zajišťuje JavaScript:
  * Např. reakce na stisknutí tlačítka (zobrazení obsahu, odeslání dat).
* Možnost vykreslovat vlastní grafický obsah:
  * Vhodné pro simulace či webové hry s využitím elementu `<canvas>` (který podporuje WebGL).
* Specifickým HTML elementem je formulář (`<form>`):
  * K odeslání dat není potřeba programovat interaktivitu v JavaScriptu; po odeslání prohlížeč naviguje (odešle požadavek) na příslušnou adresu.
  * Příklad objednávky:
    * Formulář obsahuje pole: `[Zadejte počet fazolí] [Zadejte svůj email] [Zadejte adresu]` (akce: `/kup`, metoda: `POST`).
    * Po kliknutí na odeslat prohlížeč otevře v aktuálním okně stránku `/kup`. Server při tomto načtení obdrží zadané hodnoty, zpracuje je a vrátí uživateli například potvrzení objednávky.

## Backend

* Implementace logiky na straně serveru.
* Často zprostředkovává spojení s databází:
  * Požadavek uživatele -> zpracování na serveru -> dotaz na databázi -> zpracování odpovědi z databáze serverem -> odeslání odpovědi uživateli.
* Může být implementován v mnoha programovacích jazycích a frameworcích:
  * PHP (Nette, Laravel, případně čisté PHP).
  * C# a .NET (ASP.NET).
  * Java (Spring).
  * JavaScript (runtimy jako Node.js, frameworky jako Next.js).
  * Python (Django, FastAPI, Flask).
* **API (Application Programming Interface)**:
  * Rozhraní, pomocí kterého mohou s backendem komunikovat další aplikace (např. standard [REST](https://cs.wikipedia.org/wiki/Representational_State_Transfer)).
  * Příklady využití: načtení informací o produktu do mobilní aplikace, přihlášení a odhlášení uživatele.
  * Příklady požadavků:
    * `POST /api/v1/user/login` (tělo: `username=...&password=...`)
    * `POST /api/v1/user/logout` (hlavička `Authorization: …`)
    * `GET /api/v2/product?id=…`
  * Struktura přenášených dat: nejčastěji formáty JSON nebo XML, může však jít o libovolný text či bajtové pole.

## Stack aplikace

* Pojem popisující všechny technologie a vrstvy, které daná aplikace využívá.
* Příklad stacku u aplikace na psaní poznámek:
  * Klient: webový prohlížeč (zobrazuje HTML, CSS, JavaScript).
  * Server: PHP (zpracovává požadavky a posílá vygenerované stránky).
  * Databáze: PostgreSQL (ukládá poznámky uživatelů).
  * Další služby: CDN pro rychlé stahování statického obsahu, externí API pro stahování obrázků, autentizační služba pro přihlašování.

## Zdroje

* HTML5. In: *Wikipedie* [online]. 2025 [cit. 31.12.2025]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=HTML5&oldid=25256119](https://cs.wikipedia.org/w/index.php?title=HTML5&oldid=25256119)
* Representational State Transfer. In: *Wikipedie* [online]. 2025 [cit. 31.12.2025]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Representational_State_Transfer&oldid=25220688](https://cs.wikipedia.org/w/index.php?title=Representational_State_Transfer&oldid=25220688)
* Web Applications. In: *Web Applications* [online] [cit. 31.12.2025]. Dostupné z: [https://spring.io/web-applications](https://spring.io/web-applications)
* Webová aplikace. In: *Wikipedie* [online]. 2025 [cit. 31.12.2025]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Webov%C3%A1_aplikace&oldid=25474761](https://cs.wikipedia.org/w/index.php?title=Webov%C3%A1_aplikace&oldid=25474761)