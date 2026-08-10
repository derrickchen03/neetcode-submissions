class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        r = []
        def bt(index, subset, curr_sum):
            if curr_sum == target:
                r.append(list(subset))
                return
            
            if index == len(nums) or curr_sum > target:
                return

            

            subset.append(nums[index])
            bt(index, subset, curr_sum + nums[index])

            subset.pop()
            bt(index + 1, subset, curr_sum)
        bt(0, [], 0)
        return r