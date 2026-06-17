# Základy SQL

## Osnova

* Co to je SQL?
* Historie
* Základní syntaxe:
  * SELECT
  * CREATE TABLE
  * UPDATE
  * DELETE
  * INSERT

## Co to je SQL?

* **Structured Query Language** (strukturovaný dotazovací jazyk).
* Jazyk, pomocí kterého se můžeme dotazovat relační databáze na data.
* Můžeme jím data také modifikovat, vytvářet nové položky, tabulky, pohledy atd.
* Databázové systémy běžně podporují správu uživatelů a oprávnění z bezpečnostních důvodů:
  * Oprávnění se dělí např. na čtení (READ), zápis (WRITE) a správu (ADMIN/DDL – tvoření a úprava struktur).
* SQL využívají databázové systémy jako MySQL, PostgreSQL, SQLite, MS SQL Server, Oracle atd.
* Jazyk je **deklarativní** – definujeme pouze to, jakých výsledků chceme dosáhnout (co se má stát), nikoliv konkrétní algoritmus, jakým se k nim databázový stroj dobere.
* Používá se pro relační databáze.

## Historie

* Navrženo na začátku 70. let 20. století v IBM.
* V průběhu 70. a 80. let probíhal intenzivní vývoj a rozšiřování.
* Na přelomu 80. a 90. let proběhla první oficiální standardizace (standardy SQL-86, SQL-89, SQL-92 atd.).

## Základní syntaxe

* Nejdřív musíme vědět, jakou operaci chceme provést:
  * **Výběr dat**: `SELECT`
  * **Odstranění záznamu**: `DELETE`
  * **Úprava (přepsání) záznamu**: `UPDATE`
  * **Vložení nového záznamu**: `INSERT`
  * **Vytvoření nového objektu (např. tabulky)**: `CREATE TABLE`

### Vytvoření tabulky

Při vytváření tabulky se definují jednotlivé sloupce, jejich datové typy a případná omezení (constraints).

```sql
CREATE TABLE [databáze.]název (
    vlastnost datový_typ omezení,
    ...
);
```

Příklad vytvoření tabulky uživatelů:

```sql
CREATE TABLE users (
    userid number AUTOINCREMENT NOT NULL,
    jmeno text NOT NULL,
    email text NOT NULL
);
```

### Získání dat (SELECT)

Základní výběr specifických sloupců z tabulky:

```sql
SELECT sloupec1, sloupec2, ... FROM tabulka;
```

Příklad:

```sql
SELECT id, jmeno, email FROM users;
```

Výběr dat s filtrem (podmínkou):

```sql
SELECT sloupec1, sloupec2, ... FROM tabulka WHERE podmínka;
```

Příklad vyhledání uživatele podle jména:

```sql
SELECT jmeno, id, email FROM users WHERE jmeno = 'Otokar Březina';
```

Spojení dat z více tabulek na základě vazby (relace):

```sql
SELECT sloupec1, sloupec2, ... FROM tabulka JOIN tabulka2 ON podmínka;
```

Příklad vyhledání plodů a jejich typů:

```sql
SELECT id_typu_plodu, jmeno, typy.nazev FROM ovoce
JOIN typy ON typy.id = ovoce.id_typu;
```

### Odstranění záznamu (DELETE)

Smazání konkrétních záznamů podle podmínky:

```sql
DELETE FROM tabulka WHERE podmínka;
```

Příklad:

```sql
DELETE FROM users WHERE id = 85;
```

> [!WARNING]
> Pokud není uvedena klauzule `WHERE` s podmínkou, dojde ke smazání všech dat z tabulky!

* Pro smazání celé struktury tabulky (nikoliv pouze dat v ní obsažených) se používá příkaz `DROP TABLE název;`.

### Úprava záznamu (UPDATE)

Změna hodnot ve stávajících řádcích tabulky:

```sql
UPDATE tabulka SET sloupec1 = hodnota1, sloupec2 = hodnota2, ... WHERE podmínka;
```

Příklad nastavení administrátorských práv uživateli s ID 85:

```sql
UPDATE users SET admin = 1 WHERE id = 85;
```

> [!WARNING]
> Pokud není uvedena klauzule `WHERE` s podmínkou, dojde k úpravě hodnot u všech řádků v tabulce!

### Vložení záznamu (INSERT)

Přidání nového řádku do tabulky:

```sql
INSERT INTO tabulka (sloupec1, sloupec2, ...) VALUES (hodnota1, hodnota2, ...);
```

Příklad:

```sql
INSERT INTO users (name, email) VALUES ('Ivan', 'ivan@example.com');
```

## Zdroje

* SQL. In: *Wikipedie* [online]. 2025 [cit. 29.03.2026]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=SQL&oldid=25479485](https://cs.wikipedia.org/w/index.php?title=SQL&oldid=25479485)
* SQL Tutorial. In: [cit. 29.03.2026]. Dostupné z: [https://www.w3schools.com/sql/](https://www.w3schools.com/sql/)