class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] != "O":
                return
            if board[x][y] == "O":
                board[x][y] = "#"

            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if ((x == 0 or y == 0) or (x == len(board) - 1 or y == len(board[0]) - 1)) and board[x][y] == "O":
                    dfs(x, y)
                    
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == "#":
                    board[x][y] = "O"
                else:
                    board[x][y] = "X"