import random


class Genome:
    def __init__(self, gene_manager):
        self.connections = {}  # name: [weight, enabled]
        self.genes = []
        self.gene_manager = gene_manager
        self.fitness = None

    def create(self, connection_number):
        for _ in range(connection_number):
            sensor = random.choice(self.gene_manager.get_all_gene_type("sensor"))
            output = random.choice(self.gene_manager.get_all_gene_type("output"))
            weight = random.uniform(-2, 2)
            self.add_connection(sensor, output, weight)

    def find_connection(self, sensor_name, output_name):
        for connection in self.connections.keys():
            if connection.node_in.name == sensor_name and connection.node_out.name == output_name:
                return connection

    def add_connection(self, sensor, output, weight):
        connection = self.gene_manager.get_connection(sensor, output)
        if sensor not in self.genes:
            self.genes.append(sensor)
        if output not in self.genes:
            self.genes.append(output)
        self.connections[connection] = [weight, True]

    def show_connections(self):
        for connection in self.connections.keys():
            print(connection.node_in.name + "->" + connection.node_out.name, self.connections[connection])

    def add_node(self, sensor_name, output_name):
        gene = self.gene_manager.add_gene("dummy name", "hidden")
        self.genes.append(gene)
        connection = self.find_connection(sensor_name, output_name)
        self.connections[connection][1] = False
        self.add_connection(connection.node_in, gene, 1)
        self.add_connection(gene, connection.node_out, self.connections[connection][0])

# -------------------Mutation------------------------------------------------
    def mutate_node(self, chance):
        hiddens = self.gene_manager.get_hidden_unique(self.genes)
        sensor, output = None, None
        while sensor == output:
            sensor = self.gene_manager.get_all_gene_type("hidden") + self.gene_manager.get_all_gene_type("sensor")
            output = self.gene_manager.get_all_gene_type("hidden") + self.gene_manager.get_all_gene_type("output")
        if random.randint(1, 100) <= chance:
            sensor_name = random.choice(sensor).name
            output_name = random.choice(output).name
            print("sensor: ", sensor_name)
            print("output: ", output_name)
            if len(hiddens) == 0:
                self.add_node(sensor_name, output_name)

    def mutate_connection(self, chance):
        pass

    def mutate_enable_disable(self, connection):
        self.connections[connection][1] = not self.connections[connection][1]

    def mutate_weight_shift(self, connection):
        self.connections[connection][0] *= random.uniform(0.5, 1.5)

    def mutate_weight_random(self, connection):
        self.connections[connection][0] = random.uniform(-2, 2)

    def mutate(self, chance_mutate, mutation_intensity):
        pass


