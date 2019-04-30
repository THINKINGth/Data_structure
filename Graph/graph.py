class GraphException(Exception):
    pass


class Graph:
    """
    function : Graph(mat, type)
    mat: two-dimensional matrix
    type: 1 > undirected graph 0 > directed graph
    """
    def __init__(self, mat, type=1):
        self._vnum = len(mat)
        self._mat = []
        self._type = type
        for i in range(self._vnum):
            if len(mat) != self._vnum:
                raise GraphException
        if type == 0:
            for i in range(self._vnum):
                for j in range(self._vnum):
                    if mat[i][j] != mat[j][i]:
                        raise GraphException
        for i in range(self._vnum):
            self._mat.append(mat[i][:])

    # output graph
    def prints(self):
        for i in range(self._vnum):
            for j in range(self._vnum):
                print(self._mat[i][j], end=' ')
            print()

    # output number of edges
    def vertex_vnum(self):
        return self._vnum

    # Check that the vertex range is legal
    def _invalid(self, v):
        return (v < 0) and (v >= self._vnum)

    # add new vertex
    def add_vertex(self, row, line=None):
        # this is undirected graph
        if not self._type:
            if len(row) != self._vnum + 1:
                raise GraphException
            for i in range(self._vnum):
                self._mat[i].append(row[i])
        else:
            if len(row) != self._vnum + 1 and len(line) >= self._vnum:
                raise GraphException
            for i in range(self._vnum):
                self._mat[i].append(line[i])
        self._vnum += 1
        self._mat.append(row)

    def get_edge(self, vi, vj):
        if self._invalid(vi) and self._invalid(vj):
            raise GraphException
        return self._mat[vi][vj]

    def add_edges(self, vi, vj):
        if self._invalid(vi) and self._invalid(vj):
            raise GraphException
        self._mat[vi][vj] = 1

    def sub_edges(self, vi, vj):
        if self._invalid(vi) and self._invalid(vj):
            raise GraphException
        self._mat[vi][vj] = 0

    def __str__(self):
        print("This is a python implementation of the graph structure.\n" +
              "Graph(mat, type) \nmat: two-dimensional matrix \ntype: 1 > undirected graph 0 > directed graph"
              )
