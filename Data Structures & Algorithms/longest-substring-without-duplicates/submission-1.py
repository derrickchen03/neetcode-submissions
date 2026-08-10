class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = set()
        p1 = 0
        p2 = 0
        c_max = 0
        while p2 < len(s):
            
            if s[p2] in x:
                if p2 - p1 > c_max:
                    c_max = p2 - p1
                               
                x.discard(s[p1])
                p1 += 1
            else:
                x.add(s[p2])
                p2 += 1
        if p2 - p1 > c_max:
             c_max = p2 - p1
        return c_max
