class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(string):
            l, r = 0, len(string) - 1
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        r = []
        def bt(i, curr):
            if i >= len(s):
                r.append(list(curr))
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s[i: j + 1]):
                    curr.append(s[i: j + 1])
                    bt(j + 1, curr)
                    curr.pop()


        bt(0, [])
        return r