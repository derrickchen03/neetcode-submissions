class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {node: [] for node in range(n + 1)}
        def adj():
            for node, neighbor, weight in times:
                graph[node].append((neighbor, weight))
        adj()
        dist = [float('inf') for node in range(n + 1)]
        dist[k] = 0
        

        p = [(0, k)]

        while p:
            curr_d, curr_n = heapq.heappop(p)

            if curr_d > dist[curr_n]:
                continue

            for neighbor, weight in graph[curr_n]:
                distance = curr_d + weight

                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(p, (distance, neighbor))
        if float('inf') in dist[1:]:
            return -1
        return max(dist[1:])
    
