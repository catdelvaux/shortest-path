import numpy as np
import csv as csv

# Algorithme de Dijkstra
def Dijkstra(C: np.matrix) -> np.matrix:
    """
    Trouve les distances les plus courtes sur bases de chaque noeud du graphe via l'algorithme de Dijkstra

    @pre: C, un objet matrice issu de la librairie Numpy. C est une matrice carrée n*n tel que :
        - C[i,j] donne la distance du noeud i vers le noeud j
        - C[i, i] = 0, de part le simple fait que partir d'un noeud vers le même noeud ne coûte rien

    @post: d, un objet matrice issu de la librairie Numpy. D est la matrice des plus cours chemin du graphe
        - d[i,j] donne la distance du plus court chemin de i vers j
        - d[i, i] = 0 pour la même raison que C[i, i] = 0

    """

    n = len(C)

    # Initialisation de la matrice des distances les plus courtes
    # Le 1er arguments utilisés : "np.zeros((n,n)" permet de créer une matrice n*n, où n est la taille de la matrice de coûts C, de 0
    # Le 2ème arguments permet de définir le type de ces 0 comme type float (nombre à virgule flottante)
    d = np.matrix(np.zeros((n,n)), dtype=float)

    # Etant donné que l'algorithme de Dijkstra ne calcul les distances les plus courtes que par rapport à un seul noeud du graphe,
    # la boucle j permet d'appliquer l'algorithme à chaque noeud de manière itérative
    for j in range(n):

        # Initialise le problème de résolution : 
        # L est une liste rempli d'infinie où l'élément de départ = 0 ; 
        # S est le frigo qui contient les noeuds stockés après leur sélection ;
        L = n * [float('inf')]
        S = []
        L[j] = 0

        # Tant que le frigo S ne contient pas tous les noeuds
        while len(S) != n :

            # Recherche du minimum dans la ligne L, néanmoins le minimum ne peut pas avoir été déjà sélectionné (= se trouver dans le frigo S)
            min = float('inf')
            u = float('-inf')
            for i in range(n):
                if L[i] < min and i not in S:
                    u = i
                    min = L[i]

            # Ajout du minimum au frigo (ce qui augmente sa taille)
            S.append(u)

            #Pour chaque noeud qui n'est pas dans le frigo S, va modifier les distances les plus courtes vers chaque noeud
            for v in range(n) :
                if v not in S:
                    # La modification de la distance n'est effectué que si : 
                    # la distance du plus court chemin Lu (vers le minimum qui vient d'être trouvé) + le coût d'aller du noeud u vers le noeud actuel v
                    # est inférieur au plus court chemin contenu dans L vers v
                    if L[u] + C[u,v] < L[v]:
                        L[v] = L[u] + C[u,v]
        
        #Actualise la ligne j avec la matrice des plus court chemin L qui vient d'être calculé
        d[j] = L
    return d


# Algorithme de Bellman Ford
def Bellman_Ford(C: np.matrix) -> np.matrix:
    return None

# Algorithme de Floyd Warshall
def Floyd_Warshall(C: np.matrix) -> np.matrix:
    """
    @pre: C est une matrice n x n de type numpy représentant la matrice de coûts C du graphe 
        - C[i, j] contient le poids de l'arête entre les nœuds i et j, ou np.inf si aucune arête directe n'existe.
        - C[i, i] = 0 pour tous les nœuds i (distance d'un nœud à lui-même).

    @post: Retourne une matrice d (n x n) de type numpy représentant les plus courts chemins entre toutes les paires de nœuds.
        - Pour chaque paire de nœuds (i, j), d[i, j] est la distance minimale entre ces nœuds.
        - Si aucun chemin n'existe entre i et j, d[i, j] reste np.inf.
        - d[i, i] = 0 pour tous i (distance d'un nœud à lui-même).
        
    """

    n = len(C)
    d = np.matrix(np.zeros((n,n)), dtype=float) # Création d'une matrice nulle initialisée à 0 qui stockera les distances
    # Copie des valeurs de C dans d
    for i in range(n): 
        for j in range(n):
            d[i,j] = C[i,j] 
    # i représente le noeud intermédiaire potentiel
    for i in range(n):
    #j et k : représentent une paire de nœuds entre lesquels on cherche le chemin le plus court.
        for j in range(n): # noeud de départ
            for k in range(n): # nœud d'arrivée
                if d[j,i] + d[i,k] < d[j,k]: # si passer par i est plus court, alors on met à jour d[j,k]
                    d[j,k] = d[j,i] + d[i,k]
    return d # Retourne la matrice contenant les distances les plus courtes entre toutes les paires de nœuds