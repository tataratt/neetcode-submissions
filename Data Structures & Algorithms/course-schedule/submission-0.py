class Solution:
    from collections import defaultdict
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)

        for d, c in prerequisites:
            preMap[d].append(c)

        visit = set()


        def dfs(d):
            if d in visit:
                return False
            
            if not preMap[d]:
                return True
            visit.add(d)

            for c in preMap[d]:
                if not dfs(c):
                    return False
            visit.remove(d)

            preMap[d] = []
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True

