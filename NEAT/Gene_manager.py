from NEAT.Connection import Connection
from NEAT.Gene import Gene


class GeneManager:
    def __init__(self, genes=None, connections=None):
        if connections is None:
            connections = []
        if genes is None:
            genes = []
        self.genes = genes
        self.connections = connections
        self.connection_name = 1
        self.hidden_name = 1

    def add_gene(self, name, node_type, behavior=None):
        if node_type == "hidden":
            name = f"H_{self.hidden_name}"
            self.hidden_name += 1
        gene = Gene(name, node_type, behavior)
        self.genes.append(gene)
        return gene

    def remove_gene(self, name):
        for gene in self.genes:
            if gene.name == name:
                self.genes.remove(gene)

    def get_all_gene_type(self, node_type):
        temp = []
        for gene in self.genes:
            if gene.node_type == node_type:
                temp.append(gene)
        return temp

    def get_hidden_unique(self, already_exist):
        hidden = self.get_all_gene_type("hidden")
        temp = self.get_all_gene_type("hidden")
        for value in hidden:
            if value in already_exist:
                temp.remove(value)
        return temp

    def add_connection(self, node_in, node_out):
        new_connection = Connection(node_in, node_out, self.connection_name)
        self.connections.append(new_connection)
        self.connection_name += 1
        return new_connection

    def get_connection(self, node_in, node_out):
        for connection in self.connections:
            if connection.node_in == node_in and connection.node_out == node_out:
                return connection
        return self.add_connection(node_in, node_out)

    def get_existing_connection(self, node_in, node_out, genome):
        for connection in genome.connections.keys():
            if connection.node_in == node_in and connection.node_out == node_out:
                return connection
        return None

    def get_all_connection_not_made(self, genome):
        temp = []
        for sensor in self.get_all_gene_type("sensor") + self.get_all_gene_type("hidden"):
            for output in self.get_all_gene_type("hidden") + self.get_all_gene_type("output"):
                if self.get_existing_connection(sensor, output, genome) is None and sensor != output:
                    temp.append([sensor, output])
        return temp

    def get_all_connection_made(self, genome):
        temp = list(genome.connections.keys())
        return temp