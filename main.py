from Game.create_all_genes import generate
from NEAT import Gene_manager
from NEAT.graph.visualise_genome import Graph
from NEAT.graph.visualise_sepciation import show_repartition
from Game import all_functions
from NEAT import Genome_manager

gene_manager = generate()

genome_manager = Genome_manager.GenomeManager()
for i in range(100):
    genome_manager.create_genome(gene_manager, 5)

speciation = genome_manager.new_speciation(1, 1, 0.79, 1.5)
show_repartition(speciation)


#Graph().create_graph(genome_manager.genomes[0], gene_manager)

print("new node")
for i in range(0):
    genome_manager.genomes[0].mutate(600, 1)
    #Graph().create_graph(genome_manager.genomes[0], gene_manager)
#Graph().create_graph(genome_manager.genomes[0], gene_manager)

genome_manager.save_population('population.meow', 3)