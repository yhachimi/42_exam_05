class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """ 
        res = []
        if numCourses >= 1 and not prerequisites:
           return [i for i in range(numCourses)]

        graph = {}

        for i, j in prerequisites:
            if i in graph and j not in graph[i]:
                graph[i].append(j)

            else:
                graph[i] = [j]


        new_graph = {}
        indegree = {pkg: 0 for pkg in range(numCourses)}
        for pkg, deps in graph.items():
            for dep in deps: 
                if pkg == dep:
                    return []
                if dep not in new_graph:
                    new_graph[dep] = []
                if dep in new_graph and pkg not in new_graph[dep]:
                        new_graph[dep].append(pkg)
                        indegree[pkg]+= 1

        heap = sorted([pkg for pkg in indegree if indegree[pkg] == 0])

        while heap:
            pkg = heap.pop(0)
            res.append(pkg)
            if not new_graph.get(pkg):
                continue
            for dep in sorted(new_graph[pkg]):
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    heap.append(dep)

            heap.sort()

        if len(res) != numCourses:
            return []
        return res


