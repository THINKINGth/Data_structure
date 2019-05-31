from random import randrange
from Lstack import Lstack


class GraphException(Exception):
    # print("Error")
    pass


class Graph:
    # conf = 0; 带权图
    def __init__(self, mat, conf=0):
        self._vnum = len(mat)
        for x in range(self._vnum):
            if self._vnum != len(mat[x][:]):
                raise GraphException
        for i in range(self._vnum):
            self._mat = mat
        self._conf = conf

    # 返回图的顶点个数
    def vertex_num(self):
        return self._vnum

    # 打印图的邻接矩阵
    def prints(self):
        for i in range(self._vnum):
            for j in range(self._vnum):
                print(self._mat[i][j], end=' ')
            print()

    # 增加图的边的权值
    def add_edge(self, vi, vj):
        if self._invalid(vi) and self._invalid(vj):
            raise GraphTest
        else:
            self._mat[vi][vj] += 1
        return

    # 判断查询的顶点是否超出范围
    def _invalid(self, vi):
        return vi < 0 or vi > self._vnum

    # 查询图的边的权值
    def get_edge(self, vi, vj):
        if self._invalid(vi, vj):
            raise GraphException
        return self._mat[vi][vj]

    # 增加图的顶点数
    def add_vertex(self, vx, vy):
        if self._vnum == len(vx) - 1 and self._vnum == len(vy) - 1 and vx[-1] == vy[-1]:
            self._mat.append(vx[:-1])
            self._vnum += 1
            for i in range(self._vnum):
                self._mat[i].append(vy[i])
        else:
            raise GraphException

    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphException
        return self._mat[vi]

    # 输出一个的各条出边和权值
    @staticmethod
    def _out_edges(row, conf=0):
        edges =[]
        for i in range(len(row)):
            if row[i] != 0:
                edges.append((i, row[i]))
        return edges

    def depth_first(self, vi, path, visit):
        # 当前节点已经被访问
        visit[vi] = 1
        # 输出当前节点的目标节点和边的权值
        row = self.out_edges(vi)
        out_edge = Graph._out_edges(row, 0)
        for aim_edge in out_edge:
            if visit[aim_edge[0]] != 1:
                path.append((vi, aim_edge[0]))
                self.depth_first(aim_edge[0], path, visit)
            else:
                ins = 0
                for vs in visit:
                    if vs == 1:
                        ins += 1
                if ins == self._vnum:
                   print(path)

    # 堆栈实现深度优先搜索
    def depth_first_search(self, v):
        vnum = self.vertex_num()
        row = self.out_edges(v)
        edges = ()
        visited = [0] * vnum
        st = Lstack.Lstack()
        visited[v] = 1
        st.push((0, (v, self._out_edges(row))))
        while not st.is_empty():
            i, vedges = st.pop()
            vi, edges = vedges
            if i < len(edges):
                vj, w = edges[i]
                st.push(((i + 1), (vi, edges)))
                if visited[vj] == 0:
                    visited[vj] = 1
                    print((vi, vj), end=' ')
                    row = self.out_edges(vj)
                    st.push((0, (vj, self._out_edges(row))))


class GraphTest:
    def __init__(self):
        pass

    @staticmethod
    def graph_test():
        m = 4
        mat = [[randrange(0, 5) for i in range(m)] for j in range(m)]
        for i in range(len(mat)):
            for j in range(len(mat)):
                print(mat[i][j], end=' ')
            print()
        graph = Graph(mat)
        print()
        graph.prints()
        # 自定义，其中最后一个元素必须相同
        # vx = [1, 1, 1, 1, 0]
        # vy = [0, 1, 1, 1, 0]
        # 随机
        vx = [randrange(0, 5) for i in range(m + 1)]
        vy = [randrange(0, 5) for i in range(m + 1)]
        vx[m] = vy[m]
        graph.add_vertex(vx, vy)
        graph.prints()
        print()
        '''
        graph.prints()
        row, conf = graph.out_edges(3)
        test_out_edges = Graph._out_edges(row, conf)
        for i in test_out_edges:
            print(i)
        '''

        test = [
            [0, 1, 1, 0],[1, 0, 1, 0],[1, 1, 0, 1],[0, 0, 1, 0]
        ]
        for i in test:
            for j in i:
                print(j, end=' ')
            print()
        graph = Graph(test)
        print(Graph._out_edges(graph.out_edges(2)))
        visit = [0 for i in range(graph._vnum)]
        vi = 2
        graph.depth_first(vi, [], visit)
        graph.depth_first_search(vi)

if __name__ == "__main__":
    test = GraphTest()
    test.graph_test()

