import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {}
        for i in range(len(points)):
            graph[i] = []
        def buildGraph():
            for i in range(len(points)):
                x1, y1 = points[i]

                for j in range(i + 1, len(points)):
                    x2, y2 = points[j]

                    distance = abs(x1 - x2) + abs(y1 - y2)

                    graph[i].append((distance, j))
                    graph[j].append((distance, i))
        buildGraph()

        def prims(start_node):
            visited = set()
            edges = []

            h = [(0, start_node, None)]

            while h:
                weight, curr, parent = heapq.heappop(h)

                if curr in visited:
                    continue
                
                visited.add(curr)
                if parent is not None:
                    edges.append((weight, parent, curr))
                
                for distance, neighbor in graph[curr]:
                    if neighbor not in visited:
                        heapq.heappush(h, (distance, neighbor, curr))

            return sum(weight for weight, _, _ in edges)
        return prims(0)