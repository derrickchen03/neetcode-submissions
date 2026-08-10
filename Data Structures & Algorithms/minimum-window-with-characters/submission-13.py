class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""
        g_r = 0
        g_l = 0
        cl = float('inf')
        
        freq = {char: 0 for char in t}
        freqq = {char: 0 for char in t}
        req = len(freq)
        have = 0

        for char in t:
            freq[char] += 1

        l = 0
        ri = 0

        while ri < len(s):
            c = s[ri]
            if c in freq:
                freqq[c] += 1

                if freqq[c] == freq[c]:
                    have += 1
                
            while have == req:
                ch = s[l]
                curr = ri - l + 1

                if curr < cl:
                    g_l = l
                    g_r = ri
                    cl = curr

                if ch in freq:
                    freqq[ch] -= 1

                    if freq[ch] > freqq[ch]:
                        have -= 1
                l += 1
                

            ri += 1
        return s[g_l : g_r + 1] if cl != float('inf') else ""