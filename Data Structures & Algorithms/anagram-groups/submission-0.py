class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = 0
        h = {}
        res = []
        for i in strs:
            x = "".join(sorted(i))
            if x not in h:
                h[x] = count
                res.append([i])
                count += 1
            else:
                res[h[x]].append(i)
        return res