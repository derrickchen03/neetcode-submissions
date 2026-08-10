class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [0] * numCourses
        h = {node: [] for node in range(numCourses)}
        s = []

        for n, ne in prerequisites:
            h[n].append(ne)

        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True
            
            visited[node] = 1

            
            for i in h[node]:
                if not dfs(i):
                    return False

            visited[node] = 2
            s.append(node)
            return True

        for node in h:
            if not dfs(node):
                return []
        
        return s