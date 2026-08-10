class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r = []
        def bt(index, subset):
            if index == len(nums):
                r.append(list(subset))
                return

            subset.append(nums[index])
            bt(index + 1, subset)

            subset.pop()
            bt(index + 1, subset)

        bt(0, [])

        return r