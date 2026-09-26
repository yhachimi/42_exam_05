class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """


        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        if len(prerequisites) <= 1:
            return  True

        for course, pre in  prerequisites:
            graph[pre].append(course)
            indegree[course] += 1 


        quue = [] 

        for course in range(numCourses):
            if indegree[course] == 0:
                quue.append(course)


        quue = sorted(quue)
        c = 0
        while quue:
            crs = quue.pop(0)
            c += 1 

            for next_crs in graph[crs]:
                indegree[next_crs] -= 1 
                if indegree[next_crs] <= 0:
                    quue.append(next_crs)

            quue.sort()

        return c == numCourses
                
