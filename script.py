from vertex import Vertex
from graph import Graph
from linked_list import LinkedList
from data import locations, resources, locations_names


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
    matching_places = {}
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

        # Generate and print places with selected resource
        if len(found_resources) == 1:
            want_check = str(input(f'\nDo you want check where you can find {found_resources[0]}? For yes type y, for no type n: ')).lower()
            if want_check == 'y':
                selected_resource = found_resources[0]
                print(f'\nYou can find {selected_resource} in:')
                locations_linked_list_head = locations_linked_list.get_head_node()
                
                index = 1
                while locations_linked_list_head.get_next_node() is not None:
                    sublist_head = locations_linked_list_head.get_value().get_head_node()

                    def is_resource():
                        return selected_resource in sublist_head.get_value()['resources']
                    
                    if is_resource():
                        while sublist_head.get_next_node() is not None:
                            if is_resource() and sublist_head.get_value()['name'] not in matching_places.values():
                                sublist_head_resources = ', '.join(sublist_head.get_value()['resources'])
                                sublist_head_neighborhood = ', '.join(city_map.graph_dict[sublist_head.get_value()['name']].get_roads())
                                sublist_head_name = sublist_head.get_value()['name']
                                print('~~~~~~~~~~~~~~~~~~~~')
                                print(f'Name: {sublist_head_name}')
                                print(f'Resources: {sublist_head_resources}')
                                print(f'Neighboring places: {sublist_head_neighborhood}')
                                print('~~~~~~~~~~~~~~~~~~~~\n')  
                                matching_places[str(index)] = sublist_head_name
                                index += 1
                            sublist_head = sublist_head.get_next_node()
                    locations_linked_list_head = locations_linked_list_head.get_next_node()

    # Print path to selected resource from the start location
    exit_path_finding = 'n'
    while exit_path_finding == 'n':
        # Choose place to visit from searching results
        print('\nWhere do you want to go? \nChoose a number from list below:')
        for key, value in matching_places.items():
            print(f'-- {key} - {value}')
        index_to_go = str(input('Your choice: '))
        place_to_go = matching_places[index_to_go]

        # Choose starting place
        print('\nWhere you are? \nChoose a number from list below:')
        for key, value in locations_names.items():
            print(f'-- {key} - {value}')
        index_start = str(input('Your choice: '))
        start_place = locations_names[index_start]

        move_range = int(input('What is your move range? Type integer number: '))

        # Show possible path
        possible_path = city_map.split_path(start_place, place_to_go, move_range)
        print(f'\nIt takes you {len(possible_path)} round(s) to arrive to {place_to_go} from {start_place}.')
        print('You can go this way: ')
        for i in range(0, len(possible_path)):
            print(f'{i + 1}: {possible_path[i]}')
        
        # Exit path search loop
        exit_path_question = input('Do you want to end path search? For yes type y, for no type n: ').lower()
        if exit_path_question == 'y':
            exit_path_finding = 'y'
    
    # Exit the main loop
    question = str(input("\nDo you want finish searching for resources? (for yes type 'y'): ")).lower()
    if question == 'y':
        want_finish = 'y'

    