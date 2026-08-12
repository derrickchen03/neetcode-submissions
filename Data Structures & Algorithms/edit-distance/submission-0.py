from collections import defaultdict
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = defaultdict(int)

        def rec(i, j):
            if i == len(word1):
                return len(word2) - j
            elif j == len(word2):
                return len(word1) - i
            
            if (i, j) in dp:
                return dp[(i, j)]

            if word1[i] == word2[j]:
                dp[(i, j)] = rec(i + 1, j + 1)
            else:
                dp[(i, j)] = min(
                    1 + rec(i + 1, j),
                    1 + rec(i + 1, j + 1),
                    1 + rec(i, j + 1)
                )

            return dp[(i, j)]

        return rec(0, 0)
            