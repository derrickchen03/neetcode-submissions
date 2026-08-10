from collections import defaultdict

class Node:
    def __init__(self):
        self.child = defaultdict(Node)
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        curr = self.root
        for char in word:
            curr = curr.child[char]
        curr.isEnd = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        t = Trie()
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for word in wordDict:
            t.insert(word)
        
        for i in range(len(s)):
            curr = t.root
            if dp[i] == True:
                for j in range(i, len(s)):
                    if s[j] not in curr.child:
                        break
                    curr = curr.child[s[j]]
                    if curr.isEnd:
                        dp[j + 1] = True
        return dp[len(s)]
