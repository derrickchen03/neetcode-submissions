class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        r = []
        
        print(nums)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            k = len(nums) - 1
            j = i + 1
            
            while j < k:
                s = nums[i] + nums[k] + nums[j]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    r.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return r
