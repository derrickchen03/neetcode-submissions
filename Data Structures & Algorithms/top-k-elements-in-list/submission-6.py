class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        b = [[] for _ in range(len(nums) + 1)]
        d = {}
        r = []
        count = 0
        for i in nums:
            d[i] = d.get(i, 0) + 1
        for i in d:
            b[d[i]].append(i)
        print(b)
        for j in b[len(b):0:-1]:
            if count == k:
                break
            if j:
                r += j
                count += len(j)
        return r