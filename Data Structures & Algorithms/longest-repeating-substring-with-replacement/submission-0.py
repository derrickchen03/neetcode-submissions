class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        c = {}
        m = 0
        lo = 0
        for r in range(len(s)):
            c[s[r]] = c.get(s[r], 0) + 1
            w = r - l + 1
            mc = max(c.values())
            while w - mc > k:
                c[s[l]] -= 1
                l += 1
                w = r - l + 1
            lo = max(lo, w)
        return lo


        
        