class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = {(r, c): set() for r in range(3) for c in range(3)}
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                box = ((r // 3), (c // 3))
                val = board[r][c]
                if val == ".":
                    continue
                else:
                    val = int(val)

                if val in rows[r] or val in cols[c] or val in boxes[box]:
                        return False
                
                boxes[box].add(val)
                rows[r].add(val)
                cols[c].add(val)
                    
        return True
    
        