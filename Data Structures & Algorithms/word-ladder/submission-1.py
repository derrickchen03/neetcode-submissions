from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set(beginWord)
        h = {}
        q = deque()
        c = 1

        for word in wordList + [beginWord]:
            for i in range(len(word)):
                x = word[:i] + "*" + word[i + 1:]
                if x not in h:
                    h[x] = [word]
                    continue
                h[x].append(word)

        q.append((beginWord, 1))

        while q:
            word, length = q.popleft()
            
            if word == endWord:
                return length
            
            for i in range(len(word)):
                p = x = word[:i] + "*" + word[i + 1:]

                for ne in h[p]:
                    if ne not in visited:
                        visited.add(ne)
                        q.append((ne, length + 1))

                h[p] = []
        return 0