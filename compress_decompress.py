def compress(string: str) -> str:
    res = [f"{c}{string.count(c)}" if string.count(c) > 1 else c for c in string]
    r = {s: s  for s in res}

    return "".join(r.values())




def decompress(string: str) -> str:
    res = []
    chrs = list(string)


    i = 0
    start = 0
    nums_indx = []
    end = 0
    while i < len(string):
        char = string[i]
        i += 1

        num = 0 
        while i < len(string) - 1 and chrs[i].isdigit():
            num = num * 10 + int(string[i])
            i += 1

        if num == 0:
            num = 1

        res.append(char * num)


    return "".join(res)





print(compress("aabbbc"))
print(compress("aaabbcccc"))
print(compress("abcd"))
print(compress("//"))

print(decompress("a2b3c"))
