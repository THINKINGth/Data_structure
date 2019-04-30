import random
import graph
if __name__ == "__main__":
    num = 5
    # Graph
    print("Graph")
    mat = [[random.randrange(0, 2) for j in range(num)] for i in range(num)]
    graph_test = graph.Graph(mat)
    graph_test.prints()

    # add_vertex
    print("Func: add_vertex")
    row = [random.randrange(0, 2) for j in range(num + 1)]
    print(row)
    line = [random.randrange(0, 2) for j in range(num + 1)]
    print(line)
    graph_test.add_vertex(row, line)

    # prints
    print("Func: prints")
    graph_test.prints()

    # get_edge
    print("Func: get_edge")
    print(graph_test.get_edge(3, 3))

    # vertex_vnum
    print("Func: vertex_vnum")
    print(graph_test.vertex_vnum())

    # add_edge
    print("Func: add_edge")
    print("now: " + str(graph_test.get_edge(3, 0)))
    graph_test.add_edges(3, 0)
    print("add edge: " + str(graph_test.get_edge(3, 0)))
    graph_test.sub_edges(3, 0)
    print("sub edge: " + str(graph_test.get_edge(3, 0)))