#------------------------------------------     IMPORTS       ------------------------------------------------------------#

import matplotlib.pyplot as plt
import networkx as nx

#------------------------------------------     TASK 1.2      ------------------------------------------------------------#

G = nx.karate_club_graph()
print(nx.dijkstra_path(G,24,16))