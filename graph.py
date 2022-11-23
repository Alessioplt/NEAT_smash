import itertools
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def create_graph(self, connections, number_input, number_output, number_hidden):
        subset_sizes = [number_input, number_hidden, number_output]
        subset_color = [
            "gold",
            "violet",
            "limegreen",
            "violet",
            "violet",
            "violet",
            "limegreen",
            "darkorange",
        ]

        G = self.multilayered_graph(*subset_sizes, connections)
        color = [subset_color[data["layer"]] for v, data in G.nodes(data=True)]
        pos = nx.multipartite_layout(G, subset_key="layer")
        plt.figure(figsize=(8, 8))
        nx.draw(G, pos, node_color=color, with_labels=False)
        plt.axis("equal")
        plt.show()

    def multilayered_graph(self, *subset_sizes, connections):
        extents = nx.utils.pairwise(itertools.accumulate((0,) + subset_sizes))
        layers = [range(start, end) for start, end in extents]
        G = nx.Graph()
        for connection in connections.keys():
            G.add_edge(connection.node_in.name, connection.node_out.name, weight=(float("%.4f" % connections[connection][0])))
        return G


