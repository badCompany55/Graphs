from room import Room
from player import Player
from world import World
from queue import LifoQueue
from queue import Queue
from big_room import roomGraph

import random

# Load world
world = World()

roomGraph = roomGraph

# You may uncomment the smaller graphs for development and testing purposes.
# roomGraph={0: [(3, 5), {'n': 1}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}]}
# roomGraph={0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}], 4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 6: [(3, 3), {'n': 5}], 7: [(2, 5), {'w': 8, 'e': 0}], 8: [(1, 5), {'e': 7}]}
# roomGraph={0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}], 4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 6: [(3, 3), {'n': 5, 'w': 11}], 7: [(2, 5), {'w': 8, 'e': 0}], 8: [(1, 5), {'e': 7}], 9: [(1, 4), {'n': 8, 's': 10}], 10: [(1, 3), {'n': 9, 'e': 11}], 11: [(2, 3), {'w': 10, 'e': 6}]}
# roomGraph={0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}], 1: [(3, 6), {'s': 0, 'n': 2, 'e': 12, 'w': 15}], 2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}], 4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 6: [(3, 3), {'n': 5, 'w': 11}], 7: [(2, 5), {'w': 8, 'e': 0}], 8: [(1, 5), {'e': 7}], 9: [(1, 4), {'n': 8, 's': 10}], 10: [(1, 3), {'n': 9, 'e': 11}], 11: [(2, 3), {'w': 10, 'e': 6}], 12: [(4, 6), {'w': 1, 'e': 13}], 13: [(5, 6), {'w': 12, 'n': 14}], 14: [(5, 7), {'s': 13}], 15: [(2, 6), {'e': 1, 'w': 16}], 16: [(1, 6), {'n': 17, 'e': 15}], 17: [(1, 7), {'s': 16}]}

world.loadGraph(roomGraph)
player = Player("Name", world.startingRoom)


# FILL THIS IN
traversalPath = []


graph = {0: {"n": "?", "e": "?", "s": "?", "w": "?"}}

# when reaching a dead end, turn around
inverse_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}



# UNCOMMENT TO VIEW MAP
# world.printRooms()

player = Player("Name", world.startingRoom)

# Fill this out
s = LifoQueue()
q = Queue()
visited_rooms = set()
graph = {}
traversalPath = []

s.put(player.currentRoom)

def dead_end_check(room):
    dead_end = True
    for v in room.values():
        if v == '?':
            dead_end = False
    return dead_end

