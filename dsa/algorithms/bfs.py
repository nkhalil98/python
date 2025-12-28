"""
Breath First Search (BFS)
    - Tree BFS
    - Graph BFS
"""

from __future__ import annotations

from collections import deque
from typing import Dict

from data_structures.tree import TreeNode


def tree_bfs_has_path(root: TreeNode, target) -> bool:
    queue = deque([root])

    while queue:
        current_node = queue.pop()

        if current_node.value == target:
            return True

        for child in current_node.children:
            queue.appendleft(child)

    return False


def tree_bfs_find_path(root: TreeNode, target):
    queue = deque([[root]])

    while queue:
        current_path = queue.pop()
        current_node = current_path[-1]

        if current_node.value == target:
            return current_path

        for child in current_node.children:
            new_path = current_path[:] + [child]
            queue.appendleft(new_path)

    return []


def graph_bfs(graph: Dict, start, target):
    path = [start]
    vertex_and_path = (start, path)
    bfs_queue = deque([vertex_and_path])
    visited = set()

    while bfs_queue:
        current_vertex, path = bfs_queue.pop()
        visited.add(current_vertex)
        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                if neighbor == target:
                    return path + [neighbor]
                else:
                    bfs_queue.appendleft((neighbor, path + [neighbor]))

    return []
