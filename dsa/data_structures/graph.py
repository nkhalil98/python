"""
Graph
"""

from __future__ import annotations

from collections import deque


class Graph:
    def __init__(self, edges: list[tuple[str, str]]):
        self.graph_dict = {}
        for src, dest in edges:
            if src in self.graph_dict:
                self.graph_dict[src].append(dest)
            else:
                self.graph_dict[src] = [dest]

    def find_path_bst(self, start_vertex: str, end_vertex: str) -> bool:
        if start_vertex not in self.graph_dict or end_vertex not in self.graph_dict:
            return False
        visited = set()
        queue = deque([start_vertex])
        while queue:
            current = queue.popleft()
            if current == end_vertex:
                return True
            visited.add(current)
            for neighbor in self.graph_dict.get(current, []):
                if neighbor not in visited:
                    queue.append(neighbor)
        return False

    def find_path_dfs(self, start_vertex: str, end_vertex: str) -> bool:
        if start_vertex not in self.graph_dict or end_vertex not in self.graph_dict:
            return False
        visited = set()
        stack = [start_vertex]
        while stack:
            current = stack.pop()
            if current == end_vertex:
                return True
            visited.add(current)
            for neighbor in self.graph_dict.get(current, []):
                if neighbor not in visited:
                    stack.append(neighbor)
        return False

    def find_path_dfs_recursive(
        self, start_vertex: str, end_vertex: str, visited=None
    ) -> bool:
        if visited is None:
            visited = set()
        if start_vertex not in self.graph_dict or end_vertex not in self.graph_dict:
            return False
        if start_vertex == end_vertex:
            return True
        visited.add(start_vertex)
        for neighbor in self.graph_dict.get(start_vertex, []):
            if neighbor not in visited:
                if self.find_path_dfs_recursive(neighbor, end_vertex, visited):
                    return True
        return False

    def get_all_paths_dfs_recursive(
        self, start_vertex: str, end_vertex: str, path=None
    ) -> list[list[str]]:
        if path is None:
            path = []
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in self.graph_dict:
            return []
        paths = []
        for neighbor in self.graph_dict.get(start_vertex, []):
            if neighbor not in path:
                new_paths = self.get_all_paths_dfs_recursive(neighbor, end_vertex, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path_dfs_recursive(
        self, start_vertex: str, end_vertex: str, path=None
    ) -> list[str] | None:
        if path is None:
            path = []
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in self.graph_dict:
            return None
        shortest_path = None
        for neighbor in self.graph_dict.get(start_vertex, []):
            if neighbor not in path:
                sp = self.get_shortest_path_dfs_recursive(neighbor, end_vertex, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path

    def get_shortest_path_bst(
        self, start_vertex: str, end_vertex: str
    ) -> list[str] | None:
        if start_vertex not in self.graph_dict or end_vertex not in self.graph_dict:
            return None
        queue = deque([(start_vertex, [start_vertex])])
        while queue:
            current, path = queue.popleft()
            if current == end_vertex:
                return path
            for neighbor in self.graph_dict.get(current, []):
                if neighbor not in path:
                    queue.append((neighbor, path + [neighbor]))
        return None
