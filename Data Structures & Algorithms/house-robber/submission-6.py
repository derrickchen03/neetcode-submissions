class Solution:
    def rob(self, nums: List[int]) -> int:
        s = [0] * len(nums)
        s[0] = nums[0]
        if len(nums) > 1:
            s[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            s[i] = max(nums[i] + s[i - 2], s[i - 1])
            print(s[i], nums[i] + s[i - 2], s[i - 1])
        
        return(max(s))