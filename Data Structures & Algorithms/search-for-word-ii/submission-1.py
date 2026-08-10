class TreeNode:

    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str):
        curr = self.root
        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
                continue
            curr.children[ch] = TreeNode()
            curr = curr.children[ch]
        curr.isEnd = True
        curr.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie()
        r = []

        for word in words:
            t.insert(word)

        def bt(row, col, node):
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == "#":
                return
            char = board[row][col]

            if char not in node.children:
                return
            
            nxt = node.children[char]

            if nxt.word is not None:
                r.append(nxt.word)
                nxt.word = None
            
            board[row][col] = "#"

            bt(row + 1, col, nxt)
            bt(row - 1, col, nxt)
            bt(row, col + 1, nxt)
            bt(row, col - 1, nxt)

            board[row][col] = char

        for i in range(len(board)):
            for j in range(len(board[0])):
                bt(i, j, t.root)
        return r