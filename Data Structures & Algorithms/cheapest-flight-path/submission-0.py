class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = {node: [] for node in range(n)}
        prices = [float('inf')] * (n)
        prices[src] = 0

        for _ in range(k + 1):
            n = prices.copy()
            for node, neighbor, weight in flights:
                if prices[node] != float('inf') and n[node] + weight < n[neighbor]:
                    n[neighbor] = prices[node] + weight
            prices = n
        r = n[dst] if n[dst] != float('inf') else -1
        return r