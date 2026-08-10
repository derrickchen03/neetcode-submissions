class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        c_max = 0
        while p1 < p2:
            h = (p2 - p1) * min(heights[p1], heights[p2])
            if c_max < h:
                c_max = h
            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        return c_max