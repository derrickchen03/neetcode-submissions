class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        h = set()
        prereq = {course: [] for course in range(numCourses)}

        for course, pre in prerequisites:
            prereq[course].append(pre)
        
        def dfs(pr):
            if pr in h:
                return False
            
            h.add(pr)

            for i in prereq[pr]:
                if not dfs(i):
                    return False
            h.remove(pr)
            return True
        
        for i in prereq:
            if not dfs(i):
                return False
        return True