class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        p1 = 0
        p2 = len(s1) - 1
        r = "".join(sorted(s1))
        while p2 < len(s2):
            s = "".join(sorted(s2[p1:p2 + 1]))
            if r == s:
                return True
            p1 += 1
            p2 += 1
        return False