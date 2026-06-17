# Základy HTML, CSS a JS

## Osnova

* Struktura webové stránky
* Základní HTML elementy
* Základní CSS parametry
* Základy JavaScriptu

## Struktura webové stránky

```html
<!doctype html>  
<html lang="cs">  
<head>  
   <meta charset="UTF-8">  
   <meta name="viewport"  
         content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">  
   <meta http-equiv="X-UA-Compatible" content="ie=edge">  
   <title>Nadpis stránky</title>  
</head>  
<body>  
<strong>Ahoj!</strong>  
</body>  
</html>
```

* `<!DOCTYPE html>` napovídá programu, v jakém formátu je tento XML/HTML dokument (moderní HTML5 staví na zjednodušeném zápisu doctype).
* Stránka je celá obklopena párovým elementem `<html>`.
* Element `<head>` obsahuje metadata (kódování, nastavení viewportu atd.), `<title>` (název stránky zobrazený v záložce prohlížeče) a také odkazy na externí styly či skripty:

```html
<link rel="stylesheet" href="style.css">
```

* V `<body>` (těle stránky) je zapsán HTML kód, který bude prohlížečem vykreslen na obrazovku.
* Tato ukázka by se vykreslila jako:

<pre>
——————————————————————
| Nadpis stránky   x |
————————————————————————————————

<strong>Ahoj!</strong>

————————————————okno prohlížeče
</pre>

## Základní HTML elementy

* HTML dokument má stromovou strukturu (DOM).
* Elementy mohou obsahovat vnořené elementy (děti), čímž se strom dále větví:
  * Příklad: `<div><h1>Nadpis</h1><p>Paragraf</p></div>` tvoří strukturu, kde `div` je rodičem pro `h1` a `p`.
* Základní jednotkou stránky jsou [HTML elementy](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements) vymezené tagy:
  * Zápis začátku elementu: `<tagname>`, konec elementu: `</tagname>`.
  * Samouzavíratelné elementy (např. `<input>`, `<img>`): nemají ukončovací tag ani vnitřní obsah.
  * Atributy definují vlastnosti elementů (např. u `<input>` atribut `type` určuje typ vstupu – text, číslo, tlačítko).
* **Nadpisy**:
  * [<h1> až <h6>](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements) (headings).
  * Číslo označuje úroveň nadpisu, přičemž `<h1>` je největší (hlavní nadpis) a `<h6>` nejmenší.
* **Paragrafy**:
  * [<p>](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p) (paragraph).
  * Zápis: `<p>Toto je paragraf textu</p>`.
* **Hypertextové odkazy**:
  * [<a>](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a) (anchor).
  * Povinný atribut `href` určuje cílovou adresu odkazu.
  * Nepovinný atribut `target` určuje, kde se odkaz otevře (např. `_blank` pro nový panel; bez uvedení se otevře v aktuálním).
* **Obrázek**:
  * [<img>](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img).
  * Povinný atribut `src` udává URL cestu k obrázku a `alt` obsahuje alternativní text pro čtečky obrazovky.
  * Rozměry lze definovat v CSS nebo nepovinnými atributy `width` a `height` (např. `<img src="/logo.png" alt="logo" width="100" height="100">`).
* **Strukturální elementy**:
  * `<header>`: záhlaví stránky, obvykle obsahuje logo, název a hlavní navigaci.
  * `<main>`: hlavní a jedinečný obsah konkrétní stránky, se kterým uživatel interaguje.
  * `<footer>`: zápatí stránky, obsahuje kontaktní údaje, autorská práva či odkazy na smluvní podmínky.
* **Další sémantické a stylové elementy**:
  * `<section>`: tematická sekce dokumentu, zpravidla by měla obsahovat nadpis.
  * `<article>`: samostatný a nezávislý článek nebo příspěvek vhodný k distribuci.
  * `<aside>`: boční panel nebo obsah nepřímo související s hlavním textem.
  * `<div>`: univerzální blokový kontejner pro seskupení prvků (často stylovaný pomocí CSS).
  * `<span>`: univerzální řádkový (inline) kontejner pro stylování části textu.
