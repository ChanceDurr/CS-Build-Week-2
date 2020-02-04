import time
import random
import endpoints as action
import t_graph
import sys

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def cooldown(data):
    print('Waiting for cooldown')
    wait_time = int(data['cooldown'])
    time.sleep(wait_time)
    print('Cooldown Done')
    





data = action.get_room_data()
if '-start' in sys.argv:
    t_graph.add_room({data['room_id']: {i: '?' for i in data['exits']}})

# Explore until full inventory?
while True:
    # Get room data
    cooldown(data)

    # Choose a random direction to explore
    current_paths = data['exits']
    unexplored_paths = []
    for k, v in t_graph.get_rooms()[data['room_number']]:
        for path in current_paths:
            if v[path] == '?':
                unexplored_paths.append(path)


    choice = random.choice(unexplored_paths)

    data = action.move(choice)


t_graph.add_room({"80": {'n': '?', 'e': '?', 's': '?', 'w': '?', 'title': "A Shop"}})


print(t_graph.get_rooms())

