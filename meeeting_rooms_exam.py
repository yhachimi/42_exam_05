def meet_exam(met: list):


    srts = [st for st,end in met]
    ends = [end for st, end in met]
    res = {}
    count = 0 


    
    res["ass_count"] = 0
    res["ass_mets"] = {}



    visited = []
    counts = {f"{m}": met.count(m) for m in met}


    for i in range(len(met)):
        lst = []

        if i in visited:
            continue
        lst.append(met[i])
        for j in range(i+1, len(met)):

            if srts[j] >= ends[i] and j not in visited:
                check = [srts[j] >= met[s][1] for s in range(len(lst))]

                if not all(check):
                    continue 

                lst.append(met[j])

                visited.append(j)


        if counts[f"{met[i]}"] >= 1:
            lst.sort()
            res["ass_mets"][count] = lst
            count += 1
            visited.append(i)
            counts[f"{met[i]}"] -= 1



    

    res["ass_count"] = count
    return  res





print(meet_exam([[1,4], [5, 6], [1,4]]))

print(meet_exam([[1, 5], [1, 6], [5, 3], [5, 10], [5, 10]]))




