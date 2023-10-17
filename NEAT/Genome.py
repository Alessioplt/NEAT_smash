import random


class Genome:
    def __init__(self, gene_manager):
        self.connections = {}  # name: [weight, enabled]
        self.genes = []
        self.genes_score = {}
        self.gene_manager = gene_manager
        self.score = 0

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
            print(f"({connection.name}) {connection.node_in.name}->{connection.node_out.name}",
                  self.connections[connection])

    # ajoute un gene sur une connection, ayant pour effet de la coupé en deux
    def add_node(self, sensor_name, output_name, gene=None):
        # dummy name because hidden gene are automatically named anyway
        if gene is None:
            gene = self.gene_manager.add_gene("dummy name", "hidden")
            self.genes.append(gene)

        connection = self.find_connection(sensor_name, output_name)
        self.connections[connection][1] = False
        self.add_connection(connection.node_in, gene, 1)
        self.add_connection(gene, connection.node_out, self.connections[connection][0])

    def calculate(self, game_state, controller):
        self.genes_score = {}
        all_sensor = self.gene_manager.get_all_gene_type("sensor")
        all_output = self.gene_manager.get_all_gene_type("output")
        for gene in self.genes:
            if gene in all_sensor:
                self.genes_score[gene] = gene.behavior(game_state)
        for connection in self.connections:
            if self.connections[connection][1] == True:
                if connection.node_out in self.genes_score.keys():
                    self.genes_score[connection.node_out] += \
                        self.genes_score[connection.node_in] * self.connections[connection][0]
                else:
                    self.genes_score[connection.node_out] = \
                        self.genes_score[connection.node_in] * self.connections[connection][0]
        best_output = None
        for gene in self.genes_score:
            if gene in all_output:
                if best_output is None:
                    best_output = [gene, self.genes_score[gene]]
                elif self.genes_score[gene] > best_output[1]:
                    best_output = [gene, self.genes_score[gene]]
        #print(best_output[0].name, best_output[1])
        return best_output[0]
    # -------------------Mutation------------------------------------------------
    # add randomly a new node (pick an already existing if not in this genome)
    def mutate_node(self, chance):
        done = False
        connection_made = self.gene_manager.get_all_connection_made(self)
        if random.randint(1, 100) <= chance:
            done = True
            choice = random.choice(connection_made)
            sensor_name = choice.node_in.name
            output_name = choice.node_out.name
            hiddens = self.gene_manager.get_hidden_unique(self.genes)
            if len(hiddens) == 0:
                self.add_node(sensor_name, output_name)
            else:
                self.add_node(sensor_name, output_name, hiddens[0])
        return done

    # randomly add new connection between two genes
    def mutate_connection(self, chance):
        done = False
        connection_not_made = self.gene_manager.get_all_connection_not_made(self)
        choice = random.choice(connection_not_made)
        if random.randint(1, 100) <= chance:
            done = True
            self.add_connection(choice[0], choice[1], random.uniform(-2, 2))

        return done

    # randomly enable or disable connections
    def mutate_enable_disable(self, chance):
        done = False
        connection = random.choice(list(self.connections.keys()))
        if random.randint(1, 100) <= chance:
            done = True
            self.connections[connection][1] = not self.connections[connection][1]
        return done

    # randomly shift the weight by *0.5 to *1.5
    def mutate_weight_shift(self, chance):
        done = False
        connection = random.choice(list(self.connections.keys()))
        if random.randint(1, 100) <= chance:
            done = True
            self.connections[connection][0] *= random.uniform(0.5, 1.5)
        return done

    # randomly re randomize weight
    def mutate_weight_random(self, chance):
        done = False
        connection = random.choice(list(self.connections.keys()))
        if random.randint(1, 100) <= chance:
            done = True
            self.connections[connection][0] = random.uniform(-2, 2)
        return done

    def mutate_weight_shift_sign(self, chance):
        done = False
        connection = random.choice(list(self.connections.keys()))
        if random.randint(1, 100) <= chance:
            done = True
            self.connections[connection][0] = -self.connections[connection][0]
        return done

    # chance mutate between 0 and 100
    def mutate(self, chance_mutate, mutation_intensity):
        chance_holder = chance_mutate
        for _ in range(mutation_intensity):
            chance_mutate = chance_holder
            division = 6
            if self.mutate_node(chance_mutate / division) is False:
                division -= 1
            if self.mutate_connection(chance_mutate / division) is False:
                division -= 1
            if self.mutate_enable_disable(chance_mutate / division) is False:
                division -= 1
            if self.mutate_weight_shift(chance_mutate / division) is False:
                division -= 1
            if self.mutate_weight_shift_sign(chance_mutate / division) is False:
                division -= 1
            self.mutate_weight_random(chance_mutate / division)
