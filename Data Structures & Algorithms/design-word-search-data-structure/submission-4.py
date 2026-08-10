class Trie:
    
    def __init__(self):
        self.value = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.value = Trie()

    def addWord(self, word: str) -> None:
        curr = self.value
        for ch in word:
            if ch in curr.value:
                curr = curr.value[ch]
            else:
                curr.value[ch] = Trie()
                curr = curr.value[ch]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        return self.recSearch(self.value, word)

    def recSearch(self, t, word):
            curr = t
            for i in range(len(word)):
                if i == len(word) - 1 and word[i] == ".":
                    for ch in curr.value:
                        if curr.value[ch].isEnd:
                            return True
                    return False
                elif word[i] == ".":
                    for ch in curr.value:
                        if self.recSearch(curr.value[ch], word[i + 1:]):
                            return True
                    return False
                if word[i] != ".":
                    if word[i] in curr.value:
                        curr = curr.value[word[i]]
                    else:
                        return False
            return curr.isEnd