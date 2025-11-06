class UDGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, start_vertex, end_vertex):
        if start_vertex in self.graph and end_vertex in self.graph:
            self.graph[start_vertex].append(end_vertex)
        else:
            print("One or both vertices not found.")

    def get_following_list(self, vertex):
        return self.graph.get(vertex, [])

    def get_followers_list(self, vertex_to_find):
        followers = []
        for vertex, following_list in self.graph.items():
            if vertex_to_find in following_list:
                followers.append(vertex)
        return followers