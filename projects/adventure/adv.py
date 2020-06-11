from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

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
map_file = "projects/adventure/maps/test_line.txt"
# map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "projects/adventure/maps/test_loop_fork.txt"
# map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

# start in room 0
player = Player(world.starting_room)

visited = {}
visited[player.current_room.id] = True

print(player.current_room.get_exits())
print(world.rooms[0].get_room_in_direction('n'))
newRoom = world.rooms[0].get_room_in_direction('n').id
print(newRoom)
print(len(world.rooms))

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def traverse():
    found_exit = True
    while found_exit:
        found_exit = False
        exits = player.current_room.get_exits()
        # go to first unexplored (?) direction
        for direction in exits:
            if player.current_room.get_room_in_direction(direction).id not in visited:
                player.travel(direction)
                traversal_path.append(direction)
                visited[player.current_room.id] = True
                found_exit = True
                break
        # loop until no unexplored direction

def find_unexplored():
    opposite_direction = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
    backward_path = []
    index = len(traversal_path) - 1
    found_new_path = False
    while index >= 0 and not found_new_path:
        # walk backward through traversal_path
        direction = opposite_direction[traversal_path[index]]
        index -= 1
        player.travel(direction)
        # add directions to path as you traverse
        backward_path.append(direction)
        # check for unexplored exits at each room
        exits = player.current_room.get_exits()
        for d in exits:
            # go to the first unexplored room
            if player.current_room.get_room_in_direction(d).id not in visited:
                # we found an unexplored room
                player.travel(d)
                # extend traversal path with backward path
                traversal_path.extend(backward_path)
                traversal_path.append(d)
                visited[player.current_room.id] = True
                found_new_path = True
                break

while len(world.rooms) != len(visited):
    traverse()
    # use bft to find the shortest path back to an unexplored direction
    # If visited == number of rooms, all rooms are explored 
    if len(visited) != len(world.rooms):
        find_unexplored()



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
