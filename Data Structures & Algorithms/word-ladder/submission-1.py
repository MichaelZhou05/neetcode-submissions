class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ret = float('inf')

        # if beginWord == endWord: return 0
        visited = set()
        que = deque()
        que.append(beginWord)
        count = 1
        while que:
            currWord = que.popleft()
            
            if currWord == endWord:
                return count
            
            if currWord in visited:
                continue
            visited.add(currWord)
            
            for change in wordList:
                counter = 0
                diff = True
                for i,char in enumerate(currWord):
                    if char != change[i]:
                        counter += 1
                    if counter > 1:
                        diff = False
                        break
                if diff : 
                    print(currWord + " --> " + change)
                    que.append(change)
            count += 1 

        return 0