class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def __repr__(self):
    resources = self.value['resources']
    return f'{resources}'

  def add_edge(self, vertex, length = 0):
    self.edges[vertex] = length

  def get_edges(self):
    return list(self.edges.keys())