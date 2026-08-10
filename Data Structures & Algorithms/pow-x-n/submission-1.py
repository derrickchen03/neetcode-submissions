class Solution:
    def myPow(self, x: float, n: int) -> float:
        d = x
        for i in range(abs(n - 1)):
            if n > 0:
                x = x * d
            else:
                x = x * (1/d)
        return x