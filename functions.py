import numpy as np
import csv as csv

def findMin(r, S, line):
    minim = None
    indJ = None
    size = r.shape

    for i in range(0, size[1]):
        if((line, i) in S):
            continue
        minim = r[0, i]
        indJ = i
        break

    for i in range(0, size[1]):
        if((line, i) not in S):
            if(r[0, i]<minim):
                minim = r[0, i]
                indJ = i

    return (minim, indJ)

def Dijkstra(C : np.matrix) -> np.matrix:
    D=[]
    rowShort=[]
    size=C.shape
    
    for i in range(size[0]):
        rowShort=[]
        for j in range(size[1]):
            rowShort.append(np.inf)
        D.append(rowShort)

    D = np.matrix(D)

    #i, i est noeud de départ
    for i in range(size[1]):

        row = D[i]
        rowSize=row.shape
        fridge = []
        D[i, i] = 0

        while(len(fridge)<rowSize[1]):

            Lu, indJ = findMin(row, fridge, i)
            u = (i, indJ)
            fridge.append(u)

            for j in range(rowSize[1]):

                if((Lu+C[indJ, j]<D[i, j]) and ((0, j) not in fridge)):
                    D[i, j] = Lu + C[indJ, j]


    return D

    

def Bellman_Ford(C: np.matrix) -> np.matrix:
    """
    Trouve les plus courtes distances depuis le nœud source (0) vers tous les autres nœuds
    en utilisant l'algorithme de Bellman-Ford.

    :param C: np.matrix - Matrice d'adjacence où np.inf représente une absence de connexion.
    :return: np.matrix - Matrice colonne contenant les distances les plus courtes.
    :raises: ValueError si un cycle de poids négatif est détecté.
    """
    n = len(C)  # Nombre de nœuds
    distances = [float('inf')] * n
    distances[0] = 0  # Le nœud source est fixé à l'indice 0

    # Étape 2 : Relâchement des arêtes (n-1 fois)
    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                if C[u, v] < np.inf:  # Si l'arête u -> v existe
                    new_distance = distances[u] + C[u, v]
                    if new_distance < distances[v]:
                        distances[v] = new_distance

    # Étape 3 : Vérification des cycles de poids négatif
    #for u in range(n):
        #for v in range(n):
            #if C[u, v] < np.inf and distances[u] + C[u, v] < distances[v]:
                #raise ValueError("Cycle de poids négatif détecté")

    # Retourne les distances sous forme de matrice colonne
    return np.matrix(distances)


import numpy as np

def Floyd_Warshall(C: np.matrix) -> np.matrix:
    """
    Trouve les plus courtes distances entre tous les couples de nœuds
    en utilisant l'algorithme de Floyd-Warshall. Modifie directement la matrice donnée.

    :param C: np.matrix - Matrice d'adjacence où np.inf représente une absence de connexion.
    :return: np.matrix - La même matrice, mise à jour avec les distances les plus courtes.
    """
    n = len(C)  # Nombre de nœuds

    # Étape principale : relaxation des distances
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Mise à jour si un chemin plus court existe via le nœud k
                C[i, j] = min(C[i, j], C[i, k] + C[k, j])

    # Détection de cycles négatifs (facultatif)
    for i in range(n):
        if C[i, i] < 0:
            raise ValueError("Cycle de poids négatif détecté")

    return C




#main
matrix=[]

with open('graph.csv', 'r') as f:

    reader = csv.reader(f)
    for line in reader:
        for i in range(len(line)):
            line[i]=int(line[i])
            if line[i] == 1000000000000:
                line[i] = np.inf
        matrix.append(line)

m = np.matrix(matrix)



#print(m)

print(Dijkstra(m))
#print(Bellman_Ford(m))
#print(Floyd_Warshall(m))