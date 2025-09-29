"""
Breath First Search (BFS)
    - Tree BFS
    - Graph BFS
"""

from __future__ import annotations


from collections import deque
from data_structures.tree import TreeNode


def tree_bfs(root: TreeNode, target):
    path_queue = deque()
    initial_path = [root]
    path_queue.appendleft(initial_path)

    while path_queue:
        current_path = path_queue.pop()
        current_node = current_path[-1]

        if current_node.val == target:
            return current_path

        for child in current_node.children:
            new_path = current_path[:]
            new_path.append(child)
            path_queue.appendleft(new_path)

    return None


def graph_bfs(graph: dict, start, target):
    path = [start]
    vertex_and_path = (start, path)
    bfs_queue = deque([vertex_and_path])
    visited = set()

    while bfs_queue:
        current_vertex, path = bfs_queue.popleft()
        visited.add(current_vertex)
        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                if neighbor == target:
                    return path + [neighbor]
                else:
                    bfs_queue.append((neighbor, path + [neighbor]))

    return None
