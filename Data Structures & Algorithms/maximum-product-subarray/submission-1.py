class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_min = nums[0]
        curr_max = nums[0]
        for i in nums[1:]:
            curr_min, curr_max = min(i, curr_max * i, curr_min * i), max(i, curr_max * i, curr_min * i)
            res = max(res, curr_max, curr_min)
            
        return res