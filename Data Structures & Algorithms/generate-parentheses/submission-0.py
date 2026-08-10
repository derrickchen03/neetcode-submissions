class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def bt(string, opened, closed):
            if len(string) == 2 * n:
                r.append("".join(string))

            if opened < closed:
                return
            
            if opened < n:
                string.append("(")
                bt(string,opened + 1, closed)
                string.pop()
            
            if closed < n:
                string.append(")")
                bt(string, opened, closed + 1)
                string.pop()
        r = []
        bt([], 0, 0)
        return r