* **Důležité globální atributy**:
  * `class`: zařazení do tříd pro stylování pomocí CSS.
  * `id`: unikátní identifikátor elementu (vhodné pro JavaScript a jako cíl odkazu, např. `/o-nas#mapa` odroluje k id `mapa`).
  * `value`: hodnota u formulářových prvků (např. u `<input>`).
  * `name`: název elementu odesílaný na server při odeslání formuláře.

## Základní CSS parametry

* CSS (Cascading Style Sheets) slouží ke stylování elementů.
* Většina vlastností se v DOM struktuře dědí od rodičů na potomky.
* Základní syntaxe:

```css
selektor {  
    atribut: hodnota;  
    atribut: hodnota;  
}
```

* **Selektory** určují, na které elementy se styl aplikuje:
  * `tagname`: název elementu (např. `body`).
  * `.class`: třída elementu (např. `.blue`). Lze kombinovat (např. `button.blue` vybere `<button class="blue">`).
  * `#id`: unikátní identifikátor elementu (např. `#hlavni-nadpis`).
* **Pseudotřídy a pseudoelementy** (začínají dvojtečkou `:`):
  * `:root`: představuje kořen dokumentu (vrchol dědičnosti).
  * `:nth-child(n)`: vybere n-té dítě (např. `:nth-child(even)` pro sudé řádky).
  * `:before` a `:after`: umožňují vložit a stylovat obsah před nebo za element.
* **Media queries** (`@media`) slouží k přizpůsobení stylů parametrům zobrazovacího zařízení (počítač, telefon, tisk):
  * `@media print`: styl pro tištěnou verzi stránky.
  * `@media screen`: styl pro obrazovky.
  * `@media screen and (max-width: 400px)`: specifikuje pravidla pro obrazovky užší než 400 pixelů.

```css
/* Šedá barva pozadí pro obrazovky užší než 400px */
@media screen and (max-width: 400px) {  
    body {  
        background-color: lightgrey;  
    }  
}
```

* **Vybrané CSS vlastnosti**:
  * `color`: barva textu (lze zadat jako název, hexadecimální kód či RGB, např. `color: red;`, `color: rgb(255, 0, 0);`, `color: #FF0000;`).
  * `background-color`: barva pozadí.
  * `font-size`: velikost písma (např. `font-size: 12pt;`, `font-size: 2em;`, `font-size: 10px;`).
  * `border`: nastavení ohraničení elementu.

## Základy JavaScriptu

* JavaScript (JS) je **skriptovací programovací jazyk**, který umožňuje interaktivitu na webových stránkách.
* Běží hlavně na straně klienta (v prohlížeči), ale existuje i serverová varianta (např. Node.js).
* Propojuje HTML (strukturu) a CSS (styl) a přidává dynamické chování.

### Syntaxe

* **Proměnné**:
  * Deklarace pomocí `let` (měnitelná hodnota) nebo `const` (konstanta, neměnná hodnota).
  * Příklad: `const jmeno = "Jan";` nebo `let vek = 30;`
  * Starší způsob `var` se dnes nedoporučuje kvůli chování rozsahu platnosti proměnných (scoping).
* **Datové typy**:
  * Základní (primitivní) typy zahrnují `string` (text), `number` (čísla), `boolean` (pravda/nepravda), `null` a `undefined`.
  * Složitější typy jsou `object` (objekty, pole) a `function` (funkce).
* **Příkazy a středníky**:
  * Každý příkaz je obvykle ukončen středníkem `;`. V moderním JS to sice není vždy striktně vyžadováno, ale jedná se o doporučený osvědčený postup.
  * Příklad: `console.log("Ahoj světe");`
* **Komentáře**:
  * Jednořádkové komentáře začínají `//`.
  * Víceřádkové komentáře jsou uzavřeny mezi `/*` a `*/`.
* **Funkce**: Blok kódu, který lze opakovaně volat.

