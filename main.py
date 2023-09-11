from NEAT import Gene_manager
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

speciation = genome_manager.new_speciation(1, 1, 0.2, 1.63)
print(speciation)
#for keys in speciation.keys():
#    print(f"new groupe")
#    print("Pere")
#    dadGene = keys
#    Graph().create_graph(dadGene.connections, gene_manager)
#
#    for value in speciation[keys]:
#        print("Fils")
#        Graph().create_graph(value.connections, gene_manager)
#    break

show_repartition(speciation)

"""print("new node")
new_genome.mutate(20, 1)

Graph().create_graph(new_genome.connections,  new_gene_manager.get_all_gene_type("sensor"),
                                            new_gene_manager.get_all_gene_type("output"),
                                            new_gene_manager.get_all_gene_type("hidden"))
"""
