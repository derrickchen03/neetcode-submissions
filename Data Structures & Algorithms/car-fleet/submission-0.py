class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        x = []
        s = []
        for i in range(len(position)):
            x.append((position[i], speed[i]))
        x.sort(reverse=True)
        
        for j in x:
            time = ((target - j[0]) / j[1])
            if s and s[-1] >= time:
                continue
            s.append(time)
        return len(s)
