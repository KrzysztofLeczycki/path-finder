class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_connection(self, first_vertex, second_vertex, length=0):
        self.graph_dict[first_vertex.value].add_connection(second_vertex.value, length)
        self.graph_dict[second_vertex.value].add_connection(first_vertex.value)