class Gene:
    def __init__(self, name, node_type, behavior = None):
        self.name = name
        self.node_type = node_type  # sensor, output, hidden
        self.behavior = behavior
