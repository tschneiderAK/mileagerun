edges = [[0,1],[1,2]]
patience = [0,2,1]

# First create a hashtable to store the pathlen for each server, and one to store servers adjacent to server i
n = len(patience)
pathlens = {}
adj = {i:set() for i in range(n)}
# Now iterate over edges and add them to adj
for edge in edges:
    adj[edge[0]].add(edge[1])
    adj[edge[1]].add(edge[0])
# Now we need to traverse these adjacent servers to determine path lens. We can do this with bfs using a queue.
q = [0]
level = 0
# We want to continue traversing the network until there are no more servers to map.
while q:
    # Loop over the number of servers in the queue at this level.
    for i in range(len(q)):
        server = q.pop(0)

        # Only want to process servers we haven't seen before. This way we avoid loops and using less efficient paths
        if server not in pathlens:
            # Add the server to the level.
            pathlens[server] = level
            # There may be duplicates, but this is OK as we wll only process once
            for adjacent in adj[server]:
                q.append(adjacent)

    # Once we iterate through the level, we increase the level.
    level += 1
# Now we have pathlens, so we can calculate the time until silent.
print(max([3*pathlens[i] - min(patience[i],pathlens[i]) for i in range(1,n)]))