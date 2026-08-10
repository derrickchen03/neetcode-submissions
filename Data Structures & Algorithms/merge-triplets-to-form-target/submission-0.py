class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        i, j, k = target[0], target[1], target[2]
        r = [0, 0, 0]

        for v in triplets:
            a, b, c = v[0], v[1], v[2]
            if a <= i and b <= j and c <= k:
                r[0] = max(a, r[0])
                r[1] = max(b, r[1])
                r[2] = max(c, r[2])
        return r == target