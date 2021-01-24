# TP du dictionnaire ordonné - OpenClassrooms - Formation Python

TP du dictionnaire ordonné proposé par OpenClassrooms, dans le cadre de sa formation sur le langage Python :
https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/233322-tp-realisez-un-dictionnaire-ordonne

Ce TP consiste à créer une nouvelle classe imitant le fonctionnement d'un dictionnaire, mais sur lequel il est possible des
tris et des inversions.
Pour ce faire, les méthodes `sort` et `reverse` ont été définies en triant le dictionnaire en fonction des clés.

La version de Python utilisée dans le cadre de ce TP est la version 3.7.
Après avoir cloné ce projet, celui-ci peut être exécuté en exécutant les commandes suivantes à la racine:

```
chmod 700 dictionnaire_ordonne.py
./dictionnaire_ordonne.py
```

Ce qui permettra d'afficher dans la console les résultats de quelques lignes de code Python
permettant de tester le bon fonctionnement de ce dictionnaire ordonné :

```
Initialisation de fruits
{}
Ajouts des clés pomme, poire, prune et melon avec pour quantités respectives 52, 34, 128 et 15
{"pomme": 52, "poire": 34, "prune": 128, "melon": 15}
Tri des fruits
{"melon": 15, "poire": 34, "pomme": 52, "prune": 128}
Initialisation de legumes

{"carotte": 26, "haricot": 48}
Taille de legumes
2
Inversion de legumes
{"haricot": 48, "carotte": 26}
Ajout des legumes aux fruits
{"melon": 15, "poire": 34, "pomme": 52, "prune": 128, "haricot": 48, "carotte": 26}
Suppression des haricots
haricot est-il dans fruits ?
False
Affichage de la quantité associée à haricot dans legumes
48
Affichage de tous les légumes
haricot
carotte
Clés de legumes
['haricot', 'carotte']
Valeurs de legumes
[48, 26]
Affichage simultané des noms et quantités des légumes
haricot (48)
carotte (26)
```
