from collections import defaultdict, deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str: 
        adj = defaultdict(list)
        indegree = {char: 0 for word in words for char in word}
        res = []

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            ml = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:ml] == w2[:ml]:
                return ""
            
            for x in range(ml):
                if w1[x] != w2[x]:
                    if w2[x] not in adj[w1[x]]:
                        adj[w1[x]].append(w2[x])
                        indegree[w2[x]] += 1
                    break
            
        q = deque(char for char in indegree if indegree[char] == 0)

        while q:
            c = q.popleft()
            res.append(c)

            for ch in adj[c]:
                indegree[ch] -= 1
                if indegree[ch] == 0:
                    q.append(ch)
        if len(res) != len(indegree):
            return ""
            
        return "".join(res)