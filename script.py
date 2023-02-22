from vertex import Vertex
from graph import Graph
from linked_list import LinkedList
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
    

#
# Construct linked lists
#

# The resources linked list
resources_linked_list = LinkedList()
for resource in resources:
    resources_linked_list.insert_beginning(resource)

# The places linked list of linked lists
locations_linked_list = LinkedList()
for resource in resources:
    locations_sublist = LinkedList()
    for location in locations:
        if resource in location['resources']:
            locations_sublist.insert_beginning(location)
    locations_linked_list.insert_beginning(locations_sublist)