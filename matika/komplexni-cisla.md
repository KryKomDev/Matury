# Komplexní čísla

## Zápisy

- **obecný tvar**: $z= a + bi, \{a; b\} \in \mathbb{R}, i = \sqrt{-1}$
- **goniometrický tvar**: $z = |z|(cos(\varphi) + i \cdot sin(\varphi))$
  - $cos(\varphi) = \frac{a}{|z|} \land sin(\varphi) = \frac{b}{|z|}$

> [!NOTE]
> komplexní číslo lze interpretovat jako vektor v gaussově rovině, kde $a$ je
> velikost po ose $x$, a $b$ je velikost po ose $y$

## Operace

- **sčítání** a **odčítání** stejné jako pro vektory
- **násobení**: $z_1 \cdot z_2 = (a_1 + b_1 i) \cdot (a_2 + b_2 i) = a_1 a_2 + a_1 b_2 i + b_1 a_2 i - b_1 b_2$
- **velikost** $z$: $|z| = \sqrt{a^2 + b^2}$
- **komplexně sdružené číslo** ze $z$: $\overline{z} = a - bi$

## Moivreova věta

- $z^n = |z|^n (cos(\varphi n) + i \cdot sin(\varphi n))$

## Řešení rovnic

### Kvadratické rovnice

#### a) s reálnými koeficienty

- řešíme pomocí vzorečku
- pokud determinant vyjde záporný, pouze přidáme $i$

#### b) s komplexními koeficienty

- řešíme pomocí moivreovy věty

### Binomické rovnice

- zadána jako: $z - x^n = 0$ 
- kořeny: $x_k = \sqrt[n]{|z|}(cos(\frac{\varphi 2 \pi k}{n}) + i \cdot sin(\frac{\varphi 2 \pi k}{n})), k \in \{0; 1; 2; ... ; n - 1\}$