class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        r = ""
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

                if have == req:
                    if cl > len(s[l : ri + 1]):
                        r = s[l : ri + 1]
                        cl = len(s[l : ri + 1])

                if ch in freq:
                    freqq[ch] -= 1

                    if freq[ch] > freqq[ch]:
                        have -= 1
                l += 1
                

            ri += 1
        return r if cl > 0 else ""