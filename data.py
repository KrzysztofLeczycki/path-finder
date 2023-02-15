# Based on Arkham Horror second edition boardgame
locations = [
    {'name': 'Northside', 
    'connections': [
        {'name': 'Train station', 'length': 1}, 
        {'name': 'Redaction', 'length': 1}, 
        {'name': 'Antique shop', 'length': 1}, 
        {'name': 'Downtown', 'length': 1}, 
        {'name': 'Trade District', 'length': 1}
        ], 
    'resources':[]},

    {'name': 'Train station', 
    'connections': [
        {'name': 'Northside', 'length': 1}, 
        ], 
    'resources':['unique items', 'common items']},

    {'name': 'Redaction', 
    'connections': [
        {'name': 'Northside', 'length': 1}, 
        ], 
    'resources':['money', 'information']},

    {'name': 'Antique shop', 
    'connections': [
        {'name': 'Northside', 'length': 1}, 
        ], 
    'resources':['unique items', 'common items']},

    {'name': 'Downtown', 
    'connections': [
        {'name': 'Asylum', 'length': 1}, 
        {'name': 'Bank', 'length': 1}, 
        {'name': 'The Independence Square', 'length': 1}, 
        {'name': 'Northside', 'length': 1}, 
        {'name': 'Trade District', 'length': 1}, 
        {'name': 'Easttown', 'length': 1}
        ], 
    'resources':[]},

    {'name': 'Asylum', 
    'connections': [
        {'name': 'Downtown', 'length': 1}, 
        ], 
    'resources':['mind health', 'information']},

    {'name': 'Bank', 
    'connections': [
        {'name': 'Downtown', 'length': 1}, 
        ], 
    'resources':['money']},

    {'name': 'The Independence Square', 
    'connections': [
        {'name': 'Downtown', 'length': 1}, 
        ], 
    'resources':['unique items', 'information']},

    {'name': 'Easttown', 
    'connections': [
        {'name': 'East Inn', 'length': 1}, 
        {'name': 'Restaurant', 'length': 1}, 
        {'name': 'Downtown', 'length': 1}, 
        {'name': 'Police Station', 'length': 1}, 
        {'name': 'Rivertown', 'length': 1}
        ], 
    'resources':[]},

    {'name': 'East Inn', 
    'connections': [
        {'name': 'Easttown', 'length': 1}, 
        ], 
    'resources':['money', 'common items']},

    {'name': 'Restaurant', 
    'connections': [
        {'name': 'Easttown', 'length': 1}, 
        ], 
    'resources':['money', 'health']},

    {'name': 'Police Station', 
    'connections': [
        {'name': 'Easttown', 'length': 1}, 
        ], 
    'resources':['common items', 'information']},

    {'name': 'Rivertown', 
    'connections': [
        {'name': 'Cementary', 'length': 1}, 
        {'name': 'Cave', 'length': 1}, 
        {'name': 'Shop', 'length': 1}, 
        {'name': 'Easttown', 'length': 1}, 
        {'name': 'French Hill', 'length': 1}, 
        {'name': 'Trade District', 'length': 1}
        ], 
    'resources':[]},

    {'name': 'Cementary', 
    'connections': [
        {'name': 'Rivertown', 'length': 1}, 
        ], 
    'resources':['unique items', 'information']},

    {'name': 'Cave', 
    'connections': [
        {'name': 'Rivertown', 'length': 1}, 
        ], 
    'resources':['common items', 'spells']},

    {'name': 'Shop', 
    'connections': [
        {'name': 'Rivertown', 'length': 1}, 
        ], 
    'resources':['common items', 'money']},

    {'name': 'Trade District', 
    'connections': [
        {'name': 'Unknown', 'length': 1}, 
        {'name': 'River Docks', 'length': 1}, 
        {'name': 'Deserted Island', 'length': 1}, 
        {'name': 'Northside', 'length': 1}, 
        {'name': 'University', 'length': 1}, 
        {'name': 'Downtown', 'length': 1},
        {'name': 'Rivertown', 'length': 1}
        ], 
    'resources':[]},

    {'name': 'Deserted Island', 
    'connections': [
        {'name': 'Trade District', 'length': 1}, 
        ], 
    'resources':['spells', 'information']},

    {'name': 'Unknown', 
    'connections': [
        {'name': 'Trade District', 'length': 1}, 
        ], 
    'resources':['unique items', 'information']},

    {'name': 'Docks', 
    'connections': [
        {'name': 'Trade District', 'length': 1}, 
        ], 
    'resources':['money', 'common items']},

    {'name': 'University', 
    'connections': [
        {'name': 'The Science Building', 'length': 1}, 
        {'name': 'The Administration Building', 'length': 1}, 
        {'name': 'Library', 'length': 1}, 
        {'name': 'Uptown', 'length': 1}, 
        {'name': 'French Hill', 'length': 1}, 
        {'name': 'Trade District', 'length': 1}
        ], 
    'resources':[]},

    {'name': 'The Science Building', 
    'connections': [
        {'name': 'University', 'length': 1}, 
        ], 
    'resources':['unique items', 'information']},

    {'name': 'The Administration Building', 
    'connections': [
        {'name': 'University', 'length': 1}, 
        ], 
    'resources':['money', 'skills']},

    {'name': 'Library', 
    'connections': [
        {'name': 'University', 'length': 1}, 
        ], 
    'resources':['unique items', 'spells']},

    {'name': 'French Hill', 
    'connections': [
        {'name': 'Lodge', 'length': 1}, 
        {'name': "The Witch's House", 'length': 1}, 
        {'name': 'University', 'length': 1}, 
        {'name': 'Rivertown', 'length': 1}, 
        {'name': 'Southside', 'length': 1}
        ], 
    'resources':[]},

    {'name': "The Witch's House", 
    'connections': [
        {'name': 'French Hill', 'length': 1}, 
        ], 
    'resources':['spells', 'information']},

    {'name': 'Lodge', 
    'connections': [
        {'name': 'French Hill', 'length': 1}, 
        ], 
    'resources':['unique items', 'information']},

    {'name': 'Southside', 
    'connections': [
        {'name': 'Guesthouse', 'length': 1}, 
        {'name': "Church", 'length': 1}, 
        {'name': 'Historical Association', 'length': 1}, 
        {'name': 'French Hill', 'length': 1}, 
        {'name': 'Uptown', 'length': 1}, 
        ], 
    'resources':[]},

    {'name': 'Guesthouse', 
    'connections': [
        {'name': 'SouthSide', 'length': 1}, 
        ], 
    'resources':['health', 'allies']},

    {'name': 'Church', 
    'connections': [
        {'name': 'SouthSide', 'length': 1}, 
        ], 
    'resources':['mind health']},

    {'name': 'Historical Association', 
    'connections': [
        {'name': 'SouthSide', 'length': 1}, 
        ], 
    'resources':['skills', 'spells']},

    {'name': 'Uptown', 
    'connections': [
        {'name': 'Forest', 'length': 1}, 
        {'name': "Old Shop", 'length': 1}, 
        {'name': 'Hospital', 'length': 1}, 
        {'name': 'Southside', 'length': 1}, 
        {'name': 'University', 'length': 1}, 
        ], 
    'resources':[]},

    {'name': 'Forest', 
    'connections': [
        {'name': 'Uptown', 'length': 1}, 
        ], 
    'resources':['money', 'common items']},

    {'name': 'Old Shop', 
    'connections': [
        {'name': 'Uptown', 'length': 1}, 
        ], 
    'resources':['spells', 'unique items']}, 

    {'name': 'Hospital', 
    'connections': [
        {'name': 'Uptown', 'length': 1}, 
        ], 
    'resources':['health', 'information']}
]

resources_list = set()
for location in locations:
    if location['resources'] is not None:
        for resource in location['resources']:
            resources_list.add(resource)
