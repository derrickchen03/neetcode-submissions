from functools import lru_cache
class Solution:

    @lru_cache
    def longestPalindrome(self, s: str) -> str:
        p1 = 0
        p2 = 0
        rs = ""
        rl = 0
        for i in range(len(s)):
            p1 = i
            p2 = i

            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                if p2 - p1 + 1 > rl:
                    rl = p2 - p1 + 1
                    rs = s[p1:p2 + 1]

                p1 -= 1
                p2 += 1

            p1 = i
            p2 = i + 1

            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                if p2 - p1 + 1 > rl:
                    rl = p2 - p1 + 1
                    rs = s[p1:p2 + 1]

                p1 -= 1
                p2 += 1

        return rs