
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty= self.find(y)

        if rootx != rooty:
            if self.size[rootx] < self.size[rooty]:
                self.parent[rootx] = rooty
                self.size[rooty] += self.size[rootx]

            else:
                self.parent[rooty] = rootx
                self.size[rootx] += self.size[rooty]
            return True
        return False

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = n

        uf = UnionFind(n)

        for node1, node2 in edges:
            if uf.union(node1, node2):
                res -= 1
        
        return res
        