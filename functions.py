import numpy as np
import csv as csv

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



def Bellman_Ford(C: np.matrix) -> np.matrix:
    return None


def Floyd_Warshall(C: np.matrix) -> np.matrix:
    n = len(C)
    d = np.matrix(np.zeros((n,n)), dtype=float)
    for i in range(n):
        for j in range(n):
            d[i,j] = C[i,j]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if d[j,i] + d[i,k] < d[j,k]:
                    d[j,k] = d[j,i] + d[i,k]
    return d