class Vertex:
  def __init__(self, value):
    self.value = value
    self.roads = {}

  def __repr__(self):
    resources = self.value['resources']
    return f'{resources}'

  def add_road(self, vertex, length = 0):
    self.roads[vertex] = length

  def get_roads(self):
    return list(self.roads.keys())