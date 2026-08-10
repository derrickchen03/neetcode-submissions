import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        
        while l < r:
            s = (l + r) // 2
            t = 0
            for p in piles:
                t += math.ceil(p / s)
            if t <= h:
                r = s 
            elif t > h:
                l = s + 1
        return l