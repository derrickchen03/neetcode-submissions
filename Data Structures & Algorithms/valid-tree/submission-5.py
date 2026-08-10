class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        v = set()
        e = {node: [] for node in range(n)}

        for node, edge in edges:
            e[node].append(edge)
            e[edge].append(node)

        def dfs(node, parent):
            if node in v:
                return False

            v.add(node)

            for i in e[node]:
                if parent == i:
                    continue
                if not dfs(i, node):
                    return False

            return True

        if not dfs(0, -1):
            return False
        print(v)
        return len(v) == n