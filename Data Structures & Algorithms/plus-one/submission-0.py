class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = False
        for i in range(len(digits) - 1,-1,-1):
            if i == len(digits) - 1:
                val = digits[i] + 1
                c = True if val >= 10 else False
            else:
                if c:
                    val = digits[i] + 1
                    c = True if val >= 10 else False
                else:
                    val = digits[i]
            digits[i] = val % 10
        if c:
            digits = [1] + digits
        return digits