class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        g = 0
        i = 0
        r = 0
        rs = 0
        while i < len(gas):
            diff = gas[i] - cost[i]
            i += 1
            rs += diff
            if rs < 0:
                rs = 0
                r = i
            
        return r
        