class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rs = -1001
        curr_best = -1001
        for i in nums:
            rs += i
            if rs < i:
                rs = i
            if rs > curr_best:
                curr_best = rs
        return curr_best

