import numpy as np
import csv as csv
from functions import Dijkstra, Bellman_Ford, Floyd_Warshall

def main():
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

    print("Matrice de coûts :")
    print(m)
    
    print("\nMatrice des plus courts chemins avec Dijkstra :")
    print(Dijkstra(m))
    
    print("\nMatrice des plus courts chemins avec Bellman-Ford :")
    print(Bellman_Ford(m))
    
    print("\nMatrice des plus courts chemins avec Floyd-Warshall :")
    print(Floyd_Warshall(m))

if __name__ == "__main__":
    main()


        
    