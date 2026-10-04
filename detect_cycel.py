def findOrder(numCourses, prerequisites):




    indegree  = [0]  * numCourses

    if not prerequisites and numCourses > 0:
        return [i for i in range(numCourses)]

    new_pkg = {i: [] for i in range(numCourses)}
    for curse, pre in prerequisites:
            new_pkg[pre].append(curse)
            indegree[curse] += 1

    quue = []

    for i in  range(numCourses):
        if indegree[i] == 0:
            quue.append(i)


    res = []
    quue.sort()
    while quue:
        pkg = quue.pop()


        for dep in new_pkg[pkg]:
            indegree[dep] -= 1 

            if indegree[dep] == 0:
                quue.append(dep)
        quue.sort()
        res.append(pkg)


    if len(res) != numCourses:
        return []
    return res



print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
            

