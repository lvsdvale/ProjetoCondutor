import numpy as np
import pandas as pd
import networkx as nx
import csv
import math
import matplotlib.pyplot as plt
import traveling_salesman as ts

fp = "tabela_coordenadas.csv"
radius = 6371

list = pd.read_csv(fp)
f = open('ciclo_minimo', 'w')
writer = csv.writer(f)
x = []
y = []

for p in list.to_numpy():
    for q in list.to_numpy():
        x.append(radius*math.radians((math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2))))
    y.append(x.copy())
    x.clear()
route = ts.brute_force(y, 0)

for l in route:
    f.write(str(list.to_numpy()[l]))
    f.write('\n')
f.write(str(ts.min_path))
G = nx.from_numpy_matrix(np.array(y)) 
pos=nx.spring_layout(G)

nx.draw(G)

pos = nx.circular_layout(G)
nx.draw_networkx_nodes(G, pos, 
                        node_size = 500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, arrows=False)
plt.savefig('network.png')