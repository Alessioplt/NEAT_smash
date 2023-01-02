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

    def get_existing_connection(self, node_in, node_out):
        for connection in self.connections:
            if connection.node_in == node_in and connection.node_out == node_out:
                return connection
        return None

    def get_all_connection_not_made(self):
        temp = []
        for sensor in self.get_all_gene_type("sensor") + self.get_all_gene_type("hidden"):
            for output in self.get_all_gene_type("hidden") + self.get_all_gene_type("output"):
                if self.get_existing_connection(sensor, output) is None and sensor!=output:
                    temp.append([sensor, output])
        return temp

    def get_all_connection_made(self):
        temp = []
        for sensor in self.get_all_gene_type("sensor") + self.get_all_gene_type("hidden"):
            for output in self.get_all_gene_type("hidden") + self.get_all_gene_type("output"):
                if self.get_existing_connection(sensor, output) is not None and sensor!=output:
                    temp.append([sensor, output])
        return temp

    # -------------------Fitness Calculation------------------------------------------------

    #find the latest connection name by name (connection 10 > than connection 9)
    def get_biggest_connection(self, genome):
        value = 0
        for connection in genome.connections:
            if connection.name > value:
                value = connection.name
        return value



    def calculate_number_excess_genes(self, genome_1, genome_2):
        excess = []
        genome_1_biggest = self.get_biggest_connection(genome_1)
        genome_2_biggest = self.get_biggest_connection(genome_2)
        if genome_1_biggest > genome_2_biggest:
            for connection in genome_1.connections:
                if connection.name > genome_2_biggest:
                    excess.append(connection)
        else:
            for connection in genome_2.connections:
                if connection.name > genome_1_biggest:
                    excess.append(connection)
        return len(excess)

    def calculate_number_disjoint_genes(self, genome_1, genome_2):
        disjoint = []
        for connection in genome_1.connections:
            work = True
            for connection_2 in genome_2.connections:
                if connection == connection_2:
                    work = False
            if work:
                disjoint.append(connection)
        for connection in genome_2.connections:
            work = True
            for connection_2 in genome_1.connections:
                if connection == connection_2:
                    work = False
            if work:
                disjoint.append(connection)
        return len(disjoint)

    def calculate_weight_diff(self, genome_1, genome_2):
        return None

    def calculate_fitness(self, genome_1, genome_2, excess_coefficient, disjoint_coefficient, weight_diff_coefficient):
        #calculate all the values necesarry
        number_excess_genes = self.calculate_number_excess_genes(genome_1, genome_2)
        number_disjoint_genes = self.calculate_number_disjoint_genes(genome_1, genome_2)
        weight_diff = self.calculate_weight_diff(genome_1, genome_2)


#todo make a graphical array like in the paper page 109: nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf