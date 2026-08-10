class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        p = []
        s = set(nums)
        cm = 0
        for i in nums:
            if (i - 1) not in s:
                p.append(i)
        for n in p:
            counter = 1
            while n + counter in s:
                counter += 1
            if counter > cm:
                cm = counter
        return cm