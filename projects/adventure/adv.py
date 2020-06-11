from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

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

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "projects/adventure/maps/test_line.txt"
# map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "projects/adventure/maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

# start in room 0
player = Player(world.starting_room)

visited = {}
visited[player.current_room.id] = True

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
rooms_to_visit = Stack()

def traverse():
    found_exit = True
    while found_exit:
        found_exit = False
        exits = player.current_room.get_exits()
        # go to first unexplored (?) direction
        current = player.current_room
        for direction in exits:
            if current.get_room_in_direction(direction).id not in visited:
                if found_exit:
                    rooms_to_visit.push(current.get_room_in_direction(direction).id)
                else:
                    player.travel(direction)
                    traversal_path.append(direction)
                    visited[player.current_room.id] = True
                    found_exit = True
        # loop until no unexplored direction

def find_shortest_path_to_unexplored():
    visited_room = set()

    q = Queue()
    q2 = Queue()

    q.enqueue([])
    q2.enqueue(player.current_room)
    destination = rooms_to_visit.pop()

    while q.size() > 0:
        path = q.dequeue()
        current = q2.dequeue()
        if current.id not in visited_room:
            visited_room.add(current.id)
            if current.id == destination:
                return path
            exits = current.get_exits()
            for direction in exits:
                path_copy = list(path)
                path_copy.append(direction)
                q.enqueue(path_copy)
                q2.enqueue(current.get_room_in_direction(direction))
    return None

def find_unexplored(path):
    # move player along path to unexplored
    for direction in path:
        player.travel(direction)
        traversal_path.append(direction)
    visited[player.current_room.id] = True

while len(world.rooms) > len(visited):
    traverse()
    if len(visited) != len(world.rooms):
        path = find_shortest_path_to_unexplored()
        find_unexplored(path)



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
