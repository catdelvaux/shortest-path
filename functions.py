import numpy as np
import csv as csv

# Algorithme de Dijkstra
def Dijkstra(C: np.matrix) -> np.matrix:
    n = len(C)
    matrix = np.matrix(np.zeros((n,n)), dtype=float)
    for j in range(n):
        L = n * [float('inf')]
        S = []
        L[j] = 0
        while len(S) != n :
            min = float('inf')
            u = float('-inf')
            for i in range(n) :
                if L[i] < min and i not in S:
                    u = i
                    min = L[i]
            S.append(u)
            for v in range(n) :
                if v not in S:
                    if L[u] + C[u,v] < L[v]:
                        L[v] = L[u] + C[u,v]
        matrix[j] = L
    return matrix


# Algorithme de Bellman Ford
def Bellman_Ford(C: np.matrix) -> np.matrix:
    return None

# Algorithme de Floyd Warshall
def Floyd_Warshall(C: np.matrix) -> np.matrix:
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