class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in x:
                return [min(i, x[diff]),max(i, x[diff])]
            else:
                x[nums[i]] = i
        return []