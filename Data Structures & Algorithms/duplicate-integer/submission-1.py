class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = []
        for i in nums:
            if i in store:
                return True
            else:
                store.append(i)
        return False
