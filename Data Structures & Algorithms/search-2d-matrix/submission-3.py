class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        p1 = 0
        p2 = len(matrix) - 1
        s = 0
        while p1 <= p2:
            dd = (p1 + p2) // 2
            print(dd)
            if matrix[dd][0] <= target:
                p1 = dd + 1
            else:
                p2 = dd - 1
        dd = (p1 + p2) // 2
        return target in matrix[dd]
