class Solution:
    def search(self, nums: List[int], target: int) -> int:
        front = 0
        back = len(nums) - 1
        while front <= back:
            curr = ((front + back) // 2)
            if nums[curr] == target:
                return curr
            elif nums[curr] < target:
                front = curr + 1
            else:
                back = curr - 1
        return -1 