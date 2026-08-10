from functools import lru_cache
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            #ODD
            p1 = i
            p2 = i
            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                count += 1
                p1 -= 1
                p2 += 1

            #EVEN
            p1 = i
            p2 = i + 1
            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                count += 1
                p1 -= 1
                p2 += 1
        return count