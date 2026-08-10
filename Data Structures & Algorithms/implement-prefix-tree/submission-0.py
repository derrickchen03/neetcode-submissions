class TreeNode:

    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        
    def insert(self, word: str) -> None:
        curr_node = self.root
        for ch in word:
            if ch in curr_node.children:
                curr_node = curr_node.children[ch]
            else:
                curr_node.children[ch] = TreeNode()
                curr_node = curr_node.children[ch]
        curr_node.isEnd = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        for ch in word:
            if ch in curr_node.children:
                curr_node = curr_node.children[ch]
            else:
                return False
        return curr_node.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for ch in prefix:
            if ch in curr_node.children:
                curr_node = curr_node.children[ch]
            else:
                return False
        return True
        