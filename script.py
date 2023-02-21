from vertex import Vertex
from graph import Graph
from data import locations, resources


#
# Construct the graph with connections
# 

# Initialize the graph
city_map = Graph()
for location in locations:
    new_vertex = Vertex(location)
    city_map.add_vertex(new_vertex)

# Create connections
for vertex, content in city_map.graph_dict.items():
    city_map.add_connection(content)
    #print(content.get_roads())
    
print(city_map.split_path('Northside', 'Hospital', 3))