#!/usr/bin/python3.7
# -*-coding:Utf-8 -*

import json #permet d'afficher facilement les dictionnaires via la commande print()

class DictionnaireOrdonne():
    """TLV 05/10/2019
    Classe faisant l'équivalent d'un dictionnaire, mais avec des méthodes sort() et reverse()
    permettant de faire des tris par clé
    Par défaut, le dictionnaire d'une instance est vide"""
    def __init__(self, dicodefaut=dict(), **kwargs):
        """Constructeur : par défaut, l'attribut est un dictionnaire vide
        Ou alors un dictionnaire déjà fait passé en paramètre
        Ou alors un dictionnaire fait à partir des valeurs de celui-ci passées en paramètre"""
        if len(kwargs) == 0:
        #S'il n'y a qu'une seule valeur du type dictionnaire passée en paramètre
        #Alors la valeurs de kwarg est {}. On vérifie donc la longueur pour
        #mettre le dictionnaire par defaut dans cette situation
            self.listecles = list(dicodefaut.keys())
            self.listevaleurs = list(dicodefaut .values())
        else:
        #kwargs est un dico des valeurs passées en paramètre
        #Utile lorsqu'on veut passer plusieurs paramètres d'affilée
            self.listecles=list(kwargs.keys())
            self.listevaleurs=list(kwargs.values())


    def __str__(self):
        """Afficher élégamment l'objet dans l'interpréteur comme demandé dans la spécification
        json.dumps permet d'afficher le dictionnaire avec print() via str"""
        dictionnaireAffichage = dict(zip(self.listecles, self.listevaleurs))
        return json.dumps(dictionnaireAffichage)

    def __getitem__(self,index):
        """Méthode appelée quand on fait objet[index]"""
        if index in self.listecles:
            return self.listevaleurs[self.listecles.index(index)]

    def __setitem__(self, index, valeur):
        """Méthode appelée pour faire objet[index]=valeur
        Si l'index n'existe pas, on fait du append
        S'il existe déjà dans les index, on màj la valeur existante"""
        if index not in self.listecles:
            self.listecles.append(index)
            self.listevaleurs.append(valeur)
        else:
            self.listevaleurs[self.listecles.index(index)] = valeur

    def __delitem__(self,index):
        """Méthode appelée pour faire del objet[cle]"""
        if index in self.listecles:
            #On supprime d'abord dans la liste des valeurs
            del self.listevaleurs[self.listecles.index(index)]
            #Puis on supprime la valeur correspondant à l'indice trouvé
            self.listecles.remove(index)

    def __contains__(self,index):
        if index in self.listecles:
            return True
        else:
            return False

    def __len__(self):
        return len(self.listecles)

    def __add__(self, dico_a_ajouter):
        """Gestion de l'addition : Pour d1 et d2 deux dictionnaires ordonnes,
        faire d1 + d2 ajoute les clés et valeurs de d2 à d1"""
        d3 = DictionnaireOrdonne()
        d3.listecles = self.listecles + dico_a_ajouter.listecles
        d3.listevaleurs = self.listevaleurs + dico_a_ajouter.listevaleurs
        return d3

    def reverse(self):
        #inverse les éléments du dictionnaire ordonné
        self.listecles.reverse()
        self.listevaleurs.reverse()
        return self

    def sort(self):
        #trie les éléments du dictionnaire par clé
        #Utilisation d'un dictionnaire intermédiaire pour conserver les liaisons avec les clés
        dicoIntermediaire=dict(zip(self.listecles, self.listevaleurs))
        self.listecles.sort()
        for i in range(0,len(self.listecles)):
            self.listevaleurs[i] = dicoIntermediaire[self.listecles[i]]
        return self

    def keys(self):
        return self.listecles

    def values(self):
        return self.listevaleurs

    def __iter__(self):
        """Itération sur la liste des clés en faisant un for, comme spécifié"""
        return iter(self.listecles)

    def items(self):
        """retourne les clés et valeurs du dictionnaire"""
        for i, cle in enumerate(self.listecles):
            valeur=self.listevaleurs[i]
            yield (cle,valeur) #On retourne simplement comme ça les couples clé valeur


print('Initialisation de fruits')
fruits = DictionnaireOrdonne()
print(fruits)
print('Ajouts des clés pomme, poire, prune et melon avec pour quantités respectives 52, 34, 128 et 15')
fruits['pomme'] = 52
fruits['poire'] = 34
fruits['prune'] = 128
fruits["melon"] = 15
print(fruits)
print('Tri des fruits')
fruits.sort()
print(fruits)
print('Initialisation de legumes')
legumes = DictionnaireOrdonne(carotte = 26, haricot = 48)
print(legumes)
print('Taille de legumes')
print(len(legumes))
print('Inversion de legumes')
legumes.reverse()
print(legumes)
print('Ajout des legumes aux fruits')
fruits = fruits + legumes
print(fruits)
print('Suppression des haricots')
del fruits['haricot']
print('haricot est-il dans fruits ?')
print('haricot' in fruits)
print('Affichage de la quantité associée à haricot dans legumes')
print(legumes['haricot'])
print('Affichage de tous les légumes')
for cle in legumes:
    print(cle)
print('Clés de legumes')
print(legumes.keys())
print('Valeurs de legumes')
print(legumes.values())
print('Affichage simultané des noms et quantités des légumes')
for nom, qtt in legumes.items():
    print("{0} ({1})".format(nom, qtt))
