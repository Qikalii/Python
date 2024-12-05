class GraphAdjMat:
    """基于邻接矩阵实现的无向图类"""

    def __init__(self, vertices: list[int], edges: list[list[int]]):
        """构造方法"""
        self.vertices = []  # 顶点列表
        self.adj_mat = []  # 邻接矩阵

        # 添加顶点
        for val in vertices:
            self.add_vertex(val)

        # 添加边
        for e in edges:
            self.add_edge(e[0], e[1])

    def size(self) -> int:
        """获取顶点数量"""
        return len(self.vertices)

    def add_vertex(self, val: int):
        """添加顶点"""
        # 添加新顶点
        self.vertices.append(val)

        # 向邻接矩阵添加新行和新列
        for row in self.adj_mat:
            row.append(0)
        self.adj_mat.append([0] * len(self.vertices))

    def remove_vertex(self, index: int):
        """删除顶点"""
        if index < 0 or index >= self.size():
            raise IndexError("索引超出范围")

        # 删除顶点
        self.vertices.pop(index)

        # 删除对应的邻接矩阵行和列
        self.adj_mat.pop(index)
        for row in self.adj_mat:
            row.pop(index)

    def add_edge(self, i: int, j: int):
        """添加边"""
        # 参数 i, j 对应 vertices 元素索引
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError("索引无效或自环")

        # 无向图，设置邻接矩阵对称
        self.adj_mat[i][j] = 1
        self.adj_mat[j][i] = 1

    def remove_edge(self, i: int, j: int):
        """删除边"""
        # 参数 i, j 对应 vertices 元素索引
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError("索引无效或自环")

        self.adj_mat[i][j] = 0
        self.adj_mat[j][i] = 0

    def print(self):
        """打印邻接矩阵"""
        print("顶点列表 =", self.vertices)
        print("邻接矩阵 =")
        for row in self.adj_mat:
            print(row)
