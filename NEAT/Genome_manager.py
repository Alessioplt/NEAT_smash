from NEAT import Genome
from NEAT.Connection import Connection
from NEAT.Gene import Gene


# -------------------Fitness Calculation------------------------------------------------

# find the latest connection name by name (connection 10 > than connection 9)

def get_biggest_connection(genome):
    value = 0
    for connection in genome.connections:
        if connection.name > value:
            value = connection.name
    return value


def calculate_number_excess_genes(genome_1, genome_2):
    excess = []
    genome_1_biggest = get_biggest_connection(genome_1)
    genome_2_biggest = get_biggest_connection(genome_2)
    if genome_1_biggest > genome_2_biggest:
        for connection in genome_1.connections:
            if connection.name > genome_2_biggest:
                excess.append(connection)
    else:
        for connection in genome_2.connections:
            if connection.name > genome_1_biggest:
                excess.append(connection)
    return len(excess)


def calculate_number_disjoint_genes(genome_1, genome_2):
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


def calculate_weight_diff(genome_1, genome_2):
    final = 0
    for connection in genome_1.connections:
        for connection_2 in genome_2.connections:
            if connection == connection_2:
                final += (genome_1.connections[connection][0] - genome_2.connections[connection_2][0])
    return final


def calculate_fitness(genome_1, genome_2, excess_coefficient, disjoint_coefficient, weight_diff_coefficient):
    # calculate all the values necessary
    number_excess_genes = calculate_number_excess_genes(genome_1, genome_2)
    number_disjoint_genes = calculate_number_disjoint_genes(genome_1, genome_2)
    weight_diff = calculate_weight_diff(genome_1, genome_2)

    # get biggest
    size_genome_1 = get_biggest_connection(genome_1)
    size_genome_2 = get_biggest_connection(genome_2)
    biggest_genome = size_genome_1 if size_genome_1 > size_genome_2 else size_genome_2

    # do the math in paper
    excess_math = (excess_coefficient * number_excess_genes) / biggest_genome
    disjoint_math = (disjoint_coefficient * number_disjoint_genes) / biggest_genome
    weight_math = weight_diff_coefficient * weight_diff
    compatibility_distance = abs(excess_math) + abs(disjoint_math) + abs(weight_math)

    return compatibility_distance


class GenomeManager:
    def __init__(self, genomes=None, speciation=None):
        if speciation is None:
            speciation = {}
        if genomes is None:
            genomes = []
        self.genomes = genomes
        self.speciation = speciation

    def add_genome(self, genome):
        self.genomes.append(genome)

    def add_speciation(self, key, value):
        if key in self.speciation:
            self.speciation[key].append(value)
        else:
            self.speciation[key] = [value]

    def clean_genome(self):
        self.genomes = []

    def clean_speciation(self):
        self.speciation = {}

    def create_genome(self, gene_manager, connection_number):
        genome = Genome.Genome(gene_manager)
        genome.create(connection_number)
        self.add_genome(genome)
        return genome

    # threshold is the moment where 2 score become too far away
    def new_speciation(self, excess_coefficient, disjoint_coefficient, weight_diff_coefficient, threshold):
        for value in self.genomes:
            for key in self.speciation.keys():
                fitness = calculate_fitness(value, key, excess_coefficient, disjoint_coefficient,
                                            weight_diff_coefficient)
                if fitness < threshold:
                    self.speciation[key].append(value)
                else:
                    self.speciation[value] = []
                    break
            if not self.speciation.keys():
                self.speciation[value] = []
        return self.speciation
