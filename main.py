from NEAT import Gene_manager
from NEAT import Genome
from NEAT.visualise_genome import Graph
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
new_genome.create(5)

new_genome2 = Genome.Genome(new_gene_manager)
new_genome2.create(5)
#new_genome.show_connections()

Graph().create_graph(new_genome.connections, new_gene_manager.get_all_gene_type("sensor"),
                                            new_gene_manager.get_all_gene_type("output"),
                                            new_gene_manager.get_all_gene_type("hidden"))

Graph().create_graph(new_genome2.connections, new_gene_manager.get_all_gene_type("sensor"),
                                            new_gene_manager.get_all_gene_type("output"),
                                            new_gene_manager.get_all_gene_type("hidden"))


new_gene_manager.calculate_fitness(genome_1=new_genome,
                                   genome_2=new_genome2,
                                   excess_coefficient=1,
                                   disjoint_coefficient=1,
                                   weight_diff_coefficient=1)

"""print("new node")
new_genome.mutate(20, 1)

Graph().create_graph(new_genome.connections,  new_gene_manager.get_all_gene_type("sensor"),
                                            new_gene_manager.get_all_gene_type("output"),
                                            new_gene_manager.get_all_gene_type("hidden"))
"""