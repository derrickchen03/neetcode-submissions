class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robHelper(array):
            prev1, prev2 = 0, 0
            
            for n in array:
                curr = max(prev1, prev2 + n)
                prev2 = prev1
                prev1 = curr

            return prev1

        return max(robHelper(nums[:len(nums) - 1]), robHelper(nums[1: len(nums)]))