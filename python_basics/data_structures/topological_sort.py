from collections import deque


def topoligical_sort(vertices, edges):
    sort_order = []
    if vertices == 0:
        return sort_order
    # 1. Initialize the graph
    in_degree = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}

    print(f"1 :In degree : {in_degree}, Graph : {graph}")

    # 2. Build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        in_degree[child] += 1
    print(f"2 :In degree : {in_degree}, Graph : {graph}")

    # 3. Find all sources
    sources = deque()
    for node, value in in_degree.items():
        if value == 0:
            sources.append(node)
    print(f"3 :Sources : {sources}")

    # 4. For each source find, add it to the sort_order and decremnt in_degree for all of its childrens
    while sources:
        vertex = sources.popleft()
        sort_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)
    print(
        f"4 :In degree : {in_degree}, Graph : {graph}, Sources : {sources}, Sort order: {sort_order}")

    # 5. Topological sor is not possible as the graph has cycle
    if len(sort_order) < vertices:
        print("5. Cycle detected in graph")
        return []
    return sort_order


vertices = 4
edges = [3, 2], [3, 0], [2, 0], [2, 1], [2, 3]
print(topoligical_sort(vertices, edges))
