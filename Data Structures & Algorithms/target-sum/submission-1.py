class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def rec(index, cs):
            if index >= len(nums):
                return 1 if cs == target else 0
            
            if (index, cs) in dp:
                return dp[(index, cs)]
            
            skip = rec(index + 1, cs - nums[index])
            take = rec(index + 1, cs + nums[index])
            
            dp[(index, cs)] = skip + take

            return dp[(index, cs)]

        return rec(0,0)