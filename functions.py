import numpy as np
import csv as csv


def Dijkstra(C: np.matrix) -> np.matrix:
    """
    Trouver le chemin le plus court du nœud de départ (0) vers tous les autres nœuds
    en utilisant l'algorithme de Dijkstra.

    :param C: np.matrix - Matrice d'adjacence où np.inf représente une absence de connexion.
    :return: np.matrix - Matrice contenant les distances les plus courtes depuis le nœud de départ.
    """
    n = len(C) 
    distances = [float('inf')] * n  
    visited = [False] * n           
    distances[0] = 0               
    for _ in range(n):  
        shortest_distance = float('inf')
        shortest_index = -1
        for i in range(n):
            if not visited[i] and distances[i] < shortest_distance:
                shortest_distance = distances[i]
                shortest_index = i
        if shortest_index == -1:
            break
        visited[shortest_index] = True
        for i in range(n):
            if C[shortest_index, i] < np.inf:  
                new_distance = distances[shortest_index] + C[shortest_index, i]
                if new_distance < distances[i]:  
                    distances[i] = new_distance
    return np.matrix(distances)  


def Bellman_Ford(C : np.matrix) -> np.matrix:
    return None

def Floyd_Warshall(C : np.matrix) -> np.matrix:
    return None


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





print(Dijkstra(m))