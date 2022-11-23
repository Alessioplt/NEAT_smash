import matplotlib.pyplot as pelote
import networkx
import networkx as nx


class Graph:
    def create_graph(self, connections):
        G = nx.Graph()
        for connection in connections.keys():
            self.add_edge(G, connection.node_in.name, connection.node_out.name, (float("%.4f" % connections[connection][0])))
        elarge_pos = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 1]
        esmall_pos = [(u, v) for (u, v, d) in G.edges(data=True) if 0 < d["weight"] <= 1]
        elarge_neg = [(u, v) for (u, v, d) in G.edges(data=True) if -1 < d["weight"] <= 0]
        esmall_neg = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= -1]
        pos = nx.spring_layout(G, seed=1)  # positions for all nodes - seed for reproducibility
        nx.draw_networkx_nodes(G, pos, node_size=700)
        nx.draw_networkx_edges(G, pos, edgelist=elarge_pos, width=6, edge_color="b")
        nx.draw_networkx_edges(G, pos, edgelist=esmall_pos, width=6, edge_color="b")
        nx.draw_networkx_edges(G, pos, edgelist=elarge_neg, width=3, edge_color="r")
        nx.draw_networkx_edges(G, pos, edgelist=esmall_neg, width=3, edge_color="r")
        # node labels
        nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
        # edge weight labels
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels)

        ax = pelote.gca()
        ax.margins(0.08)
        pelote.axis("off")
        pelote.tight_layout()
        pelote.show()

    def add_edge(self, graph, input, output, weight):
        graph.add_edge(u_of_edge=input, v_of_edge=output, weight=weight)

