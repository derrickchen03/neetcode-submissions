class Solution:
    def checkValidString(self, s: str) -> bool:
        st = []
        sta = []

        for i in range(len(s)):
            if s[i] == "(":
                st.append(("(",i))
            elif s[i] == "*":
                sta.append(("*", i))
            else:
                if st:
                    st.pop()
                elif sta:
                    sta.pop()
                else:
                    return False

        while st and sta:
            a = st.pop()
            b = sta.pop()

            if a[1] > b[1]:
                return False
        
        if len(st) > len(sta):
            return False
        
        return True
