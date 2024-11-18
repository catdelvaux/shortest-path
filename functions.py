import numpy as np
import csv as csv

def Dijkstra(C : np.matrix) -> np.matrix:
    D=[]
    rowShort=[]
    size=C.shape
    fridge=[]
    
    for i in range(size[0]):
        rowShort=[]
        for j in range(size[1]):
            rowShort.append(np.inf)
        D.append(rowShort)

    D = np.matrix(mShort)

    #Pour chaque noeud, cherche le plus court chemin par rapport à chaque noeud
    for i in range(len()):
        for j in range(len()):
            return D


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