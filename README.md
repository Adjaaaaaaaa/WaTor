🌊 Projet Wa-Tor – Simulation d'écosystème marin
📁 Structure du projet
WATOR/
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py          # Paramètres de simulation
│   │   ├── fish.py            # Classe de base pour les créatures marines
│   │   ├── shark.py           # Classe Shark (prédateur)
│   │   ├── tuna.py            # Classe Tuna (proie)
│   │   ├── planet.py          # Grille de simulation (monde torique)
│   │   └── simulation.py      # Moteur principal de simulation
│   └── ui/
│       ├── __init__.py
│       └── window.py          # Interface graphique
├── assets/
│   ├── tuna.png               # Image du thon
│   ├── shark.png              # Image du requin
├── main.py                    # Point d'entrée du programme
├── requirements.txt           # Dépendances du projet
🌐 Principe Général
Wa-Tor est une simulation d’écosystème marin où thons (tuna) et requins (sharks) interagissent sur une grille torique (le monde "boucle" sur lui-même comme un globe).

L'objectif est d'observer l'évolution des populations et l'équilibre naturel entre proies et prédateurs.

🐟 Les Thons (Tuna)
Rôle : Proies

Comportement :

Se déplacent aléatoirement vers une case vide voisine.

Se reproduisent après un certain nombre de chronons (TUNA_REPRODUCTION_TIME).

Ne meurent pas de faim.

🦈 Les Requins (Shark)
Rôle : Prédateurs

Comportement :

Cherchent à se déplacer vers une case contenant un thon (qu’ils mangent).

Si aucun thon n’est adjacent, se déplacent vers une case vide.

Se reproduisent après SHARK_REPRODUCTION_TIME.

Meurent de faim.

⏱️ Chronons
Un chronon représente une unité de temps dans la simulation.

À chaque chronon :

Chaque entité agit (déplacement, reproduction, ou mort).

La grille est mise à jour.

Des statistiques peuvent être collectées : nombre de thons, de requins, etc.

🔁 Grille Torique
La grille est fermée sur elle-même :

Aller à droite du bord droit revient à gauche.

Monter au bord supérieur revient en bas.

Cela empêche les entités de sortir de la grille.

🎯 Objectif de la Simulation
Observer les dynamiques de population : croissance, décroissance, extinction.

Analyser l’impact des paramètres :

Taux de reproduction 

Taille de la grille...

Comprendre les équilibres naturels dans un écosystème simple.
📁 Simulation réalisée

![alt text](image.png)