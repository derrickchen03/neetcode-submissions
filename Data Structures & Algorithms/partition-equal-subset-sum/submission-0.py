from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        target = s / 2

        if s % 2 != 0:
            return False
        @cache
        def rec(index, curSum):
            if curSum == target:
                return True
            if index >= len(nums) or curSum > target:
                return False

            take = rec(index + 1, curSum + nums[index])
            skip = rec(index + 1, curSum)

            return take or skip
    
        return rec(0, 0)