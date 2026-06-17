# Internet

## Osnova

* Charakteristika
* Historie
  * ARPANET a další milníky
* Služby
  * WWW, e-mail, VoIP a další
* Připojení k internetu
* W3C – specifika webu

## Charakteristika

* Počítačová síť, tzv. síť sítí – propojuje jednotlivé sítě
  * Není však dostupná 100% celosvětově – některé státy internet cenzurují (Čína, Rusko, …) a blokují určité weby.
* Používají se protokoly TCP/IP – přenos viz přenos informací a počítačové sítě
  * Každý počítač připojený k internetu má IP adresu.
  * Místo IP se většinou používají doménová jména ([google.com](http://google.com)).
* Orientace na webu probíhá pomocí vyhledávačů a katalogů (seznamů odkazů).

## Historie

* **1958** – Založena agentura ARPA (později přejmenována na DARPA)
  * Cíl: udělat z USA technologického lídra v kontextu studené války
* **1969** – Zprovozněna decentralizovaná síť ARPANET
  * Původně spojovala 4 univerzitní počítače a využívala přepojování paketů
* **1990** – První webový server
* **1991** – Nasazení WWW v CERNu
* **1991** – Připojeno Československo (formální připojení linky na ČVUT proběhlo v roce 1992)
* **1994** – Založení konsorcia W3C
* **2011** – Vyčerpání IPv4 adres

![Počet uživatelů internetu na 100 obyvatel v letech 1997 až 2017](https://upload.wikimedia.org/wikipedia/commons/2/29/Internet_users_per_100_inhabitants_ITU.svg)
*Autor: Jeff Ogden (W163) and Jim Scarborough (Ke4roh) – Vlastní dílo, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=18972898*

## Služby

* Počítačové programy navzájem komunikující pomocí protokolů (viz Počítačové sítě)

### WWW (World Wide Web)
* Webové stránky
  * Klient: webový prohlížeč
  * Server: webový server
  * Protokol: HTTPS
* Důležité součásti: e-shopy a sociální sítě

### E-mail
* Elektronická pošta
* **Protokoly:**
  * SMTP – přenos e-mailů z jednoho serveru na druhý (např. @seznam.cz → @gmail.com)
  * POP3, IMAP – přenos e-mailů ze serveru do klienta
* **Klient:** mailový klient (Outlook, Thunderbird, …), případně v podobě webové služby (např. Gmail, který funguje jako klient i server)
* **Server:** mailový server

### Instant messaging
* Různé protokoly pro okamžité zasílání zpráv
* Příklady: WhatsApp, Signal, Discord, …

### VoIP (Voice over IP)
* Telefonování přes internet, obvykle transportované přes UDP (kvůli minimalizaci zpoždění)
* Příklady: Skype, WhatsApp, …

### Přenos souborů
* **Protokoly:**
  * FTP (*File Transfer Protocol*)
  * SFTP (*Secure File Transfer Protocol*)

### DNS (Domain Name System)
* Protokol: DNS
* Server: DNS server
* Funkce: překládání doménových jmen na IP adresy

### SSH (Secure Shell)
* Protokol pro zabezpečený terminálový přístup k počítači z jiného počítače

*Poznámka: Služeb existuje mnohem více…*

## Připojení k internetu

* **Zprostředkovatel internetu** = ISP (*Internet Service Provider*)
* Připojení může být realizováno kabelem, bezdrátově apod.
* **Poslední míle** – označuje přípojku, která vede přímo do našeho routeru.
* **Kvalitu připojení udává:**
  * Agregace – kolik uživatelů sdílí jednu linku
  * Doba odezvy – čas, za jak dlouho se vrátí odpověď po odeslání dotazu
  * Technologie a šířka pásma poslední míle (optická vlákna, metalické kabely atd.)
* Všechna zařízení v siťové infrastruktuře mají svoji [IP adresu](https://cs.wikipedia.org/wiki/IP_adresa) (verze IPv4 nebo IPv6, která nabízí více adres).

## W3C

* **World Wide Web Consortium** – mezinárodní konsorcium
* Vyvíjí webové standardy pro WWW.
* Tyto standardy fungují jako doporučení:
  * Nemusíte se jimi striktně řídit (např. běžně není implementováno 100% pokrytí HTML5)
* **Důležité specifikace:**
  * URL
  * HTTP
  * HTML
  * Tyto specifikace pak implementují například vyhledávače.
* WWW a W3C založil Tim Berners-Lee.

## Zdroje

* About us. In: *W3C* [online] [cit. 30.12.2025]. Dostupné z: [https://www.w3.org/about/](https://www.w3.org/about/)
* Dějiny internetu. In: *Wikipedie* [online]. 2025 [cit. 30.12.2025]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=D%C4%9Bjiny_internetu&oldid=25438815](https://cs.wikipedia.org/w/index.php?title=D%C4%9Bjiny_internetu&oldid=25438815)
* Internet. In: *Wikipedie* [online]. 2025 [cit. 30.12.2025]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Internet&oldid=25390512](https://cs.wikipedia.org/w/index.php?title=Internet&oldid=25390512)
* World Wide Web. In: *Wikipedie* [online]. 2025 [cit. 30.12.2025]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=World_Wide_Web&oldid=25204824](https://cs.wikipedia.org/w/index.php?title=World_Wide_Web&oldid=25204824)