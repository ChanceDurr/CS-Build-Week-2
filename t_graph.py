import json

def get_rooms(filename='traversal_graph.json'):
    with open(filename, 'r') as f:
        graph = json.load(f)
        return graph

def write_json(data, filename='traversal_graph.json'):
    with open(filename, 'w', ) as f:
        json.dump(data, f, indent=4)

def add_room(room_data):
    """
    Data must be in {"0": {"n": '?', 'e' : 4, 's': 5, 'w': 2}}
    format

    Add to json or updates room
    """
    with open('traversal_graph.json') as json_file:
        data = json.load(json_file)

        for k, v in room_data.items():
            data[k] = v

    write_json(data)
