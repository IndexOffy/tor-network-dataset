import networkx as nx
import matplotlib.pyplot as plt

from request import mega_data

nodes_list, nodes_connections = mega_data()

onion = nx.Graph()
onion.add_nodes_from(nodes_list)
onion.add_edges_from(nodes_connections)

options = {
    'font_size': 5,
    'linewidths': 11, 
    'node_size': 50,
    'width': 1,
    'alpha': 1,
    'font_family': 'sans-serif'
}

nx.draw(onion, with_labels=True, **options)

nx = plt.gca()
nx.collections[1].set_edgecolor("#787878") 
plt.show()
