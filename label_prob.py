# Creation Data    :    19/11/2020
# Last Modification:    22/11/2020
# Authors          :    'EN NIARI SAAD' & 'LAHRIFA Walid'
# Short Description:    Programming 'Community detection' Algorithm



from collections import Counter
from networkx.utils import groups
from networkx.utils import not_implemented_for
from networkx.utils import py_random_state
__all__ = ["label_propagation_communities", "asyn_lpa_communities"]
import networkx as nx
@py_random_state(2)
def asyn_lpa_communities(G, weight=None, seed=None):
    labels = {n: i for i, n in enumerate(G)}
    cont = True
    while cont:
        cont = False
        nodes = list(G)
        seed.shuffle(nodes)
        for node in nodes:
            if len(G[node]) < 1:
                continue
            label_freq = Counter()
            for v in G[node]:
                label_freq.update({labels[v]: G.edges[node, v][weight] if weight else 1})
            max_freq = max(label_freq.values())
            best_labels = [
                label for label, freq in label_freq.items() if freq == max_freq]
            if labels[node] not in best_labels:
                labels[node] = seed.choice(best_labels)
                cont = True

    yield from groups(labels).values()
@not_implemented_for("directed")
def label_propagation_communities(G):
    coloring = _color_network(G)
    labeling = {v: k for k, v in enumerate(G)}
    while not _labeling_complete(labeling, G):
        for color, nodes in coloring.items():
            for n in nodes:
                _update_label(n, labeling, G)

    for label in set(labeling.values()):
        yield {x for x in labeling if labeling[x] == label}
def _color_network(G):
    coloring = dict()
    colors = nx.coloring.greedy_color(G)
    for node, color in colors.items():
        if color in coloring:
            coloring[color].add(node)
        else:
            coloring[color] = {node}
    return coloring
def _labeling_complete(labeling, G):
    return all(labeling[v] in _most_frequent_labels(v, labeling, G) for v in G if len(G[v]) > 0)

def _most_frequent_labels(node, labeling, G):
    if not G[node]:
        return {labeling[node]}
    freqs = Counter(labeling[q] for q in G[node])
    max_freq = max(freqs.values())
    return {label for label, freq in freqs.items() if freq == max_freq}
def _update_label(node, labeling, G):
    high_labels = _most_frequent_labels(node, labeling, G)
    if len(high_labels) == 1:
        labeling[node] = high_labels.pop()
    elif len(high_labels) > 1:
        if labeling[node] not in high_labels:
            labeling[node] = max(high_labels)
