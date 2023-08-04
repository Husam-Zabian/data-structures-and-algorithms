from graph.graph import Graph

def depth_first(Graph, start_node):
    visited = set()
    traversal_order = []

    def dfs_helper(node):
        visited.add(node)
        traversal_order.append(node)

        neighbors = Graph.get_neighbors(node)
        for neighbor, _ in neighbors:
            if neighbor not in visited:
                dfs_helper(neighbor)

    dfs_helper(start_node)
    return traversal_order
