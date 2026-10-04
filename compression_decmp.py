def compress(word: str) -> str:
    res = {c: f"{c}{word.count(c)}"  if  word.count(c) > 1 else c for c in word}

    return "".join([c for c in res.values()])




def decompress(word) -> str:


    i = 0 

    num = 0 
    res = ""
    for c in word:
        if c.isdigit():
            num = num * 10 + ord(c) - 48

        if not c.isdigit():
            if num > 0:
                res += c * num
            if num == 0:
                res += c
            num = 0 


    return res

print(compress("abcdaabc"))
print(decompress("a3b3c"))
print(decompress("a3b2c2d"))

