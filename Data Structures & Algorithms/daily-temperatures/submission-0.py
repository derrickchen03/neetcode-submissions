class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        r = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):
            while s and temperatures[s[-1]] < temperatures[i]:
                a = s.pop()
                r[a] = i - a
            s.append(i)
        return r

            