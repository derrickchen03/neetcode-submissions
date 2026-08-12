from collections import defaultdict
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3:
            return True

        if len(s1) + len(s2) != len(s3):
            return False

        dp = defaultdict(bool)

        def rec(i, j):
            if i + j == len(s3):
                return True
            
            result = False

            if (i, j) in dp:
                return dp[(i, j)]
            
            if i < len(s1) and s1[i] == s3[i + j]:
                dp[(i, j)] = dp[(i,j)] or rec(i + 1, j)
            if j < len(s2) and s2[j] == s3[i + j]:
                dp[(i, j)] = dp[(i,j)] or rec(i, j + 1)

            return dp[(i, j)]
    
        return rec(0,0)