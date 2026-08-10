from functools import lru_cache
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        rs = ""
        for i in range(len(s)):
            #ODD
            p1 = i
            p2 = i
            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                curr = p2 - p1 + 1
                if curr > max_len:
                    max_len = curr
                    rs = s[p1:p2 + 1]
                p1 -= 1
                p2 += 1

            #EVEN
            p1 = i
            p2 = i + 1
            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                curr = p2 - p1 + 1
                if curr > max_len:
                    max_len = curr
                    rs = s[p1:p2 + 1]
                p1 -= 1
                p2 += 1
        return rs
        