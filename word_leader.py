from collections import deque
import  string 

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word_set = set(wordList)

        if endWord not in  word_set:
            return 0 

        heap = deque([(beginWord, 1)])
        visited = set([beginWord])
        alpahebts = string.ascii_lowercase 

        while heap:
            word, steps = heap.popleft()
            if word == endWord:
                return steps 

            for i in range(len(word)):
                for c in alpahebts:
                    new_word = word[:i] + c + word[i + 1:]

                    if new_word in word_set and new_word not in visited:
                        heap.append((new_word, steps + 1))
                        visited.add(new_word)


        return 0



        
        



        



s = Solution()


d = ["hot","dot","dog","lot","log","cog"]


print(s.ladderLength("hot", "dog", d))





