# Genome Manager
## params
genomes: list of all genomes.

speciation: list of speciation of these genomes.

## methods

add_genome(genome): add a new genome to the genome list

add_speciation(key, value): add a new value the speciation list

clean_genome(): empty genome list

clean_speciation(): empty speciation list

create_genome(gene_manager, connection_number): create a new genome
# Genome
## params
connections: dic in the form of {name: [weight, enabled]}

genes: list of all genes

gene_manager: the gene manager

fitness: the score of that genome (unused yet)
## methods
create(connection_number): create a new genome

find_connection(sensor_name, output_name): find a connection with an in and an out

add_connection(sensor_name, output_name, weight): add a new connection

show_connections(): print all connections

add_node(sensor_name, output_name, gene): add a new node in the middle of a connection

mutate_node(chance): add randomly a new node (pick an already existing if not in this genome)

mutate_connection(chance): randomly add new connection between two genes

mutate_enable_disable(chance): invert the enable state with a % chance

mutate_weight_shift(chance): shift the weight with a % chance

mutate_weight_random(chance): change the weight with a % chance

mutate_weight_shift_sign(chance): change the sign with a % chance

mutate(chance_mutate, mutation_intensity): mutate the genome with intensity meaning the number of tries
# Gene Manager
## params
genes: list of all genes

connections: list of connection object

connection_name: int to name the connections

hidden_name: int to name the hidden nodes
## methods
add_gene(name, node_type, behavior=None): add a new gene

remove_gene(name): remove a gene

get_all_gene_type(node_type): get all genes of a type (input, output, hidden)

get_hidden_unique(already_exist): ???????

add_connection(node_in, node_out): add a new connection

get_connection(node_in, node_out): get a connection

get_existing_connection(node_in, node_out): get a connection if it exists

get_all_connection_not_made(): get all connections not made

get_all_connection_made(): get all connections
# Gene
## params
name: name of the gene
node_type: type of the gene (input, output, hidden)
behavior: behavior of the gene (unused yet)
# Connection
## params
node_in: input node
node_out: output node
name: name of the connection