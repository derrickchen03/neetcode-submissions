class Solution:
    def isValid(self, s: str) -> bool:
        sd = []
        valid = {"{":"}","(":")","[":"]"}
        for char in s:
            if char in valid:
                sd.append(char)
            else:
                if not sd:
                    return False
                store = sd.pop()
                if valid[store] != char:
                    return False
        return not sd