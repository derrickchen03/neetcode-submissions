class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        h = {}
        hand.sort()
        for i in hand:
            h[i] = h.get(i, 0) + 1
        
        while h:
            k = next(iter(h))
            for i in range(k, k + groupSize):
                if i in h:
                    val = h[i] - 1
                    if val == 0:
                        del h[i]
                    else:
                        h[i] = val
                else:
                    return False
        return not h