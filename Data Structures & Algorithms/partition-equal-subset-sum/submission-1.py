class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        s = sum(nums)
        target = s / 2

        if s % 2 != 0:
            return False
        def rec(index, curSum):
            if curSum == target:
                return True
            if index >= len(nums) or curSum > target:
                return False
            if (index, curSum) in memo:
                return memo[(index, curSum)]

            take = rec(index + 1, curSum + nums[index])
            skip = rec(index + 1, curSum)

            memo[(index, curSum)] = take or skip

            return memo[(index, curSum)]
    
        return rec(0, 0)