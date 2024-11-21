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