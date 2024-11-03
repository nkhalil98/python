from vertex import Vertex


class Graph:
    def __init__(self, is_directed=False):
        self.graph_dict = {}
        self.is_directed = is_directed

    def add_vertex(self, vertex: Vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex: Vertex, to_vertex: Vertex, weight=0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.is_directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

    def find_path(self, start_vertex: Vertex, end_vertex: Vertex):
        start = [start_vertex]
        visited = {}
        while len(start) > 0:
            current_vertex = start.pop(0)
            visited[current_vertex] = True
            if current_vertex == end_vertex:
                return True
            else:
                vertices_to_visit = set(self.graph_dict[current_vertex].edges.keys())
                start += [
                    vertex for vertex in vertices_to_visit if vertex not in visited
                ]
        return False
