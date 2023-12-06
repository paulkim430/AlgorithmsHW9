def solve_tsp(graph):
    nodes = len(graph)
    visited = [False] * nodes
    path = [0]
    visited[0] = True

    while len(path) < nodes:
        current_node = path[-1]
        nearest_node = None
        min_distance = float('inf')

        for next_node in range(nodes):
            if 0 < graph[current_node][next_node] < min_distance and not visited[next_node]:
                nearest_node = next_node
                min_distance = graph[current_node][next_node]

        if nearest_node is None:
            break

        path.append(nearest_node)
        visited[nearest_node] = True

    path.append(0)
    return path


