# Creation Data    :    19/11/2020
# Last Modification:    22/11/2020
# Authors          :   'LAHRIFA Walid'
# Short Description:    Programming 'Community detection' Algorithm

import networkx as nx
from networkx.generators.random_graphs import erdos_renyi_graph
from label_prob import label_propagation_communities
from timeit import default_timer as timer
from datetime import timedelta

"""
Graph - Generator
"""

start_gen = timer()
G = erdos_renyi_graph(n=17, p=0)
G.add_weighted_edges_from([(0, 1, 3.0), (1, 2, 7.5)])
G.add_weighted_edges_from([(0, 15, 3.0),(1, 9, 7.5)])
G.add_weighted_edges_from([(5, 6, 3.0), (7, 2, 7.5)])
G.add_weighted_edges_from([(3, 5, 3.0), (8, 2, 7.5)])
G.add_weighted_edges_from([(11, 6, 3.0), (12, 2, 7.5)])
G.add_weighted_edges_from([(16, 4, 3.0), (1, 0, 7.5)])
G.add_weighted_edges_from([(6, 14, 3.0), (1, 4, 7.5)])
G.add_weighted_edges_from([(4, 15, 3.0), (2, 8, 7.5)])
G.add_weighted_edges_from([(5, 15, 3.0), (7, 13, 7.5)])

end_gen = timer()
gen_time = timedelta(seconds=end_gen - start_gen)

"""
Label propagation community detector
"""

def label_propagation_community(G):
    communities_generator = list(label_propagation_communities(G))
    m = []
    for i in communities_generator:
        m.append(list(i))
    print(m)

print("\n************** Graph Informations **************")
print("Node number     : ", len(G.nodes))
print("Node            : ", G.nodes)
print("Edges            : ", G.edges)
print("Graph generation time is : ", str(gen_time) + " Seconds")
print("\n************** Community division results **************")
print("Community division result        :")
label_propagation_community(G)
