class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        def rec(n) -> int:
            s = [0] * len(n)
            if not n:
                return [0]
            s[0] = n[0]
            if len(n) > 1:
                s[1] = max(n[0], n[1])

            for i in range(2, len(n)):
                s[i] = max(n[i] + s[i - 2], s[i - 1])
            return s
        
        x = nums[:len(nums) - 1]
        y = nums[1:len(nums)]
        return max(max(rec(x)), max(rec(y)))