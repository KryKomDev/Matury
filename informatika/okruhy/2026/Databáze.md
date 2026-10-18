# Databáze

## Osnova

* Co je to databáze
* Historie databází
* Dělení databází
* Relační databáze
* Integrita dat
* Příklady známých databází

## Co je to databáze

* Systém souborů s pevně danou strukturou záznamů.
  * Příklad: jako databázi si můžeme představit tabulku, která má definované sloupce (struktura) a řádky představují jednotlivé záznamy. V jedné databázi je obvykle takových tabulek více.
* Pojem běžně zahrnuje jak samotná uložená data, tak i systém řízení báze dat (DBMS – Database Management System, např. PostgreSQL) a nástroje pro správu a přístup k datům (např. pgAdmin).
* Zjednodušeně řečeno: obsahuje informace a definuje, jak jsou tyto informace navzájem propojeny.
* Vztah klientské aplikace s databází obvykle funguje na principu klient-server.

## Historie

* **Předchůdci databází** – klasické kartotéky organizované podle určitých kritérií (napž. abecedy), které vyžadovaly manuální správu a vyhledávání.
* **Mechanická řešení** – děrné štítky, které byly použity například v roce 1890 při sčítání lidu v USA.
* **Nástup počítačů** – protože strojový kód byl pro složité operace nedostatečný, vznikly první programovací jazyky vhodné pro práci s daty (např. COBOL).
* **První databáze** – objevují se kolem roku 1965 na sálových počítačích (mainframe).
* **70. léta** – intenzivní vývoj databázových modelů pracovními skupinami, vznik prvních relačních databází a zavedení dotazovacího jazyka SQL.

## Dělení databází

### Podle způsobu ukládání dat a vazeb

* **Hierarchické databáze** (považováno za historický model):
  * Data jsou uspořádána ve stromové struktuře (podobně jako složky v počítači, kde jedna složka může obsahovat více podsložek a postupně se větvit).
* **Síťové databáze** (považováno za historický model):
  * Data jsou uspořádána v síťové struktuře (na rozdíl od hierarchického modelu umožňuje záznamu mít více nadřazených prvků).
* **Relační databáze**:
  * Data jsou uložena v tabulkách, které jsou vzájemně propojeny pomocí vztahů (relací).
* **Objektové databáze** (považováno za historický model):
  * Informace jsou reprezentovány přímo ve formě objektů (podobně jako v objektově orientovaném programování), což je vhodné pro komplexní data.
* **Objektově-relační databáze**:
  * Kombinují relační model (data v tabulkách) s principy objektově orientovaného programování (možnost definovat vlastní datové typy a metody).

### Podle struktury dat a dotazovacího jazyka

* **SQL databáze**:
  * Využívají strukturovaný dotazovací jazyk SQL.
  * Jedná se o relační databáze.
  * Skvělé pro aplikace vyžadující vysokou integritu dat a složité transakční operace.
* **NoSQL databáze**:
  * Nerelační databáze (např. dokumentové jako MongoDB, kde jsou data uložena ve formátu podobném JSON).
  * Vhodné pro velmi velké objemy nestrukturovaných dat a rychlé, jednodušší operace.

## Relační databáze

* Data jsou uložena v tabulkách, kde **sloupce** představují vlastnosti (atributy) a **řádky** představují konkrétní záznamy.
* Pro propojení a identifikaci se používají klíče:
  * **Primární klíč** (primary/private key, PK) – jednoznačný identifikátor záznamu v tabulce, často reprezentovaný unikátním číslem.
  * **Cizí klíč** (foreign key, FK) – odkazuje na primární klíč v jiné tabulce a realizuje tak propojení mezi nimi.

### Zjednodušený příklad modelu

**Lidé**

| ID člověka (PK) | Jméno | Email |
| :---- | :---- | :---- |
| 1 | Pepa Novák | pepa.novak@example.com |
| 2 | Ivan Ištván | ivan.istvan@example.com |
| 3 | Jaroslav Jaroměř | jaroslav.jaromer@example.com |

**Domácí zvířátko**

| ID druhu (PK) | Název | Mazel |
| :---- | :---- | :---- |
| 1 | Kočka | false |
| 2 | Pes | true |

**Vlastníci zvířátek**

| ID vztahu (PK) | ID člověka (FK) | ID druhu (FK) |
| :---- | :---- | :---- |
| 1 | 2 | 1 |
| 2 | 1 | 2 |
| 3 | 2 | 2 |

*Z tohoto modelu lze vyčíst: Pepa vlastní psa, Ivan vlastní kočku i psa, Jaroslav nevlastní žádné domácí zvířátko.*

### ER diagram a jeho součásti

Pro popis tabulek a jejich vztahů se používá **ER diagram** (*Entity-Relationship diagram*).

