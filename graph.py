class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value['name']] = vertex

    def add_connection(self, from_vertex):
        for location in from_vertex.value['connections']:
            self.graph_dict[from_vertex.value['name']].add_road(location['name'], location['length'])
        
        