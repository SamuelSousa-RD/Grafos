from graph import Graph

def exemplo():
    g = Graph(directed=False)

    g.add_edge("A", "B", 1)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "D", 3)
    g.add_edge("C", "D", 4)

    print("--- Exibindo Grafo ---")
    g.show()

    print("\nRemovendo aresta B-D...")
    g.remove_edge("B", "D")
    g.show()

    print("\nRemovendo vértice C...")
    g.remove_vertex("C")
    g.show()

if __name__ == "__main__":
    exemplo()
