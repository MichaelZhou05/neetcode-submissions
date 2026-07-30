class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ret = float('inf')

        # if beginWord == endWord: return 0
        visited = set()
        def dfs(word ,count):
            if word == endWord:
                nonlocal ret
                ret = min(count,ret)
                return
            if word in visited:
                return

            visited.add(word)
        
            for change in wordList:
                counter = 0
                diff = True
                for i,char in enumerate(word):
                    if char != change[i]:
                        counter += 1
                    if counter > 1:
                        diff = False
                        break
                if diff: 
                    print(word+ " ---> " + change)
                    dfs(change, count+1)
                    
        
        dfs(beginWord,1)


        return ret if ret < float('inf') else 0