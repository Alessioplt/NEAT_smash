import itertools
import random

import matplotlib.pyplot as plt
import networkx as nx
"""            "violet",
            "violet",
            "violet",
            "limegreen",
            "darkorange",
        """
class Graph:
    def create_graph(self, genome, gene_manager):
        number_input = gene_manager.get_all_gene_type("sensor")
        number_output = gene_manager.get_all_gene_type("output")
        genome_genes = []
        for value in genome.genes:
            genome_genes.append(value.name)
        G = nx.Graph()
        pos = {}
        layer_in = 0
        layer_hidden = -50
        layer_out = 0
        for value in number_input:
            if value.name in genome_genes:
                pos[value.name] = (0, layer_in)
                layer_in += 100
        for value in number_output:
            if value.name in genome_genes:
                pos[value.name] = (2, layer_out)
                layer_out += 100
        for connection in genome.connections.keys():
            self.add_edge(G, connection.node_in.name, connection.node_out.name,
                          (float("%.4f" % genome.connections[connection][0])))
            if connection.node_in.name not in pos:
                if connection.node_in not in number_input:
                    pos[connection.node_in.name] = (1, layer_hidden)
                    if layer_hidden >= 0:
                        layer_hidden += 100
                    layer_hidden = layer_hidden * -1
            if connection.node_out.name not in pos:
                if connection.node_out not in number_output:
                    pos[connection.node_out.name] = (1, layer_hidden)
                    if layer_hidden >= 0:
                        layer_hidden += 100
                    layer_hidden = layer_hidden * -1
        elarge_pos = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 1]
        esmall_pos = [(u, v) for (u, v, d) in G.edges(data=True) if 0 < d["weight"] <= 1]
        elarge_neg = [(u, v) for (u, v, d) in G.edges(data=True) if -1 < d["weight"] <= 0]
        esmall_neg = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= -1]
        print(pos)
        nx.draw_networkx_nodes(G, pos, node_size=700)
        nx.draw_networkx_edges(G, pos, edgelist=elarge_pos, width=6, edge_color="b")
        nx.draw_networkx_edges(G, pos, edgelist=esmall_pos, width=3, edge_color="b")
        nx.draw_networkx_edges(G, pos, edgelist=elarge_neg, width=6, edge_color="r")
        nx.draw_networkx_edges(G, pos, edgelist=esmall_neg, width=3, edge_color="r")
        # node labels
        nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
        # edge weight labels
        edge_labels = nx.get_edge_attributes(G, "weight")
        for value in edge_labels.keys():
            edge_label = {value: edge_labels[value]}
            position = random.randrange(20, 40) / 100
            position2 = random.randrange(60, 90) / 100
            choice = random.choice([position, position2])
            nx.draw_networkx_edge_labels(G, pos, edge_label, label_pos=choice)
        nx.set_node_attributes(G, pos, 'coord')

        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.show()

    def add_edge(self, graph, input, output, weight):
        graph.add_edge(u_of_edge=input, v_of_edge=output, weight=weight)

