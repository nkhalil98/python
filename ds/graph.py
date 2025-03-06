"""
Graph
"""

from __future__ import annotations

from collections import deque


class Vertex:
    def __init__(self, val):
        self.val: str = val
        self.edges: dict[Vertex, int] = {}

    def add_edge(self, vertex: Vertex, weight=0):
        self.edges[vertex] = weight

    def get_edges(self):
        return set(self.edges.keys())

    def __hash__(self):
        return hash(self.val)

    def __eq__(self, other):
        if not isinstance(other, Vertex):
            return False
        return self.val == other.val


class Graph:
    def __init__(self, is_directed=False):
        self.graph_dict: dict[str, Vertex] = {}
        self.is_directed = is_directed

    def add_vertex(self, vertex: Vertex):
        self.graph_dict[vertex.val] = vertex

    def add_edge(self, from_vertex: Vertex, to_vertex: Vertex, weight=0):
        if (
            from_vertex.val not in self.graph_dict
            or to_vertex.val not in self.graph_dict
        ):
            raise ValueError("Both vertices must exist in the graph")
        self.graph_dict[from_vertex.val].add_edge(to_vertex, weight)
        if not self.is_directed:
            self.graph_dict[to_vertex.val].add_edge(from_vertex, weight)

    def find_path(self, start_vertex: Vertex, end_vertex: Vertex) -> bool:
        if (
            start_vertex.val not in self.graph_dict
            or end_vertex.val not in self.graph_dict
        ):
            return False
        visited = set()
        queue = deque([start_vertex])
        while queue:
            current = queue.popleft()
            if current == end_vertex:
                return True
            visited.add(current)
            for neighbor in self.graph_dict[current.val].edges.keys():
                if neighbor not in visited:
                    queue.append(neighbor)
        return False
