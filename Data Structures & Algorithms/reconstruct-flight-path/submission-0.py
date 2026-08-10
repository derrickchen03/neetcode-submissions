class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        r = []
        for i1, i2 in tickets:
            if i2 not in adj:
                adj[i2] = []
            if i1 not in adj:
                adj[i1] = [i2]
            else:
                adj[i1].append(i2)
        for i in adj:
            adj[i].sort(reverse=True)
 
        def dfs(node):
            while adj[node]:
                destination = adj[node].pop()
                dfs(destination)
            r.append(node)
        
        dfs("JFK")
        return r[::-1]
        