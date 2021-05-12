import numpy as np
import pandas as pd
import networkx as nx
from itertools import permutations

min_path = float('inf')
dist_sum = 0

def brute_force(graph,s):
    vertex = []
    global min_path
    for i in range(len(graph)):
        if i != s:
            vertex.append(i)
 
    next_permutation=permutations(vertex)
    cycle = []
    min_cycle = []
    for i in next_permutation:
 
        current_path = 0
 
        k = s
        for j in i:
            current_path += graph[k][j]
            cycle.append(k)
            cycle.append(j)
            k = j
        current_path += graph[k][s]
        cycle.append(s)
        if (current_path < min_path):
            min_path = current_path
            min_cycle = cycle.copy()
        cycle.clear()

    return min_cycle

