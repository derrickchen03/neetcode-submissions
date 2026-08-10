class Solution:
    def trap(self, height: List[int]) -> int:
        x = [0 for _ in range(len(height))]
        y = x.copy()
        res = x.copy()

        for front in range(len(height)):
            back = len(height) - 1 - front
            if front == 0:
                x[front] = height[front]
                y[back] = height[back]
                continue
            x[front] = max(height[front], x[front - 1])
            y[back] = max(height[back], y[back + 1])

        for i in range(len(height)):
            res[i] = min(x[i], y[i]) - height[i]
        print(x, y)
        return sum(res)