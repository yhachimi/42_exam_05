class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """ 
        res = []
        if numCourses >= 1 and len(prerequisites) == 0:
            return [i for i  in range(numCourses)]



        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        for curse, pre in prerequisites:
            graph[pre].append(curse)
            indegree[curse] += 1 

        heap = sorted([curse for curse in range(numCourses) if indegree[curse] == 0])


        while heap:
            c = heap.pop()
            res.append(c)
            for next_curse in graph[c]:
                indegree[next_curse] -= 1 
                if indegree[next_curse] == 0:
                    heap.append(next_curse)

            heap.sort()
        if len(res) !=  numCourses:
            return []     
        return res

