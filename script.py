from vertex import Vertex
from graph import Graph
from data import locations, resources_list


#
# Create the graph from the locations dictionary
# 

city_map = Graph()
for location in locations:
    new_vertex = Vertex(location)
    print(new_vertex.value['name'])
    #city_map.add_vertex(new_vertex)
  