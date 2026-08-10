class Solution:

    def encode(self, strs: List[str]) -> str:
        x = ""
        for i in strs:
            x += str(len(i)) + "#" + i
        return x

    def decode(self, s: str) -> List[str]:
        r = []
        i = 0
        while i < len(s):
            j = i
            if s[i] == 0:
                return []
            else:
                while s[j] != "#":
                    j += 1
                x = int(s[i:j])
                r.append(s[j + 1: j + 1 + x])
                i = j + 1 + x
        return r