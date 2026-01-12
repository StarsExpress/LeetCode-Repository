
def find_min_reorder(connections: list[list[int]]) -> int:  # LeetCode Q.1466.
    reversed_graph: dict[int, set[int]] = dict()  # Key: end node.
    graph: dict[int, set[int]] = dict()  # Key: start node.
    
    for start, end in connections:
        if end not in reversed_graph.keys():
            reversed_graph[end] = set()
        reversed_graph[end].add(start)
        
        if start not in graph.keys():
            graph[start] = set()
        graph[start].add(end)
    
    min_changes = 0
    queue = [0]  # Always start from capital.
    visited_nodes = set()
    
    while queue:
        node = queue.pop(0)
        visited_nodes.add(node)

        # Go to next level BFS to check potential flips.
        if node in graph.keys():
            for outgoing_node in graph[node]:
                if outgoing_node not in visited_nodes:
                    queue.append(outgoing_node)
                    min_changes += 1  # Flip to let this outgoing node visit current node.
        
        if node in reversed_graph.keys():
            for incoming_node in reversed_graph[node]:
                if incoming_node not in visited_nodes:
                    queue.append(incoming_node)
    
    return min_changes
