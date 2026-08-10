import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        x = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv,}
        s = []
        for i in tokens:
            if i not in x:
                s.append(i)
            else:
                b = int(s.pop())
                a = int(s.pop())
                s.append(x[i](a, b))
        return int(s.pop())
        