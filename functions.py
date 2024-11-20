import numpy as np
import csv as csv


def Dijkstra(C: np.matrix) -> np.matrix:
    """
    Trouve le chemin le plus court depuis le nœud de départ (0) vers tous les autres nœuds
    en utilisant l'algorithme de Dijkstra.

    :param C: np.matrix - Matrice d'adjacence où np.inf représente une absence de connexion.
    :return: np.matrix - Matrice contenant les distances les plus courtes depuis le nœud de départ.
    """
    n = len(C)  # Nombre total de nœuds dans le graphe
    distances = [float('inf')] * n  # Liste des distances minimales depuis le nœud de départ
    visited = [False] * n  # Liste pour marquer les nœuds déjà visités
    distances[0] = 0  # La distance du nœud de départ à lui-même est 0

    for _ in range(n):  
        shortest_distance = float('inf')  # Variable pour stocker la plus petite distance trouvée
        shortest_index = -1  # Index du nœud avec la plus petite distance

        # Trouver le nœud non visité avec la plus petite distance
        for i in range(n):  
            if not visited[i] and distances[i] < shortest_distance:
                shortest_distance = distances[i]
                shortest_index = i

        # Si aucun nœud non visité n'a été trouvé, quitter la boucle
        if shortest_index == -1:
            break

        # Marquer le nœud comme visité
        visited[shortest_index] = True

        # Mettre à jour les distances pour les voisins du nœud courant si un chemin plus court est trouvé
        for i in range(n):
            if C[shortest_index, i] < np.inf:  # Ignorer les connexions inexistantes
                # Calculer une nouvelle distance potentielle via le nœud courant
                new_distance = distances[shortest_index] + C[shortest_index, i]
                if new_distance < distances[i]:  # Mettre à jour si une distance plus courte est trouvée
                    distances[i] = new_distance

    # Retourne les distances minimales pour chaque noeud
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



print(m)

print(Dijkstra(m))