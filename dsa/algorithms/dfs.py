"""
Depth First Search (DFS)
    - Tree DFS
    - Graph DFS
"""

from __future__ import annotations

from data_structures.tree import TreeNode


def tree_dfs(root: TreeNode, target, path=None):
    if path is None:
        path = []

    path.append(root)

    if root.val == target:
        return path

    for child in root.children:
        path_found = tree_dfs(child, target, path)

        if path_found is not None:
            return path_found

    return None


def graph_dfs(graph: dict, start, target, visited=None):
    if visited is None:
        visited = []

    visited.append(start)

    if start == target:
        return visited

    for neighbor in graph[start]:
        if neighbor not in visited:
            path = graph_dfs(graph, neighbor, target, visited)
            if path:
                return path

    return None
