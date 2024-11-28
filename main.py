import numpy as np
import csv as csv
from functions import Dijkstra, Bellman_Ford, Floyd_Warshall

# Procédure "main" 
def main():
    # Lit le fichier .csv contenant la matrice de coûts C du graphe et le convertit en matrice numpy
    matrix = []
    with open('graph.csv', 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            for i in range(len(line)):
                line[i] = int(line[i]) 
                if line[i] == 1000000000000:  
                    line[i] = np.inf
            matrix.append(line)
    
    m = np.array(matrix)

    # Imprime la matrice de coûts du fichier .csv
    print("Matrice de coûts :")
    print(m)

    # Lance le calcul des matrices de distance des plus courts chemins via les 3 algorithmes et imprime les résultats à l’écran 
    print("\nMatrice des plus courts chemins avec Dijkstra :")
    print(Dijkstra(m))
    
    print("\nMatrice des plus courts chemins avec Bellman-Ford :")
    print(Bellman_Ford(m))
    
    print("\nMatrice des plus courts chemins avec Floyd-Warshall :")
    print(Floyd_Warshall(m))

if __name__ == "__main__":
    main()


        
    