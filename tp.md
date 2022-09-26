# TP 0 - Programme en ligne de commande

Le but de ce TP est de se familiariser avec des notions qui seront utiles pour la suite :

- distances sémantiques à l'exécution et à l'interprétation, illustrées sur le cas d'un programme en ligne de commande
- modèle graphique vectoriel.

---

## Python

Si vous souhaitez travailler sur votre machine personnelle, vous pouvez télécharger une distribution de Python adaptée à votre système. Le but de ce TP n'est pas d'apprendre Python, néanmoins, si cela vous intéresse, vous pouvez consulter cette introduction à Python 2 ou mon [cours sur Python 3](http://iihm.imag.fr/blanch/teaching/python3/).

---

## Ligne de commande

Récupérez le programme trace.py. Rendez-le exécutable et testez-le.

```bash
mandelbrot:~> chmod a+x trace.py
mandelbrot:~> ./trace.py
mandelbrot:~> ./trace.py "sin(x)"
x, sin(x)
0.0, 0.0
0.1, 0.0998334166468
0.2, 0.198669330795
0.3, 0.295520206661
0.4, 0.389418342309
0.5, 0.479425538604
0.6, 0.564642473395
0.7, 0.644217687238
0.8, 0.7173560909
0.9, 0.783326909627
1.0, 0.841470984808
```

1. En quoi consistent les distances sémantiques à l'exécution et à l'interprétation pour ce programme ?

- Un utilisateur lambda ne saura comment utiliser ce programme car il n'y a aucune indication

2. Réduisez la distance sémantique à l'exécution en gérant mieux les erreurs, et en fournissant un message indiquant comment utiliser le programme.


3. Enrichissez le programme en permettant le passage d'autres paramètres par la ligne de commande (xmin, xmax, etc.)


---
## Graphique 2D

Les interfaces graphiques utilisent un modèle graphique permettant de dessiner à l'écran. En dehors d'usages particuliers, ce modèle est à deux dimensions (2D) et utilise une géométrie affine. Pour nous familiariser avec ce type de modèle, nous allons utiliser le langage [PostScript](http://www.adobe.com/products/postscript/).

4. Familiarisez-vous avec le langage PostScript en suivant cette [introduction à PostScript](http://iihm.imag.fr/blanch/howtos/PostScript.html).

### Sortie graphique