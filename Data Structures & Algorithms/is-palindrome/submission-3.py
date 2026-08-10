class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        front = 0
        back = len(s) - 1
        while front < back:
            print(s[front])
            if s[front].lower() != s[back].lower():
                print(s[front], s[back])
                return False
            front += 1
            back -= 1
        return True