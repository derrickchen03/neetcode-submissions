from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        count = 0
        @cache
        def rec(index, prev_index):
            if index >= len(nums):
                return 0

            skip = rec(index + 1, prev_index)
            
            take = 0
            if prev_index == -1 or nums[index] > nums[prev_index]:
                take = 1 + rec(index + 1, index)

            return max(skip, take)

        return rec(0, -1)