* **Entita** – skupina objektů reálného světa (např. *Zvíře*, *Člověk*). Identifikací entity je název tabulky.
* **Instance entity** – konkrétní objekt (např. *kočka*, *Pepa*). Představuje záznam (řádek) v tabulce. Identifikací instance entity je primární klíč.
* **Atributy (vlastnosti)** – definují sloupce tabulky (např. *barva očí*).
* **Hodnota atributu** – konkrétní hodnota v dané buňce (např. *modrá*).

### Typy vztahů (relací)

Vztahy slouží ke svázání entit. Rozlišujeme:

* **Vztah 1:N (jeden k mnoha)**:
  * Člověk si může půjčit více knih, ale každá konkrétní kniha může být v daný moment půjčena pouze jednomu člověku.
  * Příklad: Josef Novák vlastní knihy *Fimfárum* a *Odysea*.
* **Vztah 1:1 (jeden k jednomu)**:
  * Člověk má právě jeden platný občanský průkaz a tento průkaz patří právě jednomu člověku.
  * Příklad: Josef Novák – občanský průkaz Josefa Nováka.
* **Vztah M:N (mnoho k mnoha)**:
  * Pacient chodí k více lékařům a lékař ošetřuje více pacientů.
  * Relační databáze neumožňují přímý vztah M:N. Je nutné jej rozložit pomocí pomocné (vazební) tabulky obsahující cizí klíče (FK) odkazující na obě hlavní tabulky (např. tabulka *Vlastníci zvířátek* spojující *Lidi* a *Domácí zvířátka*).
* **Bez vztahu**:
  * Entity spolu nijak nesouvisí.

Cizí klíče (FK) se používají k tomu, aby se zabránilo duplicitnímu ukládání dat. K propojení tabulek a získání kompletních dat se pak v dotazech SQL používá klíčové slovo **JOIN**.

## Integrita dat

* Zajišťuje, že data jsou uložena podle předem definovaných pravidel a nedojde k jejich poškození či nekonzistenci.
* **Integritní omezení**:
  * **Entitní integrita** – dvě entity (řádky) v jedné tabulce nesmí mít stejný primární klíč (PK). PK musí být unikátní a nesmí být NULL.
  * **Doménová integrita** – hodnoty ve sloupcích musí odpovídat definovaným datovým typům a povoleným rozsahům.
  * **Referenční integrita** – zajišťuje konzistenci mezi provázanými tabulkami. Pokud cizí klíč (FK) odkazuje na hodnotu v jiné tabulce, tato hodnota (primární klíč) musí existovat.
  * **Aktivní referenční integrita** – definuje chování při pokusu o smazání nebo změnu dat, na která odkazují jiné tabulky (např. kaskádové smazání `ON DELETE CASCADE` nebo nastavení na `NULL`).

## Příklady známých databází

* **PostgreSQL** – robustní open-source objektově-relační databázový systém.
* **MySQL** – velmi populární open-source relační databáze, široce používaná pro webové aplikace.
* **MongoDB** – populární NoSQL dokumentová databáze, kde se data ukládají ve formátu JSON/BSON.
* **Microsoft SQL Server** – komerční relační databázový systém vyvíjený společností Microsoft.
* **Oracle Database** – robustní komerční multi-modelový systém pro správu podnikových databází.
* **SQLite** – extrémně lehká relační databáze, která nevyžaduje běžící server a ukládá celou databázi do jednoho souboru.
* **Redis** – in-memory úložiště datových struktur, extrémně rychlé, využívané jako databáze, cache nebo message broker (zprostředkovatel zpráv).

## Zdroje

* WEISER, Martin. *18 - Databáze.docx*. Praha: Gymnázium Litoměřická.
* Databáze. In: *Wikipedie* [online]. 2026 [cit. 15.02.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Datab%C3%A1ze&oldid=25613451](https://cs.wikipedia.org/w/index.php?title=Datab%C3%A1ze&oldid=25613451)
* NoSQL. In: *Wikipedie* [online]. 2023 [cit. 15.02.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=NoSQL&oldid=23031616](https://cs.wikipedia.org/w/index.php?title=NoSQL&oldid=23031616)
* Object–relational database. In: *Wikipedia* [online]. 2025 [cit. 15.02.2026]. Dostupné z: [https://en.wikipedia.org/w/index.php?title=Object%E2%80%93relational_database&oldid=1317276523](https://en.wikipedia.org/w/index.php?title=Object%E2%80%93relational_database&oldid=1317276523)
* Objektová databáze. In: *Wikipedie* [online]. 2025 [cit. 15.02.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Objektov%C3%A1_datab%C3%A1ze&oldid=25416341](https://cs.wikipedia.org/w/index.php?title=Objektov%C3%A1_datab%C3%A1ze&oldid=25416341)
* Relační databáze. In: *Wikipedie* [online]. 2025 [cit. 15.02.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Rela%C4%8Dn%C3%AD_datab%C3%A1ze&oldid=25315190](https://cs.wikipedia.org/w/index.php?title=Rela%C4%8Dn%C3%AD_datab%C3%A1ze&oldid=25315190)