```javascript
function pozdrav(jmeno) {
    return "Ahoj, " + jmeno + "!";
}

pozdrav("Jan"); // Volání funkce
```

* **Podmínky a cykly**:
  * Podmínky se zapisují pomocí `if`, `else if` a `else`.
  * Pro cykly se využívají konstrukce `for` a `while`.

### DOM queries (dotazování na dokument)

* **DOM (Document Object Model)** je programové rozhraní pro webové dokumenty. Reprezentuje stránku jako stromovou strukturu, kde každý element je uzlem.
* JS používá DOM pro přístup k HTML elementům a pro jejich manipulaci (změna obsahu, stylů, přidávání či odebírání elementů).
* Základní vyhledávací metody:
  * `document.getElementById("id_elementu")`: Vyhledá jeden konkrétní element podle jeho unikátního ID.
  * `document.querySelector(".trida_elementu")`: Vyhledá **první** vyhovující element odpovídající zadanému CSS selektoru (třída, ID, tag atd.).
  * `document.querySelectorAll("p")`: Vyhledá **všechny** vyhovující elementy a vrátí je jako seznam uzlů (`NodeList`).

### Události (events)

* Události jsou akce probíhající v prohlížeči (např. kliknutí myší, stisk klávesy, načtení celé stránky).
* JavaScript umožňuje na tyto události reagovat spuštěním kódu (tzv. **obsluha událostí** - event handler).
* **Registrace obsluhy události**:
  * Nejčastěji se realizuje pomocí metody `addEventListener()`.
  * Syntaxe: `element.addEventListener('typ_udalosti', funkce_obsluhy);`

### Příklad – stisknutí tlačítka

```javascript
const tlacitko = document.querySelector('#mojeTlacitko');

// Připojení obsluhy pro událost kliknutí (click)
tlacitko.addEventListener('click', function() {
    // Kód, který se spustí po kliknutí
    alert('Tlačítko bylo stisknuto!');
});
```

* **Běžné typy událostí**:
  * `click`: kliknutí tlačítkem myši.
  * `mouseover` / `mouseout`: najetí myši na element a odjetí z něj.
  * `keydown` / `keyup`: stisknutí a uvolnění klávesy na klávesnici.
  * `submit`: odeslání HTML formuláře.
  * `load`: dokončení načítání celého dokumentu.

## Zdroje

* CSS Tutorial. In: [cit. 05.01.2026]. Dostupné z: [https://www.w3schools.com/css/default.asp](https://www.w3schools.com/css/default.asp)
* HTML Elements. In: [cit. 05.01.2026]. Dostupné z: [https://www.w3schools.com/html/html_elements.asp](https://www.w3schools.com/html/html_elements.asp)
* HTML elements reference - HTML | MDN. In: *MDN Web Docs* [online]. 9. 11. 2025 [cit. 05.01.2026]. Dostupné z: [https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements)
* HTML5. In: *Wikipedie* [online]. 2025 [cit. 31.12.2025]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=HTML5&oldid=25256119](https://cs.wikipedia.org/w/index.php?title=HTML5&oldid=25256119)
* JavaScript Tutorial. In: [cit. 05.01.2026]. Dostupné z: [https://www.w3schools.com/js/default.asp](https://www.w3schools.com/js/default.asp)
* Representational State Transfer. In: *Wikipedie* [online]. 2025 [cit. 31.12.2025]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Representational_State_Transfer&oldid=25220688](https://cs.wikipedia.org/w/index.php?title=Representational_State_Transfer&oldid=25220688)
* Web Applications. In: *Web Applications* [online] [cit. 31.12.2025]. Dostupné z: [https://spring.io/web-applications](https://spring.io/web-applications)
* Webová aplikace. In: *Wikipedie* [online]. 2025 [cit. 31.12.2025]. Dostupné z: [https://cs.wikipedia.org/w/index.php?title=Webov%C3%A1_aplikace&oldid=25474761](https://cs.wikipedia.org/w/index.php?title=Webov%C3%A1_aplikace&oldid=25474761)