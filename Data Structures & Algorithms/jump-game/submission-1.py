class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2,-1,-1):
            print(nums[i])
            if goal - nums[i] <= i:
                goal = i
        return goal == 0
            
        