import string 
from collections import deque 

def word_leader(begin_word, end_word, words):
    alphabet = string.ascii_lowercase


    if end_word not in words:
        return 0
    quee = deque([(begin_word, 1)])
    words = set(words)
    visited = set([begin_word]) 

    while quee:

        word, steps = quee.popleft()
        if word == end_word:
            return steps
        for i in range(len(word)):
            for c in alphabet:
                new_word = word[:i] + c + word[i + 1:]

                if new_word not in visited and new_word in words:
                    quee.append((new_word, steps + 1))
                    visited.add(new_word)



    return 0






print(word_leader(
    "yay",
    "dab",
    ["yay","day","dad","dab"]
))


