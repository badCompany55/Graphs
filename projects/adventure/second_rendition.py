
def backtrack_to_unexplored(starting_vertex_id):
    """
    Making a list of all the rooms that haven't been explored in the graph
    """
    # FIFO, create a queue
    q = Queue()
    q.put([starting_vertex_id])
    visited = set()
    # roomGraph = {0: [(3, 5), {'n': 1}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}]}
    # graph = {0: {"n": "?", "e": "?", "s": "?", "w": "?"}}
    while not q.empty():
        path = q.get()
        v1 = path[-1]  # looking at last item which is your current room id
        if v1 not in visited:
            # graph[v1] exit dictionary
            for exit in graph[v1]:
                if graph[v1][exit] == '?':
                    return path  # path to the room we haven't explored yet
            # else add it back to the queue
            visited.add(v1)
            for exit_direction in graph[v1]:  # exit_direction is the key
                new_path = list(path)
                # appends room number
                new_path.append(graph[v1][exit_direction])
                q.put(new_path)
    return None


def path_to_directions(path):
    """
    takes list of room ids and converts them to a list direction (ex: [n, s, e])
    """
    current_room = path[0]
    directions = []
    # iterate through out room IDs except the current room (path[0])
    for room in path[1:]:
        for exit in graph[current_room]:
            if room == graph[current_room][exit]:
                # appends n, e, s, w to the directions list
                directions.append(exit)
    return directions


# find the shortest moves to visit all rooms (will not be the same every time)
while True:
    # get the value of all exits for current room
    currentRoomExits = graph[player.currentRoom.id]
    # graph = {0: {"n": "?", "e": "?", "s": "?", "w": "?"}}
    unExploredExits = []  # all unexplored exits

    # this is for when you want to find '?' to explore
    for direction in currentRoomExits:
        if currentRoomExits[direction] == '?':
            # during the first run, unExploredExits = ['n', 'e', 's', 'w']
            unExploredExits.append(direction)

    if len(unExploredExits) > 0:  # picking one of the unexplored exits
        # sampling one thing out of unExplored Exits
        firstExit = random.sample(unExploredExits, 1)[0]
        # will walk in that direction to that exit
        traversalPath.append(firstExit)
        # so you can refer to inverse directions (n -> s)
        prev_room_id = player.currentRoom.id

        # walk in direction to the exit; updates the current Room
        player.travel(firstExit)

        exitDict = {}  # now we're in the next room; new room
        if player.currentRoom.id not in graph:
            for exit in player.currentRoom.getExits():
                # set every exit in getExits as the key to with '?'
                exitDict[exit] = '?'
            graph[player.currentRoom.id] = exitDict

        # graph[0]['n'] = '?' --> 1
        # previous {room 0: {'n': 1, 'e': '?', 's': 0, 'w': '?'}}
        graph[prev_room_id][firstExit] = player.currentRoom.id

        # inverse_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
        # new {room 1: {'n': '?', 'e': '?', 's': 0, 'w': '?'}}
        graph[player.currentRoom.id][inverse_directions[firstExit]] = prev_room_id
    else:
        # when you hit a dead end back track
        # to the nearest room with an unexplored exit bfs path finding
        path_to_unexplored = backtrack_to_unexplored(player.currentRoom.id)
        print(f"path_to_unexplored = {path_to_unexplored}")
        if path_to_unexplored is None:
            break
        for direction in path_to_directions(path_to_unexplored):
            player.travel(direction)  # player walks
            traversalPath.append(direction)  # directions that player will walk


# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)
for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.currentRoom)

if len(visited_rooms) == len(roomGraph):
    print(
        f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")
