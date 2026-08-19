class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #keep track of all seen chars
        #build adj list
        # if cycle return "" (#edges >= #nodes)
        # if abc before ab return ""
        
        seenChars = set(words[0])

        adjList = [[] for _ in range(26)]
        indegree = [0]*26

        for i in range(1,len(words)):
            seenChars.update(words[i])
            lastWord = words[i-1]
            currWord = words[i]
            for j,char in enumerate(lastWord):
                if j >= len(currWord): return ""        # if abc before ab return ""
                if char != currWord[j]:
                    adjList[ord(char) - ord('a')].append(currWord[j])
                    indegree[ord(currWord[j]) - ord('a')] += 1
                    break
        
        que = []
        totaldegree = 0
        for i,degree in enumerate(indegree):
            totaldegree += degree
            if degree == 0 and chr(ord('a')+i) in seenChars:
               que.append(i)

        if totaldegree >= len(seenChars): return ""            #more edges than nodes --> cycle

        ret = []
        while que:
            nextQue = []
            for i in que:
                ret.append(chr(ord('a')+i))
                for char in adjList[i]:
                    indegree[ord(char)-ord('a')] -= 1
                    if indegree[ord(char)-ord('a')] == 0:
                        nextQue.append(ord(char)-ord('a'))

            que = nextQue
        
        return "".join(ret)




