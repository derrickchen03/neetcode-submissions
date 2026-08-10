class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        see = False
        while not see:
            rs = 0
            s = str(n)
            for x in s:
                rs += int(x) ** 2
            if rs in seen:
                break
            if rs == 1:
                see = True
            n = rs
            seen.append(rs)
        return see
                