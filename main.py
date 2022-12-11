import random

from NEAT import Gene_manager
from NEAT import Genome
from visualise_genome import Graph
from NEAT import all_functions


new_gene_manager = Gene_manager.GeneManager()
new_gene_manager.add_gene("A", "sensor", all_functions.fonction)
new_gene_manager.add_gene("B", "sensor", all_functions.fonction)
new_gene_manager.add_gene("C", "sensor", all_functions.fonction)
new_gene_manager.add_gene("1", "output", all_functions.fonction)
new_gene_manager.add_gene("2", "output", all_functions.fonction)
new_gene_manager.add_gene("3", "output", all_functions.fonction)
new_gene_manager.add_gene("stfu", "hidden", all_functions.fonction)


new_genome = Genome.Genome(new_gene_manager)
new_genome.create(22)
#new_genome.show_connections()

graph = Graph()
graph.create_graph(new_genome.connections,  new_gene_manager.get_all_gene_type("sensor"),
                                            new_gene_manager.get_all_gene_type("output"),
                                            new_gene_manager.get_all_gene_type("hidden"))
print("new node")
#new_genome.mutate(10000, 1)
#new_genome.show_connections()
