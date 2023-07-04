import itertools
import matplotlib.pyplot as plt
import networkx as nx
"""            "violet",
            "violet",
            "violet",
            "limegreen",
            "darkorange",
        """
class Graph:
    def create_graph(self, connections, gene_manager):
        number_input = gene_manager.get_all_gene_type("sensor")
        number_output = gene_manager.get_all_gene_type("output")
        G = nx.Graph()
        pos = {}
        layer_in = 0
        layer_hidden = -0.5
        layer_out = 0
        for value in number_input:
            pos[value.name] = (0, layer_in)
            layer_in += 3
        for value in number_output:
            pos[value.name] = (2, layer_out)
            layer_out += 3
        for connection in connections.keys():
            self.add_edge(G, connection.node_in.name, connection.node_out.name, (float("%.4f" % connections[connection][0])))
            if connection.node_in.name not in pos:
                if connection.node_in not in number_input:
                    pos[connection.node_in.name] = (1, layer_hidden)
                    if layer_hidden >= 0:
                        layer_hidden += 1
                    layer_hidden = layer_hidden * -1
            if connection.node_out.name not in pos:
                if connection.node_out not in number_output:
                    pos[connection.node_out.name] = (1, layer_hidden)
                    if layer_hidden >= 0:
                        layer_hidden += 1
                    layer_hidden = layer_hidden * -1
        elarge_pos = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 1]
        esmall_pos = [(u, v) for (u, v, d) in G.edges(data=True) if 0 < d["weight"] <= 1]
        elarge_neg = [(u, v) for (u, v, d) in G.edges(data=True) if -1 < d["weight"] <= 0]
        esmall_neg = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= -1]
        nx.draw_networkx_nodes(G, pos, node_size=700)
        nx.draw_networkx_edges(G, pos, edgelist=elarge_pos, width=6, edge_color="b")
        nx.draw_networkx_edges(G, pos, edgelist=esmall_pos, width=3, edge_color="b")
        nx.draw_networkx_edges(G, pos, edgelist=elarge_neg, width=6, edge_color="r")
        nx.draw_networkx_edges(G, pos, edgelist=esmall_neg, width=3, edge_color="r")
        # node labels
        nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
        # edge weight labels
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels, label_pos=0.69)
        nx.set_node_attributes(G, pos, 'coord')

        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.show()

    def add_edge(self, graph, input, output, weight):
        graph.add_edge(u_of_edge=input, v_of_edge=output, weight=weight)

