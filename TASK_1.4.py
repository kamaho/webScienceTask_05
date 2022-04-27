#------------------------------------------      IMPORTS       ------------------------------------------------------------#

from turtle import color
from matplotlib.colors import Colormap
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from requests import options

#------------------------------------------     TASK 1.4      ------------------------------------------------------------#

G = nx.karate_club_graph()

nodes = G.nodes()

position = nx.spring_layout(G)
color = {"Mr. Hi": "#3DA3F5", "Officer": "#E0D91B"}
dijkstra_route = nx.dijkstra_path(G, 24, 16)

colors = ["red" if n in dijkstra_route else color[G.nodes[n]["club"]] for n in nodes]

dijkstra_edges = []
for index in range(0, len(dijkstra_route) - 1):
   edge = (dijkstra_route[index], dijkstra_route[index + 1])
   dijkstra_edges.append(edge)
   
edge_colors = ["red" if edge in dijkstra_edges else "black" for edge in G.edges()]


nx.draw(G, position, node_color=colors, edge_color=edge_colors, with_labels=True)
plt.show()