#!/usr/bin/python3.6
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
            self.listevaleurs = list(dicodefaut.values())
        else:
        #kwargs est un dico des valeurs passées en paramètre 
        #Utile lorsqu'on veut passer plusieurs paramètres d'affilée
            self.listecles=list(kwargs.keys())
            self.listevaleurs=list(kwargs.values())   


    def __str__(self):
        """Afficher élégamment l'objet dans l'interpréteur comme demandé dans la spec
        json.dumps permet d'afficher le dictionnaire avec print() via str"""
        dictionnaireAffichage = dict(zip(self.listecles, self.listevaleurs))
        return json.dumps(dictionnaireAffichage)
        #On pouvait aussi utiliser repr de la manière astucieuse d'OpenClassrooms, en utilisant
        #les repr() déjà existant des listes

        
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
        return d3 #Une autre manière de faire un peu plus robuste, notamment si des cles sont communes entre les deux dictionnaires,  a été proposée en correction
        
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
        #Une manière plus astucieuse sans utiliser dict(zip) a été proposée dans la correction, en utilisant getitem() déjà définie 

    def keys(self):
        return self.listecles
    
    def values(self):
        return self.listevaleurs

    def __iter__(self):
        """Itération sur la liste des clés en faisant un for, comme spécifié"""
        #return ItDictionnaireOrdonne(self.listecles)
        #On pouvait simplement retourner l'itérateur des clés, à la :
        return iter(self.listecles)

    def items(self):
        """retourne les clés et valeurs du dictionnaire"""
        #self.indicedebutdico = 1
        #while (self.indicedebutdico) < len(self.listecles):
        #    yield(self.listecles[self.indicedebutdico])         
        #dictionnaireAffichage = dict(zip(self.listecles, self.listevaleurs))
        #return dictionnaireAffichage.items()
        for i, cle in enumerate(self.listecles):
            valeur=self.listevaleurs[i]
            yield (cle,valeur) #On retourne simplement comme ça les couples clé valeur

#Itérateur inutile
class ItDictionnaireOrdonne:
    """Un itérateur permettant de parcourir la liste des clés dans le dictionnaire si on fait 
    for cle in dictionnaire'. Il paraît qu'on pourrait utiliser un générateur, mais je n'ai 
    toujours pas bien compris comment un générateur pourrait remplacer un itérateur dans cette
    situation."""
    def __init__(self, liste_des_cles):
        self.liste_des_cles = liste_des_cles
        self.position = -1

    def __next__(self):
        """Parcours des clés"""
        #print('parkour')
        if (self.position + 1)  == len(self.liste_des_cles):
            raise StopIteration
        self.position += 1 #On avance d'un cran dans la liste des clés
        return self.liste_des_cles[self.position]
        

    



#main
print('Test d\'une initialisation vide')
fruits = DictionnaireOrdonne()
print(fruits)
print('Test d\'une initialisation avec un dictionnaire en paramètre')
fruits2={}
fruits2["pseudo"]="Peterkolios"
fruits2["mot de passe"]="Oranges"
fruits3=DictionnaireOrdonne(fruits2)
print(fruits3)
print('Test de plusieurs arguments')
fruits4 = DictionnaireOrdonne(a='orange',b='nectarine')
print(fruits4)
print('Test de getitem')
print(fruits4['a'])
print('Test de setitem')
fruits4['c']='pomme'
print(fruits4)
fruits4['b']='mandarine'
print(fruits4)

print('Suppression de la mandarine')
del fruits4['b']
print(fruits4)

#print('b' in fruits4)
#print('Longueur du dico actuellement :')
#print(len(fruits4))

#print('Test d\'un parcours itératif')
#for cle in fruits4:
#    print(cle)
#    print(fruits4[cle])

print('Test d\'une addition')
print('fruits4')
print(fruits4)
print('fruits3')
print(fruits3)
fruits5=fruits4+fruits3
print('somme')
print(fruits5) #Le remplacement de clés déjà existantes est fait grâce à print()
print('Test d\'inversion')
fruits5.reverse()
print(fruits5)
print('Test de tri')
fruits6=fruits5.sort()
print(fruits6)
print('Affichage des clés')
print(fruits6.keys())
print('Affichage des valeurs')
print(fruits6.values())

print('Test de la boucle for')
for cle in fruits6:
    print(cle)

print('test items')
for cle, valeur in fruits6.items():
    print("Clé {} contient valeur {}.".format(cle,valeur))
