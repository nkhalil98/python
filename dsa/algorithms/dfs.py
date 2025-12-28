"""
Depth First Search (DFS)
    - Tree DFS
    - Graph DFS
"""

from __future__ import annotations

from collections import deque
from typing import Dict

# from overload import overload

from data_structures.tree import TreeNode


def tree_dfs_has_path(root: TreeNode, target) -> bool:
    if root.value == target:
        return True

    for child in root.children:
        if tree_dfs_has_path(child, target):
            return True

    return False


def tree_dfs_find_path(root: TreeNode, target, path=None):
    if path is None:
        path = []

    path.append(root)

    if root.value == target:
        return path

    for child in root.children:
        path_found = tree_dfs_find_path(child, target, path)

        if path_found:
            return path_found

    return []


def iterative_tree_dfs(root: TreeNode, target):
    stack = deque([root])

    while stack:
        current_path = stack.pop()
        current_node = current_path[-1]

        if current_node.value == target:
            return current_path

        for child in current_node.children:
            new_path = current_path + [child]
            stack.append(new_path)

    return []


def graph_dfs(graph: Dict, start, target, visited=None):
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

    return []