while not s.empty():
    if len(graph) == len(roomGraph):
        # print(len(graph))
        # print(len(roomGraph))
        break

    current_room = s.get()
    # print(current_room.getExits())
    # print(current_room.id)

    if current_room.id not in visited_rooms:
        visited_rooms.add(current_room.id)

        directions = current_room.getExits()

        if current_room.id not in graph:
            initial_direction = {}
            for e in directions:
                initial_direction[e] = '?'
            graph[current_room.id] = initial_direction

        index = random.randrange(0, len(directions), 1)
        direction = directions[index]

        dead_end = dead_end_check(graph[current_room.id])
        # print("63", dead_end)

        if not dead_end:
            # print("first")
            while graph[current_room.id][direction] is not '?':
                index = random.randrange(0, len(directions), 1)
                direction = directions[index]

            if graph[current_room.id][direction] == '?':
                traversalPath.append(direction)
                player.travel(direction)
                new_room = player.currentRoom
                graph[current_room.id][direction] = new_room.id
                directions = new_room.getExits()
                # print("directions", directions)


                if new_room.id not in graph:
                    initial_direction = {}
                    for e in directions:
                        initial_direction[e] = '?'
                    graph[new_room.id] =  initial_direction

                if direction == 'n':
                    graph[new_room.id]['s'] = current_room.id
                elif direction == 's':
                    graph[new_room.id]['n'] = current_room.id
                elif direction == 'e':
                    graph[new_room.id]['w'] = current_room.id
                elif direction == 'w':
                    graph[new_room.id]['e'] = current_room.id


                s.put(player.currentRoom)
            # print(graph)
        else:
            # print("second")
            q.put(player.currentRoom)
            while not q.empty():
                current_room = q.get()
                dead_end = dead_end_check(graph[current_room.id])
                dead_end_visit = set()
                counter = 0
                while dead_end or (current_room.id in dead_end_visit):

                    dead_end_visit.add(current_room.id)
                    directions = current_room.getExits()
                    index = random.randrange(0, len(directions), 1)
                    direction = directions[index]
                    traversalPath.append(direction)
                    player.travel(direction)
                    q.put(player.currentRoom)
                    current_room = q.get()
                    dead_end = dead_end_check(graph[current_room.id])

                if not dead_end:
                    directions = current_room.getExits()
                    index = random.randrange(0, len(directions), 1)
                    direction = directions[index]

                    while graph[current_room.id][direction] is not '?':
                        index = random.randrange(0, len(directions), 1)
                        direction = directions[index]

                    if graph[current_room.id][direction] == '?':
                        traversalPath.append(direction)
                        player.travel(direction)
                        new_room = player.currentRoom
                        graph[current_room.id][direction] = new_room.id
                        directions = new_room.getExits()
                        # print("directions", directions)


                        if new_room.id not in graph:
                            initial_direction = {}
                            for e in directions:
                                initial_direction[e] = '?'
                            graph[new_room.id] =  initial_direction

                        if direction == 'n':
                            graph[new_room.id]['s'] = current_room.id
                        elif direction == 's':
                            graph[new_room.id]['n'] = current_room.id
                        elif direction == 'e':
                            graph[new_room.id]['w'] = current_room.id
                        elif direction == 'w':
                            graph[new_room.id]['e'] = current_room.id

                        s.put(player.currentRoom)
                    # print(graph)

    else:

        directions = current_room.getExits()
        index = random.randrange(0, len(directions), 1)
        direction = directions[index]

        # print(graph[current_room.id])
        dead_end = dead_end_check(graph[current_room.id])
        # print(dead_end)
        # print("149", dead_end)

        if not dead_end:
            # print("third")
            while graph[current_room.id][direction] is not '?':
                index = random.randrange(0, len(directions), 1)
                direction = directions[index]

            if graph[current_room.id][direction] == '?':
                traversalPath.append(direction)
                player.travel(direction)
                new_room = player.currentRoom
                graph[current_room.id][direction] = new_room.id
                directions = new_room.getExits()
                # print(" 109 directions", directions)


                if new_room.id not in graph:
                    initial_direction = {}
                    for e in directions:
                        initial_direction[e] = '?'
                    graph[new_room.id] =  initial_direction

                if direction == 'n':
                    graph[new_room.id]['s'] = current_room.id
                elif direction == 's':
                    graph[new_room.id]['n'] = current_room.id
                elif direction == 'e':
                    graph[new_room.id]['w'] = current_room.id
                elif direction == 'w':
                    graph[new_room.id]['e'] = current_room.id

                s.put(player.currentRoom)

        else:
            # print("fourth")

            q.put(player.currentRoom)
            while not q.empty():
                current_room = q.get()
                dead_end = dead_end_check(graph[current_room.id])
                while dead_end:
                    directions = current_room.getExits()
                    index = random.randrange(0, len(directions), 1)
                    direction = directions[index]
                    traversalPath.append(direction)
                    player.travel(direction)
                    q.put(player.currentRoom)
                    current_room = q.get()
                    dead_end = dead_end_check(graph[current_room.id])

                if not dead_end:
                    directions = current_room.getExits()
                    index = random.randrange(0, len(directions), 1)
                    direction = directions[index]

                    while graph[current_room.id][direction] is not '?':
                        index = random.randrange(0, len(directions), 1)
                        direction = directions[index]

                    if graph[current_room.id][direction] == '?':
                        traversalPath.append(direction)
                        player.travel(direction)
                        new_room = player.currentRoom
                        graph[current_room.id][direction] = new_room.id
                        directions = new_room.getExits()
                        # print("directions", directions)


                        if new_room.id not in graph:
                            initial_direction = {}
                            for e in directions:
                                initial_direction[e] = '?'
                            graph[new_room.id] =  initial_direction

                        if direction == 'n':
                            graph[new_room.id]['s'] = current_room.id
                        elif direction == 's':
                            graph[new_room.id]['n'] = current_room.id
                        elif direction == 'e':
                            graph[new_room.id]['w'] = current_room.id
                        elif direction == 'w':
                            graph[new_room.id]['e'] = current_room.id

                        s.put(player.currentRoom)
        # print(graph)










# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)

for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.currentRoom)

if len(visited_rooms) == len(roomGraph):
    print(f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")



#####
# UNCOMMENT TO WALK AROUND
# ######
# player.currentRoom.printRoomDescription(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     else:
#         print("I did not understand that command.")
