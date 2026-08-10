class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        r = []

        def bt(visited):
            if len(visited) == len(nums):
                r.append(list(visited))
                return

            for n in nums:
                if n in visited:
                    continue
                visited.append(n)
                bt(visited)
                visited.pop()
        
        bt([])
        return r
                
