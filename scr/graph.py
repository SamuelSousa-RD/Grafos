class Graph:
    def __init__(self, directed=False):
        self.adj = {}
        self.directed = directed

    # Adiciona vértice
    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    # Adiciona aresta
    def add_edge(self, u, v, weight=1):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append((v, weight))

        if not self.directed:
            self.adj[v].append((u, weight))

    # Remove vértice
    def remove_vertex(self, v):
        if v in self.adj:
            del self.adj[v]
        for u in self.adj:
            self.adj[u] = [edge for edge in self.adj[u] if edge[0] != v]

    # Remove aresta
    def remove_edge(self, u, v):
        if u in self.adj:
            self.adj[u] = [edge for edge in self.adj[u] if edge[0] != v]
        if not self.directed and v in self.adj:
            self.adj[v] = [edge for edge in self.adj[v] if edge[0] != u]

    # Exibir o grafo
    def show(self):
        print("Grafo (Lista de Adjacência):")
        for v in self.adj:
            print(f"{v} -> {self.adj[v]}")
