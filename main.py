import random

from NEAT import Gene_manager
from NEAT import Genome


def fonction(hh):
    print(hh)


new_gene_manager = Gene_manager.GeneManager()
new_gene_manager.add_gene("A", "sensor", fonction)
new_gene_manager.add_gene("B", "sensor", fonction)
new_gene_manager.add_gene("C", "sensor", fonction)
new_gene_manager.add_gene("1", "output", fonction)
new_gene_manager.add_gene("2", "output", fonction)
new_gene_manager.add_gene("3", "output", fonction)
new_gene_manager.add_gene("stfu", "hidden", fonction)


new_genome = Genome.Genome(new_gene_manager)
new_genome.create(22)
new_genome.show_connections()
print("new node")
new_genome.mutate(10000, 1)
new_genome.show_connections()
