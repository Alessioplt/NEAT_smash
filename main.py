from NEAT import Gene_manager
from NEAT.graph.visualise_genome import Graph
from NEAT.graph.visualise_sepciation import show_repartition
from Game import all_functions
from NEAT import Genome_manager

gene_manager = Gene_manager.GeneManager()
gene_manager.add_gene("A", "sensor", all_functions.fonction)
gene_manager.add_gene("B", "sensor", all_functions.fonction)
gene_manager.add_gene("C", "sensor", all_functions.fonction)
gene_manager.add_gene("1", "output", all_functions.fonction)
gene_manager.add_gene("2", "output", all_functions.fonction)
gene_manager.add_gene("3", "output", all_functions.fonction)
gene_manager.add_gene("stfu", "hidden", all_functions.fonction)

genome_manager = Genome_manager.GenomeManager()
for i in range(200):
    genome_manager.create_genome(gene_manager, 5)

speciation = genome_manager.new_speciation(1, 1, 0.15, 1.65)
show_repartition(speciation)

Graph().create_graph(genome_manager.genomes[0].connections, gene_manager)

print("new node")
for genome in genome_manager.genomes:
    try:
        genome.mutate(20, 1)
    except Exception as e:
        print(e, genome.connections)
        Graph().create_graph(genome.connections, gene_manager)
        break
Graph().create_graph(genome_manager.genomes[0].connections, gene_manager)
speciation = genome_manager.new_speciation(1, 1, 0.15, 1.65)
show_repartition(speciation)



#    print(f"new groupe")
#    print("Pere")
#    dadGene = keys
#    Graph().create_graph(dadGene.connections, gene_manager)
#
#    for value in speciation[keys]:
#        print("Fils")
#        Graph().create_graph(value.connections, gene_manager)
#    break
