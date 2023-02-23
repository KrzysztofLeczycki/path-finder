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


#
# Interaction code
#

want_finish = 'n'

print(
    '''
    ****************************
    *** Search for utilities ***
    ****************************
    '''
)

# The program main loop
while want_finish == 'n':
    selected_resource = ''
    while len(selected_resource) == 0:
        found_resources = []
        # Search for user input in resources linked list
        while len(found_resources) == 0:
            
            user_input = str(input(
            "\nWhat resource available in Arkham city would you like to find?\nType the beginning of that resource and press enter: "
        )).lower()
            resources_linked_list_head = resources_linked_list.get_head_node()
            while resources_linked_list_head is not None:
                if str(resources_linked_list_head.get_value()).startswith(user_input):
                    found_resources.append(resources_linked_list_head.get_value())
                resources_linked_list_head = resources_linked_list_head.get_next_node()
            if len(found_resources) == 0:
                print(f'There is nothing starting with "{user_input}"! Make another try.')

        # Print matching resorces to user's input
        for resource in found_resources:
            print(f'-- {resource}')

        if len(found_resources) == 1:
            want_check = str(input(f'\nDo you want check where you can find {found_resources[0]}? For yes type y, for no type n: ')).lower()
            if want_check == 'y':
                selected_resource = found_resources[0]
                print(f'\nYou can find {selected_resource} in:')
                locations_linked_list_head = locations_linked_list.get_head_node()
                while locations_linked_list_head.get_next_node() is not None:
                    sublist_head = locations_linked_list_head.get_value().get_head_node()
                    if selected_resource in sublist_head.get_value()['resources']:
                        while sublist_head.get_next_node() is not None:
                            sublist_head_resources = ', '.join(sublist_head.get_value()['resources'])
                            sublist_head_neighborhood = ', '.join(city_map.graph_dict[sublist_head.get_value()['name']].get_roads())
                            sublist_head_name = sublist_head.get_value()['name']
                            print('~~~~~~~~~~~~~~~~~~~~')
                            print(f'Name: {sublist_head_name}')
                            print(f'Resources: {sublist_head_resources}')
                            print(f'Neighboring places: {sublist_head_neighborhood}')
                            print('~~~~~~~~~~~~~~~~~~~~\n')      
                            sublist_head = sublist_head.get_next_node()
                    locations_linked_list_head = locations_linked_list_head.get_next_node()
    
    # Exit the main loop
    question = str(input("\nDo you want finish searching? (for yes type 'y'): ")).lower()
    if question == 'y':
        want_finish = 'y'

    