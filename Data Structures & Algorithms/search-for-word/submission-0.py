class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def bt(x, y, curr):
            if (x, y) in visited or x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[curr]:
                return False

            if curr == len(word) - 1:
                return True

            visited.add((x, y))
            found = ( bt(x + 1, y, curr + 1) or bt(x - 1, y, curr + 1) or bt(x, y + 1, curr + 1) or bt(x, y - 1, curr + 1) )

            visited.remove((x, y))
            return found

        for x in range(len(board)):
            for y in range(len(board[0])):
                if bt(x, y, 0):
                    return True

        return False