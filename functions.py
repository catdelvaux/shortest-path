import numpy as np
import csv as csv

def Dijkstra(C : np.matrix) -> np.matrix:
    return None


def Bellman_Ford(C : np.matrix) -> np.matrix:
    return None


def Floyd_Warshall(C : np.matrix) -> np.matrix:
    return None


with open('graph.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\n')
    for i, line in enumerate(reader):
        print('line[{}] = {}'.format(i, line))


