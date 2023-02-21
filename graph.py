from copy import copy

class Graph:
    def __init__(self):
        self.graph_dict = {}


    def add_vertex(self, vertex):
        self.graph_dict[vertex.value['name']] = vertex


    def add_connection(self, from_vertex):
        for location in from_vertex.value['connections']:
            self.graph_dict[from_vertex.value['name']].add_road(location['name'], location['length'])
                

    def bfs_search_path(self, start, target):
        path = [start]
        vertex_path = [start, path]
        queue = [vertex_path]
        visited = set()

        while queue:
            #print(f'{queue}\n')
            current_vertex, path = queue.pop(0)
            visited.add(current_vertex)
            for connection in self.graph_dict[current_vertex].roads.keys():
                if connection not in visited:
                    if connection is target:
                        return path + [connection]
                    else:
                        queue.append([connection, path + [connection]])


    def split_path(self, start, target, range):
        path = self.bfs_search_path(start, target)
        avaible_move = copy(range)
        moves_per_round = []

        while path:
            current_round = []
            while avaible_move > 0:
                current_place = path.pop(0)
                current_round.append(current_place)
                if len(path) < 1:
                    break
                distance = self.graph_dict[current_place].roads[path[0]]
                if range < distance:
                    moves_per_round.append(f'no enough action points to move to the {target}')
                    break
                avaible_move -= distance
            moves_per_round.append(current_round)
            avaible_move = copy(range)

        moves_per_round_strings = [' -> '.join(array) for array in moves_per_round]
        return moves_per_round_strings


                        